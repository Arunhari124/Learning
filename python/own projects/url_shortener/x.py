import json

url = "www.nigg.com"

# Load existing data
try:
    with open("url.json", "r") as file:
        urls = json.load(file)

        # If file contains something other than a dict
        if not isinstance(urls, dict):
            urls = {}

except (FileNotFoundError, json.JSONDecodeError):
    urls = {}


def url_short(url):
    parts = url.split(".")

    if len(parts) > 1:
        domain = parts[1]

        short_string = domain[:3]

        urls[url] = short_string

        with open("url.json", "w") as file:
            json.dump(urls, file, indent=4)

        print(f"Original URL : {url}")
        print(f"Short URL    : {short_string}")


url_short(url)
