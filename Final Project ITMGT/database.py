users = {
    "juanaruego@example.com":{"password":"MusicMan",
                         "first_name":"Niki",
                         "last_name":"Zefanya"},
}


def get_user(username):
    try:
       return users[username]
    except KeyError:
       return None