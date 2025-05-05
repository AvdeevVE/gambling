from flask import Flask, Response
from flask_cors import CORS
import json
from flask import Flask, Response, jsonify, request
from sqlalchemy import create_engine, text, bindparam


connection_string = "mysql+pymysql://ava:1234@192.168.50.129:3306/test"
engine = create_engine(connection_string, echo=True)

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/")
def index():
    return "Hello world"



@app.route("/api/course/all")
def get_products():
    with engine.connect() as connection:
        raw_result = connection.execute(text("SELECT * FROM Course"))
        result = []
        for r in raw_result.all():
            result.append(r._asdict())
        return jsonify(result)
    return Response(jsonify({"status": "500", "message": "Database is down!"}), status=500)

def main():
    app.run("localhost", 8000, True)

if __name__ == "__main__":
    main()