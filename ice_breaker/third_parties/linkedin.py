import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profile
    Manually scrape the information from the LinkedIn"""
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        res = requests.get(linkedin_profile_url, timeout=10)
        return res.json()
    else:
        return {}


if __name__ == "__main__":
    print(scrape_linkedin_profile("asdasd", True))
