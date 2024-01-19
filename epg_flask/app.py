from flask import Flask, jsonify, request, g
# from db_utils import init_app, get_db

app = Flask(__name__)



app.config['DATABASE'] = {
    'pool_size': 5,
    'connection_args': {
        'host': 'localhost',
        'port':'3308',
        'user':'munavar',
        'password': 'Munavar2@23',
        'database': 'epg_schema'
    }
}

# Data structure to store channels (in-memory list for simplicity)
channels = []


# Model for Channel
class Channel:
    def __init__(self, channel_id, name, description):
        self.channel_id = channel_id
        self.name = name
        self.description = description


# Routes for Channel Management
@app.route('/channels', methods=['GET'])
def get_all_channels():
    return jsonify([vars(channel) for channel in channels])


@app.route('/channels/<int:channel_id>', methods=['GET'])
def get_channel(channel_id):
    channel = next((channel for channel in channels if channel.channel_id == channel_id), None)
    if channel:
        return jsonify(vars(channel))
    else:
        return jsonify({"error": "Channel not found"}), 404


@app.route('/channels', methods=['POST'])
def create_channel():
    data = request.json
    new_channel = Channel(channel_id=len(channels) + 1, name=data['name'], description=data['description'])
    channels.append(new_channel)
    return jsonify(vars(new_channel)), 201


@app.route('/channels/<int:channel_id>', methods=['PUT'])
def update_channel(channel_id):
    channel = next((channel for channel in channels if channel.channel_id == channel_id), None)
    if channel:
        data = request.json
        channel.name = data['name']
        channel.description = data['description']
        return jsonify(vars(channel))
    else:
        return jsonify({"error": "Channel not found"}), 404


@app.route('/channels/<int:channel_id>', methods=['DELETE'])
def delete_channel(channel_id):
    global channels
    channels = [channel for channel in channels if channel.channel_id != channel_id]
    return jsonify({"message": "Channel deleted"}), 200


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
