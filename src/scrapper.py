# Standard library imports
from typing import List

# External dependencies
from requests_html import HTMLSession

# Type Alias for readibility (Only compatible from Python ~= 3.12.x)
type Link = str


# Getting the html response from the website link provided
session: HTMLSession = HTMLSession()
website_link: Link = "https://"


def scrape():
    try: 
        html_src: str = session.get(website_link)
        print(html_src.html.links)
    
    except:
        print("Something went wrong with the link you provided.")