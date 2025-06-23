import requests
url = "https://jsonplaceholder.typicode.com/users"
posts = "https://jsonplaceholder.typicode.com/posts"

url_respo = requests.get(url)
posts_respo = requests.get(posts)

if url_respo.status_code == 200 and posts_respo.status_code == 200:
        data_url = url_respo.json()
        data_posts = posts_respo.json()
        email_list = [
            person["name"] for person in data_url
            if "biz" in person["email"]
        ]

        filter_posts = [
             { 'id': post['id'], 'title': post['title']}
             for post in data_posts
             if len(post['title']) > 5
        ]
        print(f'Posts com Título com mais de 5 Palavras')
        for post in filter_posts:
             print(f"ID: {post['id']} - Título: {post['title']}")
        print(f'\nPessoas com Biz no email:')
        for person in email_list:
            print(f'{person}')
else:
    print(f'Erro ao acessar')


