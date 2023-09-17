# import requests
# user_id = 12345
# url = 'https://vk.com/genshinmedia'
# # url для второй страницы
# r = requests.get(url)
# with open('test.html', 'w') as output_file:
#   output_file.write(r.text)

# import requests
# url = "https://api.vk.com/method/friends.get?user_id=ТУТ_ID&fields=bdate&access_token=ТУТ_ТОКЕН"
# data = requests.get(url).json()
# print(data)

user = 'https://vk.com/id30753288'

# if type(user) is str and "/" in user:
# 		idx = user.rfind("/")
# 		user = user[idx + 1 :]

# if type(user) is str and "id" in user:
# 		idx = user.find("id")
# 		user = user[idx + 2 :]
		
# print(user)


d = {"qweqeweqw" : 2, }
print(dir(d))

# response = await api.friends.get(**params, count = 10000, offset = 0)
# response = await api.friends.get(user_id=user_id, count = 10000)
# data = response.dict()
# num_friends = data['count']
# friends = data['items']
# friends = required_fields_list(data['items'], params["fields"])
