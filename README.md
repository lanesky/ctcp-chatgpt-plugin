# Clinical Trial Criteria Parser ChatGPT Plugin

## General

The Clinical Trial Criteria Parser is a ChatGPT plugin that meticulously extracts and analyzes eligibility criteria from clinical trial records. By leveraging the advanced language understanding capabilities of ChatGPT, this plugin identifies and categorizes key medical terms and patient demographics from the inclusion and exclusion criteria. This aids in providing a clear, concise, and structured overview of the trial's participant requirements.


Uploading Screen Recording 2023-05-17 at 12.27.24.mov…


## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com.
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

The plugin should now be installed and enabled! You can start with a NCT Trial ID like "nctid NCT05859269" and then try adding something to it as well!
