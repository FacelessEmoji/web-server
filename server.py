from flask import Flask, jsonify

app = Flask(__name__)


# Простой класс для сущностей
class Entity:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# Создаем несколько сущностей
entities = [
    Entity(1, "Entity One"),
    Entity(2, "Entity Two"),
]


# Страница healthcheck
@app.route('/health')
def healthcheck():
    return "Service is up and running", 200


# Страница для вывода сущностей
@app.route('/')
def get_entities():
    response = [{'id': entity.id, 'name': entity.name} for entity in entities]
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)
