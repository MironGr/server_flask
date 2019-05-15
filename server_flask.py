# Создание пользователя (группы пользователей)
# Удаление пользователя (гр пользов)
# Обовление пользователя (гр польз)
# Получение данных о пользователе (гр польз)


from flask import Flask, request, render_template

import User
import Users

app = Flask(__name__)
data = {}


@app.route('/users/<user>', methods=['GET', 'POST', 'DELETE'])
def user(user=None):

    if request.method == 'GET':
        user_1 = render_template(name=user)
        return User.get_user(user=user_1)

    elif request.method == 'POST':
        user_1 = render_template(name=user)
        return User.create_user(user=user_1)

    elif request.method == 'DELETE':
        user_1 = render_template(name=user)
        return User.delete_user(user=user_1)


@app.route('/users', methods=['GET', 'DELETE'])
def users():

    if request.method == 'GET':
        return Users.get_users()

    elif request.method == 'DELETE':
        return Users.delete_users()


if __name__ == '__main__':
    app.run()
