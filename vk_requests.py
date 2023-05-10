from vkbottle import API, vkscript
import asyncio
# import json

def print_dict(d, indent = 4, local_indent = 0):
    """
    Input:  d, <class 'dict'>
            indent, <class 'int'> - the number of spaces in the indentation, constant, equal to 4
            local_indent, <class 'int'> - the number of spaces, added to each line in the output
    Return: <class  'str'>, it contains a "beautiful" RECURSIVE representation of the input
    """
    if type(d) is not dict:
        return f"{d}\n"
    
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
        s += f"-------------------------------- Элемент {i} --------------------------------\n"
        s += print_dict(d, indent, local_indent)
    return s


def required_fields_dict(d : dict, fields = ""):
    """
    Return: new dict with fewer keys
    """
    if type(d) is not dict:
        return d
    fields = "id,first_name,last_name,can_access_closed,is_closed," +  fields
    fields = fields.replace(",", " ").split()
    new_dict = {}
    for key in fields:
        new_dict[key] = d[key]

    return new_dict


def required_fields_list(l : list, fields = ""):
    new_list = []
    for d in l:
        new_list += [required_fields_dict(d, fields)]

    return new_list


async def get_id(api, screen_name):
    response = await api.users.get(user_ids = screen_name)
    response = response[0].dict()
    id = response["id"]
    return id


async def link_processing(api, link):
    if type(link) is not str:
        return link
    elif "/" in link:           # обрезка ссылки
        idx = link.rfind("/")
        link = link[idx + 1 :]

    if link.isdigit():
        id = int(link)
    else:
        id = await get_id(api, link)
        
    return id


@vkscript
def get_friends_script(api, count, params):
    user_id = params.user_id
    fields = params.fields
    lang = params.lang

    total_friends = []

    response = api.friends.get(user_id=user_id, count = 1)
    num_friends = response.count

    i = 0
    while i < num_friends:
        response = api.friends.get(count = count, offset = i, 
                                   user_id=user_id, fields=fields, 
                                   lang=lang) # переключение языка не работает
        total_friends += response.items
        i += count

    return {"count" : num_friends, 
            "items" : total_friends,
            }


def find_friends(name, list_friends):
    idx = []
    for elem in list_friends:
        if name in elem["first_name"] or name in elem["last_name"]:
            idx += [{"first_name"   : elem["first_name"],
                      "last_name"   : elem["last_name"],
                      "link"        : f"https://vk.com/id{elem['id']}",
                    }]

    return idx

    
async def get_friends(access_token, user_id):
    api = API(token=access_token)
    user_id = await link_processing(api, user_id)
    params = {
        'user_id'   :  user_id,
        'fields'    :  "bdate,city,country,sex",
        'lang'      :  0,
    }

    count = 1000
    response = await api.execute(code=get_friends_script(count=count, params=params))
    response = response["response"]
    # response = await api.friends.get(**params, count = 10000, offset = 0)
    # response = response.dict()
    num_friends = response["count"]
    total_friends = response["items"]
    return num_friends, total_friends


async def main():
    access_token = 'eaae23abeaae23abeaae23abdbe9bdb8f1eeaaeeaae23ab8e923c275dce8f0a13fa6e39'
    # user_id = "https://vk.com/id348249759"  # у него почти максимальное число друзей
    user_id = "https://vk.com/strong_machina"
    num_friends, list_friends = await get_friends(access_token, user_id)

    name = "lex"
    res = find_friends(name, list_friends)

    with open('response.txt', 'w') as output_file:
        output_file.write(f"Количество друзей у пользователя: { num_friends }\n")
        output_file.write(f"Количество друзей в этом файле:   { len(list_friends) }\n")
        output_file.write(print_ListOfDicts(list_friends) + "\n\n\n")
        output_file.write(f"Результат поиска по '{name}': \n{print_ListOfDicts(res)}")


if __name__ == "__main__":
    asyncio.run(main())
