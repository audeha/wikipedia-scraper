import requests

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
    elif infotext == 200:
        print("Your cookie is valid")
    else:
        print("There's an error with your cookie.")

def get_country(cookie):
    get_country = "/countries"
    country = requests.get(root_url + get_country, cookies=cookie)
    try:
        output= country.json()
    except json.JSONDecodeError:
        # If an error occurs, print the error and return None
        print("Failed to parse JSON")
        return None
    return output

def get_leaders(cookie, countries):
    get_leaders = "/leaders"
    #initializing the list
    all_leaders = []

    for country in countries:
        leaders = requests.get(root_url + get_leaders + "?country=" + country, cookies=cookie)
        #we append the response to all_leaders for each country
        all_leaders.append(leaders.text)
    return all_leaders

def get_leader_info(cookie, leader_id):
    mydata = json.loads(all_leaders_json)
    all_ids = []

    for inner_list in mydata:
        for obj in inner_list:
            all_ids.append(obj['id'])
            return all_ids

    get_leader_details = "/leader"
    all_leader_info = []

    for id in all_ids:
        payload = {"leader_id":id}
        r = requests.get(root_url + get_leader_details, params=payload, cookies=cookie)
        leader_info = r.json()
        all_leader_info.append(leader_info)
