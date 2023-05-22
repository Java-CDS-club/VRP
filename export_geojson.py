import geojson

# Convert the string coordinates to tuples of floats
locations = [(float(coord.split(',')[0]), float(coord.split(',')[1])) for coord in [
    '11.16953,-4.28875',  # depot 0
    '11.16953,-3.99572',  #1
    '11.23405,-4.04314',  #2
    '11.27924,-3.98677',  #3
    '11.30249,-3.88924',  #4
    '11.33408,-3.91161',  #5
]]

# Extract the vehicle solution
solution = [
    {'vehicle': 0, 'route': [0, 3, 4, 5, 2, 0], 'distance': 107792},
    {'vehicle': 1, 'route': [0, 1, 0], 'distance': 65207},
]

# Create a GeoJSON FeatureCollection to store the locations
features = []
for idx, location in enumerate(locations):
    feature = geojson.Feature(
        geometry=geojson.Point(location),
        properties={"id": idx}
    )
    features.append(feature)
feature_collection = geojson.FeatureCollection(features)

# Export the locations as GeoJSON
with open("locations.geojson", "w") as file:
    geojson.dump(feature_collection, file)

# Create a GeoJSON FeatureCollection to store the routes
features = []
for vehicle_solution in solution:
    route = vehicle_solution['route']
    coordinates = [locations[idx] for idx in route]
    linestring = geojson.LineString(coordinates)
    feature = geojson.Feature(
        geometry=linestring,
        properties={"vehicle": vehicle_solution['vehicle'], "distance": vehicle_solution['distance']}
    )
    features.append(feature)
feature_collection = geojson.FeatureCollection(features)

# Export the routes as GeoJSON
with open("routes.geojson", "w") as file:
    geojson.dump(feature_collection, file)
