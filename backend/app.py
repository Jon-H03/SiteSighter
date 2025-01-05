from flask import Flask, request, jsonify
from services.get_locations import get_camping_data
from services.get_weather import get_city_coordinates, get_weather

app = Flask(__name__)


@app.route("/campsites", methods=["POST"])
def get_acticity_data():
    data = request.json
    city = data.get("city")

    if not city:
        return jsonify({"error": "A city or activity was not entered.\n"}), 404
    
    try:
        # Get city coordinates
        lat, lon = get_city_coordinates(city)
        if lat is None or lon is None:
            return jsonify({"error": "Could not fetch coordinates for the given city"}), 404
        
        # Fetch recreation data
        locations = get_camping_data(lat, lon)
        print(locations)
        if "error" in locations:
            return jsonify({"error": "Could not fetch locations."}), 500
        
        # Fetch weather data
        weather = get_weather(lat, lon)
        if "error" in weather:
            return jsonify({"error": "Could not fetch weather"}), 500
        
        response = {
            "city": city,
            "coordinates": {"latitude": lat, "longitude": lon},
            "locations": locations,
            "weather": weather
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

if __name__ == "__main__":
    app.run(debug=True, port=5003)

