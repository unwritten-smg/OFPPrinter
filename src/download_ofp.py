# Imports
import requests


def downlaod_ofp(user_id):
    URL = f"https://www.simbrief.com/api/xml.fetcher.php?userid={user_id}"
    response = requests.get(URL)
    with open('./data/simbrief_data.xml', 'wb') as file:
        file.write(response.content)