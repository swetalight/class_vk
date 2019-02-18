import requests

from pprint import pprint

class FriendsVK:

    def __init__(self, token, user_id):
        super().__init__()
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

    def transform(self, json_data):
        friends_dict = set()
        for i in range(len(json_data['response']['items'])):
            str = json_data['response']['items'][i]
            friends_dict.add(str)
            # print (str)
        # print(friends_dict)
        return friends_dict

    def url_friends(self,friends):
        list_friends = friends
        result_url_profile = []
        for i in list_friends:
            friends_URL = 'https://vk.com/id' + str(i)
            result_url_profile.append(friends_URL)
            #print(result_url_profile)
        return result_url_profile

    def __str__(self):
        return 'https://vk.com/id{id}'.format(id=self.user_id)

    def __and__(self, other):
        self_dict = self.transform(self.friends_user(self.token, self.user_id))

        other_dict = other.transform(other.friends_user(other.token, other.user_id))


        #print (self_dict)
        #print(other_dict)

        #common_friends = set(self_dict.keys()) & set(other_dict.keys())
        common_friends = set(self_dict & other_dict)
        #print ('common_friends {}'.format(common_friends))

        # friends = []
        # friends = common_friends
        #print (common_friends)

        list_vk = self.url_friends(common_friends)

        #print (list_vk)

        return list_vk

###END OF CLASS





if __name__ == '__main__':
    TOKEN = '59a3a8e788f9aa9d76f4a9b5f0e854373672f86b0af3d01df94762ed97125df74e095211c9c4cab6f2c86'

    USER_ID = '926104'
    user1 = FriendsVK(TOKEN, USER_ID)



    USER_ID = '525932455'
    user2 = FriendsVK(TOKEN, USER_ID)

    print ('Общие друзья')
    print (user1.__and__(user2))

    print ("Пользователь")
    print (user2)

    print("Пользователь")
    print(user1)