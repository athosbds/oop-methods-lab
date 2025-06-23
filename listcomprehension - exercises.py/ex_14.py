import requests
url = "https://jsonplaceholder.typicode.com/users"
posts = "https://jsonplaceholder.typicode.com/posts"

url_respo = requests.get(url)
posts_respo = requests.get(posts)

if url_respo.status_code == 200 and posts_respo == 200:
        data_url = url_respo.json()
        data_posts = posts_respo.json()
        email_list = [
            person["name"] for person in data
            if "biz" in person["email"]
        ]
else:
    email_list = []
print(f'Pessoas com Biz no email:')
for person in email_list:
    print(f'{person}')