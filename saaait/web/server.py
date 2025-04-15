from flask import Flask, Response
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return "Hello world"

@app.route("/api/course/all")
def get_course():
    course = [
        {
            "name": "Мега арбетраш",
            "description": "Мамкин арбетрашник йоу",
            "DCF": "08.04.2025",
            "photo": "https://i0.wp.com/ru.facemarket.org/wp-content/uploads/2024/03/macan1.png?fit=826%2C1024&ssl=1"
        },
        {
            "name": "Сева трейд",
            "description": "Инфоцыганский курс Севы Типова",
            "price": 200,
            "photo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTozQg9TArct9e1aFafp-zQR8N2i7NXKs2vyg&s"
        },
        {
            "name": "Массаж простоты",
            "description": "Простой массаж для мужчин",
            "DCF": "22.05.2023",
            "photo": "https://img-webcalypt.ru/uploads/admin/images/meme-templates/Sbj26C3isBa1TKxZBwTbLNqI6gb9pBhi.jpg"
        },
        {
            "name": "Владмен Авдекарян",
            "description": "Научись быть мужыком",
            "DCF": "22.05.2023",
            "photo": "https://www.rubaltic.ru/upload/iblock/507/50754a7983e10231bc1ad81aae8c6e91.jpg"
        },
    ]
    return Response(json.dumps(course), content_type="application/json")

def main():
    app.run("localhost", 8000, True)

if __name__ == "__main__":
    main()