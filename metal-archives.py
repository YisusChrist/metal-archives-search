import requests
from bs4 import BeautifulSoup


SEARCH_TEXT = "Human Improvement Process"


def find_text_in_forum():
    # base_url = "https://forum.metal-archives.com/viewforum.php?f=27&start={}"
    base_url = "https://forum.metal-archives.com/viewtopic.php?f=27&t=64985&start={}"
    offset = 0

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    while True:
        url = base_url.format(offset)
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        if response.status_code != 200:
            print("Error retrieving the page:", response.status_code)
            return

        soup = BeautifulSoup(response.content, "html.parser")
        content = soup.get_text()
        if SEARCH_TEXT in content:
            print("Text found! URL:", url)
            return

        offset += 40
        print(f"Not found with url {url}")


if __name__ == "__main__":
    find_text_in_forum()
