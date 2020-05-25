"""
This transforms a curl bash command string into arguments for Python requests. This allows you to conveniently modify URL parameters or headers before making requests in Python. 
Only works for GET requests. Not tested on POST/PUT/PATCH/DELETE as I did not need the script to work in those cases when I wrote it. 
Might update the script to handle POST/PUT/PATCH/DELETE requests if I ever need it. 
"""

import json
from urllib.parse import parse_qs


def curl_to_python_requests_params(curl_command_string):

    original_url, *split_headers = curl_command_string.strip(" '").split()[1:-1]
    original_url = original_url.strip(" '")

    # Extract the url and url_parameters
    url, url_params_string = original_url.split("?")
    url_params = parse_qs(url_params_string)

    # Extract the headers
    headers_string = " ".join(split_headers)
    header_strings_list = [el.strip(" '") for el in headers_string.split("-H") if el.strip()]
    quoted_header_strings_list = ['"' + el.replace(": ", '": "') + '"' for el in header_strings_list]
    headers_json_string = "{" + ", ".join(quoted_header_strings_list) + "}"
    headers = json.loads(headers_json_string)

    # requests.request("GET", url, params=url_params, headers=headers)
    return url, url_params, headers


if __name__ == "__main__":
    curl_command_string = input("Copy-paste the curl (bash) command string here: ")
    url, url_params, headers = curl_to_python_requests_params(curl_command_string)

    print("\nPython code to replicate the curl request:\n")
    print("import requests")
    print(f'url = "{url}"')
    print(f"url_params = {url_params}")
    print(f"headers = {headers}")
    print('response = requests.request("GET", url, params=url_params, headers=headers)')
    print("try:")
    print("    response.json()")
    print("except:")
    print("    response.text")
