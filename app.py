import sys
import os
from flask import send_from_directory

if not os.path.exists("config.py"):
    print("Configuration 'config.py.py' not found.  "
          "You may create one from 'config.py.py.example'.")
    sys.exit(1)

from config import OPENAPI_STUB_DIR

if not os.path.exists(OPENAPI_STUB_DIR):
    print(f"Folder '{OPENAPI_STUB_DIR}' not found.  "
          "Please create the folder and extract zip file "
          "generated by openapi-generator into it.")
    sys.exit(1)

sys.path.append(OPENAPI_STUB_DIR)

try:
    import connexion
except ModuleNotFoundError:
    print("Please install all required packages by running:"
          " pip install -r requirements.txt")
    sys.exit(1)

from swagger_server import encoder

def main():
    # Create the Connexion app
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder

    # Serve index.html
    @app.app.route('/')
    def index():
        return send_from_directory('.', 'index.html')  # Make sure index.html is in the same folder as app.py

    # Serve assets (CSS, JS, images, etc.)
    @app.app.route('/assets/<path:path>')
    def send_assets(path):
        return send_from_directory('assets', path)

    # Register your OpenAPI YAML here
    app.add_api('sound-api.yaml',  # 👈 your new YAML file
                arguments={'title': 'Air Quality Monitoring API'},
                pythonic_params=True)

    app.run(port=8080, debug=True)

if __name__ == '__main__':
    main()
