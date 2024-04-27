import json
import os

def update_sum(user, sum, stars):
    d = {'user': user, 'summary': sum, 'stars': stars}
    with open(f"users/{user}.json","w", encoding='utf-8') as jsonfile:
        json.dump(d,jsonfile,ensure_ascii=False)


def fetch_user_hist(user):
    if os.path.exists(f"users/{user}.json"):
        a = json.load(open(f"users/{user}.json",'r'))

        return a['summary']
    else:
        return ''
