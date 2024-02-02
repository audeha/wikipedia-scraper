#calls the API and creates a JSON file

import requests
from bs4 import BeautifulSoup
import json

from src.scraper import get_cookie, get_country, get_leaders, get_first_paragraph, to_json_file
root_url = "https://country-leaders.onrender.com"

mycookie = get_cookie()
all_countries = get_country(mycookie)
all_leaders = get_leaders(mycookie, all_countries)

# Collecting all leader IDs
all_ids = []
for country, leaders in all_leaders.items():
    for leader in leaders:
        # Process each leader's information here
        all_ids.append(leader['id'])

# Fetching detailed information for each leader
get_leader_details = "/leader"
all_leader_info = []

for id in all_ids:
    payload = {"leader_id": id}
    response = requests.get(root_url + get_leader_details, params=payload, cookies=mycookie)
    if response.status_code == 200:
        leader_info = response.json()
        all_leader_info.append(leader_info)
    else:
        print(f"Failed to fetch data for leader ID {id}")

# Collecting first paragraphs
first_paragraphs = {}

for leader_info in all_leader_info:
    myurl = leader_info['wikipedia_url']
    first_paragraph = get_first_paragraph(myurl)
    first_paragraphs[leader_info['id']] = first_paragraph

# Writing all first paragraphs to the file
details_file_path = "leaders_data.json"
to_json_file(first_paragraphs, details_file_path)
