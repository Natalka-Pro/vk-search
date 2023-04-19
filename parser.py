import requests


def print_dict(d, indent, local_indent):
    """
    Input:  d, <class 'dict'>
            indent, <class 'int'> - the number of spaces in the indentation, constant, equal to 4
            local_indent, <class 'int'> - the number of spaces, added to each line in the output
    Return: <class  'str'>, it contains a "beautiful" RECURSIVE representation of the input
    """
    s = "{\n"
    for key, value in d.items():
        if type(value) is dict:
            s0 = " " * (local_indent + indent) + f"\"{key}\": "
            s += s0
            s += print_dict(value, indent, local_indent + len(s0))
        else:
            s += " " * (local_indent + indent) + f"\"{key}\": {value}, \n"
    s += " " * local_indent + "}\n"
    return s


def print_ListOfDicts(l):
    s = ""
    indent = 4
    local_indent = 0
    for i, d in enumerate(l):
        s += f"-------------------------------- Элемент {i} -------------------------------- \n"
        s += print_dict(d, indent, local_indent)
    return s
  

def print_FriendsToFile(user, number, file):
    """
    Input:  user, <class 'int'>   - id of the user to get a list of friends for
            number, <class 'int'> - the number of friends to return
            file, <class 'str'>   - file name
    Return: <class 'NoneType'>, the function writes information about friends to a file
    """
    access_token = 'eaae23abeaae23abeaae23abdbe9bdb8f1eeaaeeaae23ab8e923c275dce8f0a13fa6e39'
    api_version  = '5.131'

    friends = []
    count = 100
    num_friends = -1

    params = {
        'beginning'	: 'https://api.vk.com/method',
        'user' 		:  user,
        'ending'	: f'access_token={access_token}&v={api_version}',
    }
    
    if type(user) is str and "/" in user: # обрезка ссылки
        idx = user.rfind("/")
        params['user'] = user[idx + 1 :]
    
    # получение id пользователя
    url = '{beginning}/users.get?user_ids={user}&lang=0&{ending}'
    # print(f"-{params['user']}-")
    url_formatted = url.format(**params)
    data = requests.get(url_formatted).json()
    # print(data)
    params['user'] = data["response"][0]["id"]
    # print(params['user'])

    fields = "fields=bdate,city,country,sex"
    url = '{beginning}/friends.get?user_id={user}&{fields}&lang=0&count={count}&offset={offset}&{ending}'
    for i in range(0, number, count):
        if count + i >= number:
            count = number - i
        url_formatted = url.format(count = count, offset = i, fields=fields, **params)
        res_friends = requests.get(url_formatted)
        data = res_friends.json().get("response")

        if data is None:
            print(res_friends.json())
            raise TypeError("VK API returned an error!")

        num_friends = data['count']

        for friend in data['items']: 
            friends.append(friend)		

    with open(file, 'w') as output_file:
        output_file.write(f"Количество друзей у пользователя: {num_friends}\n")
        output_file.write(f"Количество друзей в этом файле:   {len(friends)}\n")
        output_file.write(print_ListOfDicts(friends))


if __name__ == "__main__":
    user = 'https://vk.com/strong_machina'
    file = 'response.txt'
    number = 111
    print_FriendsToFile(user, number, file)
