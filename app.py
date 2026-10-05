from flask import Flask
from routes.task_routes import task_bp

app = Flask(__name__)

app.register_blueprint(task_bp)



if __name__ == "__main__":
    app.run(debug=True)