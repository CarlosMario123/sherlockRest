from sherlock_lib import search_target

def searchUser(username):
    result = search_target(username,sfw=True)
    return result