# bugzilla-rest

This is a simple Python Script that you can use to consume the Bugzilla REST API to collect bugs for any research and analysis purpose.

Some of the actions requires authentication for which you need to get the token from https://bugzilla.mozilla.org/ (Go to Profile -> Preferences -> API keys and generate one if you haven't done yet)

## To run the Script
1) Clone the repo
2) install requests module `pip install requests`
3) Add your API key in `helpers.py` in the place of `<your-bugzilla-api-key>`
4) Change any configuration if you want to.
5) Run the script `python scrape.py`

If you found this helpful, feel free to star. And also you can raise PR for other functionalities like getting details of specific bug, getting classifications, posting a bug, etc.
