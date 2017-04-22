from database import Database


class User:

    db = None

    def __init__(self):
        self.db = Database()

    def get_user_list(self):
        user_list = []
        response = []
        try:
            users = self.db.select("SELECT name, cref, uf FROM user")
            for user in users:
                user_list.append(
                    {
                        "username": user[0],
                        "cref": user[1],
                        "uf": user[2],
                    }
                )
            response.append({'message': "Ok", 'code': 200, 'users': user_list})
        except Exception as e:
            response.append({'message': e.message, 'code': 404})

        return response

    def create_new_user(self, username, cref, uf):
        return self.db.insert('user', ['name', 'cref', 'uf'], [username, cref, uf])
