import requests

GOOGLE_BOOKS_API_URL = "https://www.googleapis.com/books/v1/volumes"

def search_books(query):
    params = {"q": query, "key": "YOUR GOOGLE BOOK API KEY"}
    response = requests.get(GOOGLE_BOOKS_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return {}

def get_book_details(volume_id):
    url = f"{GOOGLE_BOOKS_API_URL}/{volume_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {}
