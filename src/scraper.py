import requests
import json
from bs4 import BeautifulSoup

root_url = "https://country-leaders.onrender.com"

def get_cookie():
    """get cookie from api"""
    cookie_url = "/cookie"
    r = requests.get(root_url + cookie_url)
    mycookie = r.cookies
    return mycookie

def refresh_cookie(cookie):
    """returns a new cookie if the cookie has expired"""
    cookie_info = "/check"
    infoc = requests.get(root_url + cookie_info, cookies=cookie)
    infotext = infoc.status_code
    if infotext == 403:
        print("The cookie is missing or has expired")
        print("CReating new cookie...")
        return get_cookie()
        print("Your cookie has been created")
    elif infotext == 200:
        print("Your cookie is valid")
    else:
        print("There's an error with your cookie.")
    return cookie

def get_country(cookie):
    """returns a list of the supported countries from the API"""
    get_country = "/countries"
    country = requests.get(root_url + get_country, cookies=cookie)
    try:
        output = country.json()
    except json.JSONDecodeError:
        # If an error occurs, print the error and return None
        print("Failed to parse JSON")
        return None
    return output

def get_leaders(cookie, countries):
    """Populates the `leader_data` dict with the leaders of each country retrieved from the API"""
    get_leaders = "/leaders"
    leader_data = {}

    for country in countries:
        leaders = requests.get(root_url + get_leaders + "?country=" + country, cookies=cookie)
        try:
            # Assuming the API returns JSON data
            leader_data[country] = leaders.json()
        except json.JSONDecodeError:
            print(f"Failed to parse JSON for country: {country}")
            leader_data[country] = []

    return leader_data

def get_first_paragraph(wikipedia_url):
    """returns the first paragraph from the wikipedia url"""
    response = requests.get(wikipedia_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all paragraphs
    paragraphs = soup.find_all('p')
    for paragraph in paragraphs:
        # Check if the paragraph starts with a <b> tag
        if paragraph.find('b'):
            return paragraph.text

    return 'No paragraph with bold text found'

def to_json_file(data, filepath: str):
    """stores the data structure into a JSON file"""
    with open(filepath, 'a') as ofile:
        ofile = json.dumps(data, indent=4, sort_keys=True)
