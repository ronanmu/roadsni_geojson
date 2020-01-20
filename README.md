## Introduction

This simple python app repackages data the Traffic Watch NI [website](https://www.trafficwatchni.com/) into GeoJSON for use in alternative applications.
The application currently supports:
- Road Works

*Services for Incidents and Events tbc*

### Pre-requesites

This application makes use of 
- Requests - for interacting with the 3rd party API
- Flask - for serving the API endpoints

### Usage
Run as a simple Flask application by:
```commandline
flask run
```
You can then interogate the endpoint at:
```text
GET http://127.0.0.1:5000/roadworks.geojson
```
and receive a response like
```json
{
  "type": "FeatureCollection",
  "features": [{
    "geometry": {
      "coordinates": [
        -6.012369840417875,
        54.57660758448544
      ],
      "type": "Point"
    },
    "id": "19183839",
    "properties": {
      "delays": "Up to 5 minutes",
      "description": "<p>Closed daily for&nbsp;resurfacing carriageway.</p> <p><br /> Alternative route:&nbsp;Glen Road - Monagh By Pass - Andersontown Road - Shaws Road<br /> &nbsp;</p> ",
      "end": "Mon, 20 Jan 2020 16:30 GMT",
      "location": "Shaws Road, Belfast - Belfast",
      "locationSummary": "From Glen Road to Number 95",
      "severity": "Low",
      "start": "Tue, 14 Jan 2020 09:30 GMT",
      "workCarriedOutBy": "Private contractor"
    }
  },
  {
    // More entries here
  }]
}
```


## Usage in Home Assistant
This app can be used as a source of data for Geo Events in [Home Assistant](https://home-assistant.io) (which wsa the original reason for writing this app).
You can add this entry to your Home Assistant configuration:

```yaml
# Example configuration.yaml entry
geo_location:
  - platform: geo_json_events
    url: http://127.0.0.1:5000/roadworks.geojson # or wherever this app is running
    entity_namespace: trafficwatchni_roadworks
```
 


Copyright (c) 2020 Ronan Murray.