from flask import Flask
from flask_script import Manager, Server

app = Flask(__name__)
manager = Manager(app)

class CustomServer(Server):
    def __call__(self, app, *args, **kwargs):
        return Server.__call__(self, app, *args, **kwargs)

manager.add_command (
    "runserver",
    CustomServer(host = "0.0.0.0", use_reloader = False)
)

from ecg.database.ui import views
