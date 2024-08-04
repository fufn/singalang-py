import datetime

import azapi
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/lyrics', methods=['GET'])
def get_lyrics():
    print('Starting search' + datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
    artist = request.args.get('artist')
    title = request.args.get('title')
    API = azapi.AZlyrics()
    API.artist = artist
    API.title = title
    return API.getLyrics(save=False)

if __name__ == '__main__':
    app.run(debug=True)
