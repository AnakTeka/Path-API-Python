import requests
from pprint import pprint


class PathAPI:

    API_URL = "https://path.com/a/"

    def __init__(self, user_login, user_password):
        self.user_login = user_login
        self.user_password = user_password
        self.session = requests.Session()

        response = self.session.post(self.API_URL + "login",
                                    data={"emailId": user_login,
                                        "password": user_password})

        if response.status_code == 200:  # Login success
            data = response.json()
            self.meId = data['user']['id']
        else:
            return

    def getHome(self):
        params = {"ww": "562", "wh": "530", "meId": self.meId}
        response = self.session.get(self.API_URL + "feed/home", params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return

    def getFriends(self):
        params = {"locale": "en", "meId": self.meId}
        response = self.session.get(self.API_URL + "friends", params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return

    def getFriendFeedbyId(self, friend_id):
        params = {'ww': '566',
                  'wh': '530',
                  'user_id': friend_id,
                  'meId': self.meId}

        response = self.session.get(self.API_URL + "feed", params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return

    def comment(self, moment_id, comment_body):
        params = {'moment_id': moment_id,
                  'comment_body': comment_body,
                  'meId': self.meId}

        response = self.session.post(self.API_URL + "moment/comment/add", data=params)
        if response.status_code == 200:
            return response.json()
        else:
            return

    def commentEmotion(self, moment_id, emotion_type):
        """
        There are 5 emotion types, sad, happy, laugh, love, and surprise
        """

        params = {"moment_id": moment_id,
                  "emotion_type": emotion_type,
                  "meId": self.meId}

        response = self.session.post(self.API_URL + "moment/emotion/add", data=params)
        if response.status_code == 200:
            return response.json()
        else:
            return


if __name__ == "__main__":
    username = None
    password = None

    api = PathAPI(username, password)
    home = api.getHome()
    moments = home['momentSet']
    moment_created = {k: v['created'] for k, v in moments.items()}
    latest_moment = sorted(moment_created.keys())[-1]
    # post = api.comment(latest_moment,"Hi, there!")

    teman = api.getFriends()
    friends = {}
    for k,user in teman['users'].items():
        # print(user['first_name'], user['last_name'])
        friends[k] = user['first_name'] + user['last_name']
    # print(friends)

    for friend_id, friend in friends.items():
        if "yoga" in friend:
            user_id = friend_id
    print(user_id)
    # yoga = api.getfriendfeedbyid(user_id)
    # yoga.pop('users', none)
    # yoga_moment = yoga['momentset']
    # for k, v in yoga_moment.items():
    #     pprint(v['headline'])
    # pprint(yoga['momentSet'])

    # lol = api.comment(latest_moment,"Haloo")
    # pprint(lol)
    # for k,v in moments.items():
    #     moment_created = []
    #     pprint(v['created'])

    # pprint(home['momentSet'])
    # api.getFriends()
    # api.getFriendFeed("Franky")

