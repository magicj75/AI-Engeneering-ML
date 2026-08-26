import requests

params = {
    "name": "name",
}

response = requests.get("https://api.github.com/users/octocat", params=params)

print(response)