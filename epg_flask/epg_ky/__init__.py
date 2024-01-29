from flask import Flask
from epg_ky.db_utils import connection_pool_instance

app = Flask(__name__)

# Import your routes after initializing the app
from epg_ky import program_routes, channel_routes

app.register_blueprint(program_routes.programs_bp, url_prefix='/programs')
app.register_blueprint(channel_routes.channels_bp, url_prefix='/channels')
