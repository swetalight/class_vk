import requests

from pprint import pprint

class FriendsVK:

    def __init__(self, token, user_id):
        self.user_id = user_id
        self.token = token

    def get_params(self, token, user_id):
        return {
            'v': '5.92',
            'access_token': token,
            'user_id': user_id
        }

    def friends_user(self, token, user_id):
        params = self.get_params(self.token, self.user_id)
        #print (self.token, self.user_id)
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params)

        return response.json()

def transform(json_data):
    friends_dict = set()
    for i in range(len(json_data['response']['items'])):
        str = json_data['response']['items'][i]
        friends_dict.add(str)
        # print (str)
    #print(friends_dict)
    return friends_dict

def url_friends(friends):
    list_friends = friends

    for i in list_friends:
        friends_URL = 'https://vk.com/id' + str(i)
        print(friends_URL )




if __name__ == '__main__':
    TOKEN = '7e356f4d12943a9620e4136bcdfadaa3378957b36630f887600f253dd7946e429a9d297677dfa67002c74'

    USER_ID = '926104'
    user1 = FriendsVK(TOKEN, USER_ID)
    friends1 = transform(user1.friends_user(TOKEN, USER_ID))
    pprint(friends1)


    USER_ID = '525932455'
    user2 = FriendsVK(TOKEN, USER_ID)
    friends2 = transform(user2.friends_user(TOKEN, USER_ID))
    pprint(friends2)

    tot= friends1 & friends2
    url_friends(tot)
    print (tot)

    