import requests
respuesta = requests.get("https://jsonplaceholder.typicode.com/posts/1")
resp_json=respuesta.json()
print(resp_json['title'])
print(resp_json['body'])
r=requests.post("https://jsonplaceholder.typicode.com/posts", {"title": 'Juan', "body": "me gusta el rocket", "userId": '12', "id": '12'})
print(r.status_code)
user=requests.post("https://jsonplaceholder.typicode.com/users", {"title": 'Fer', "body": "le gusta el pene", "userId": '13', "id": '13'})
print(user.status_code)
user2=requests.post("https://regres.in/", )
print(user2.text)