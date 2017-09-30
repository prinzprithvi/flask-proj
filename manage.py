__author__ = 'prithvi'
import os
# Set the path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))

from flask_script import Manager, Server
from app import myApp
from app.views import user_apis


myApp.register_blueprint(user_apis)


manager = Manager(myApp)
# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0',port=8080)
)

#from GunicornServer import GunicornServer
#manager.add_command("rungunicorn", GunicornServer())

#import flask_sauth.commands
#flask_sauth.commands.add_commands(manager)

if __name__ == "__main__":
    manager.run()


