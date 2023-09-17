from vkbottle import vkscript, API
import asyncio


MAX_MEMS_TOTAL = 25000  # vkscript can't send more than 5 mb
MAX_MEMS_SINGLE = 1000  # get_members returns less than 1000 members


@vkscript
def get_members(api):
    # total_mems = []
    # i = offset
    # while i + per_req <= offset + count:
    #     mems = api.groups.get_members(group_id=group_id, offset=i, count=per_req).items
    #     total_mems.extend(mems)
    #     i += per_req
    # if count % per_req != 0:
    #     mems = api.groups.get_members(group_id=group_id, offset=count / per_req * per_req, count=count % per_req).items
    #     total_mems.extend(mems)
    # return {'items': total_mems}
    total_friends = []
    num_friends = '222'
    count = 1000
    return {num_friends: count}


async def get_subscriptions_members(api: API, user_id: int):
    try:
        subs = await api.users.get_subscriptions(user_id=user_id)
    except:
        return []  # private profile
    subs = subs.groups.items  # list of sub ids
    mems = await api.execute(code=get_members(group_id=subs[0], offset=MAX_MEMS_SINGLE, 
                                            count=MAX_MEMS_TOTAL,
                                            per_req=MAX_MEMS_SINGLE)) 
    

    # for sub in subs:
    #     mems = await api.groups.get_members(group_id=sub)  # set of mem ids
    #     total_mems.extend(mems.items)
    #     total_mems_count = mems.count
    #     for i in range(MAX_MEMS_SINGLE, total_mems_count - MAX_MEMS_TOTAL + 1, MAX_MEMS_TOTAL):
    #         mems = await api.execute(code=get_members(group_id=sub, offset=i, count=MAX_MEMS_TOTAL,
    #                                                   per_req=MAX_MEMS_SINGLE))  # vkscript handles 25 requests
    #         total_mems.extend(mems['response']['items'])
    #     if total_mems_count % MAX_MEMS_TOTAL != 0:
    #         mems = await api.execute(code=get_members(group_id=sub,
    #                                                   offset=((total_mems_count - MAX_MEMS_SINGLE) // MAX_MEMS_TOTAL *
    #                                                           MAX_MEMS_TOTAL + MAX_MEMS_SINGLE),
    #                                                   count=(total_mems_count - MAX_MEMS_SINGLE) % MAX_MEMS_TOTAL,
    #                                                   per_req=MAX_MEMS_SINGLE))
    #         total_mems.extend(mems['response']['items'])
    return mems


async def main():
    access_token = 'eaae23abeaae23abeaae23abdbe9bdb8f1eeaaeeaae23ab8e923c275dce8f0a13fa6e39'
    api = API(token=access_token)
    user_id = "30753288"
    mems = await get_subscriptions_members(api, user_id)

    with open('response.txt', 'w') as output_file:
        output_file.write(f"Количество друзей у пользователя: \n {mems}\n")

asyncio.run(main())
