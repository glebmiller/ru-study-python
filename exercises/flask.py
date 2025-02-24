from typing import Any
from flask import Flask
from flask import request
import json


app = Flask(__name__)
dict_of_users = dict()


class FlaskExercise:
    """
    Вы должны создать API для обработки CRUD запросов.
    В данной задаче все пользователи хранятся в одном словаре, где ключ - это имя пользователя,
    а значение - его параметры. {"user1": {"age": 33}, "user2": {"age": 20}}
    Словарь (dict) хранить в памяти, он должен быть пустым при старте flask.

    POST /user - создание пользователя.
    В теле запроса приходит JSON в формате {"name": <имя пользователя>}.
    Ответ должен вернуться так же в JSON в формате {"data": "User <имя пользователя> is created!"}
    со статусом 201.
    Если в теле запроса не было ключа "name", то в ответ возвращается JSON
    {"errors": {"name": "This field is required"}} со статусом 422

    GET /user/<name> - чтение пользователя
    В ответе должен вернуться JSON {"data": "My name is <name>"}. Статус 200

    PATCH /user/<name> - обновление пользователя
    В теле запроса приходит JSON в формате {"name": <new_name>}.
    В ответе должен вернуться JSON {"data": "My name is <new_name>"}. Статус 200

    DELETE /user/<name> - удаление пользователя
    В ответ должен вернуться статус 204
    """

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.route("/user", methods=["POST"])
        def user() -> Any:
            request_data = request.get_json()
            if "name" in request_data:
                name = request_data.pop("name")
                dict_of_users[name] = request_data
                response_data = {"data": f"User {name} is created!"}
                response = app.response_class(
                    response=json.dumps(response_data), status=201, mimetype="application/json"
                )
                return response
            else:
                reply = {"errors": {"name": "This field is required"}}
                response = app.response_class(
                    response=json.dumps(reply), status=422, mimetype="application/json"
                )
                return response

        @app.route("/user/<user_id>", methods=["GET", "DELETE", "PATCH"])
        def user_modify(user_id: str) -> Any:
            if request.method == "GET":
                if user_id in dict_of_users:
                    response_data = {"data": f"My name is {user_id}"}

                    response = app.response_class(
                        response=json.dumps(response_data), status=200, mimetype="application/json"
                    )
                    return response
                else:
                    response = app.response_class(status=404)
                    return response

            if request.method == "PATCH":
                if user_id in dict_of_users:
                    request_data = request.get_json()
                    new_name = request_data["name"]
                    dict_of_users[new_name] = dict_of_users[user_id]
                    dict_of_users.pop(user_id)

                    response_data = {"data": f"My name is {new_name}"}
                    response = app.response_class(
                        response=json.dumps(response_data), status=200, mimetype="application/json"
                    )
                    return response
                else:
                    response = app.response_class(status=404)
                    return response

            if request.method == "DELETE":
                if user_id in dict_of_users:
                    dict_of_users.pop(user_id)
                    response = app.response_class(status=204)
                    return response
                else:
                    response = app.response_class(status=404)
                    return response


FlaskExercise.configure_routes(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
