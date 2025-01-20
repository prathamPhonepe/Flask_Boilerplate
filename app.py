import sys
import os
from flask import Flask
from routes.routes import init_routes 
from flask_cors import CORS
from config.constants import constants

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
CORS(app)

app.register_blueprint(init_routes(), url_prefix='/api/v1')

if __name__ == "__main__":
    print(f"Application is running in {constants['TYPE']} mode on port {constants['APPLICATION_PORT']}.")
    app.run(debug=True, port=constants['APPLICATION_PORT'] ,threaded=True)

