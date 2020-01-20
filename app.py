from flask import Flask, jsonify
import requests
app = Flask(__name__)

BASE_API = 'https://www.trafficwatchni.com/twni/map/mapData'

@app.route('/roadworks.geojson')
def roadworks():
    roadwork_json_response = requests.post(
        BASE_API,
        headers={'Accept-Encoding': 'gzip'},
        data={'selectedTypes': 'ROAD_WORKS'}
    )

    if roadwork_json_response.status_code == 200:
        roadwork_json = roadwork_json_response.json()
        roadworks = roadwork_json['mapData']['ROAD_WORKS']
        features = [roadwork_to_geojson(roadwork) for roadwork in roadworks]
        response = {
            'type': 'FeatureCollection',
            'features': features
        }
        return jsonify(response)
      #  return 'Success!'
    else:
        return 'Failed'



def roadwork_to_geojson(roadwork):
    geojson = {}
    geojson['id'] = roadwork['id']
    geojson['properties'] = roadwork['details']
    geojson['geometry'] = {
        'type': 'Point',
        'coordinates': [
            roadwork['longitude'],
            roadwork['latitude']
        ]
    }
    return geojson