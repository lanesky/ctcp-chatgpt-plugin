import json
import httpx
import quart
import quart_cors
from quart import request
from bs4 import BeautifulSoup

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

_TITLE = "Here are the Inclusion and Exclusion criteria for the clinical trial:"

async def fetch_trial_data(trialID):
    url = f"https://clinicaltrials.gov/ct2/show/study/{trialID}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.text

def parse_eligibility_criteria(html):
    soup = BeautifulSoup(html, 'html.parser')
    eligibilityCriteria = soup.find(id="eligibility").parent.parent.parent.find_all('ul')
    inclusionCriteria, exclusionCriteria = eligibilityCriteria[0].text.strip(), eligibilityCriteria[1].text.strip()
    return inclusionCriteria, exclusionCriteria


@app.route("/trial/<string:trialID>", methods=['GET'])
async def get_trial(trialID):
    try:
        html = await fetch_trial_data(trialID)
        inclusionCriteria, exclusionCriteria = parse_eligibility_criteria(html)
        result = { 'Title': _TITLE, 'Inclusion Criteria': inclusionCriteria, 'Exclusion Criteria': exclusionCriteria }
        return quart.Response(response=json.dumps(result), status=200, mimetype='application/json')
    except Exception as error:
        result = { 'Title': _TITLE, 'Inclusion Criteria': 'ERROR', 'Exclusion Criteria': 'ERROR', 'Error': str(error) }
        return quart.Response(response=json.dumps(result), status=500, mimetype='application/json')

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
