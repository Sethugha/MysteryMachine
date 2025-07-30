from flask import Flask
import config
from data_models import db, Prompt, Case, AIConfig
from os import path

exit()
app = Flask(__name__)

app.config.from_object('config.DevConfig')
DB_PATH=path.abspath(path.join(path.dirname(__file__), path.join('data', 'deduction_games.db')))
source_path=path.abspath(path.join(path.dirname(__file__), path.join('Sources', 'basic_prompts')))

if DB_PATH:
    db.init_app(app)
    with app.app_context():
        db.create_all()
        app.run(host="127.0.0.1", port=5002, debug=True)
