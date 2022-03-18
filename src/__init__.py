# __init__.py

import os
from flask import Flask


# This is mainly for creating an absolute path to the running file
# with the inline 'if-else' exception incase it's imported from the pyshell.
app_root = os.path.dirname(os.path.abspath('.' if not '__file__' in locals() else __file__))
template_folder = os.path.join(app_root, 'templates')

# Create an instance of the Flask class
app = Flask(__name__)

# Add the route blueprints for main data handling.
from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

app.run(
    host='127.0.0.1',
    port=5000
)
