import requests

def get_random_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    joke_data = response.json()
    return joke_data["value"]

def main():
    joke = get_random_joke()
    print(joke)

if name == "main":
    main()