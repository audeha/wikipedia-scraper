#calls the API and creates a JSON file

import requests
from bs4 import BeautifulSoup

from src.scraper import get_cookie, get_country, get_leaders

mycookie = get_cookie()
all_countries = get_country(mycookie)
all_leaders = get_leaders(mycookie, all_countries)
