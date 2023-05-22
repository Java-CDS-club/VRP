from flask import Flask, request, render_template, jsonify
import json
import vrp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        distance_matrix = json.loads(request.form['distance_matrix'])
        num_vehicles = int(request.form['num_vehicles'])
        depot = int(request.form['depot'])
        max_distance = int(request.form['max_distance'])  # Get the maximum travel distance from the form

        # Call the solve function from vrp.py
        result = vrp.solve(distance_matrix, num_vehicles, depot, max_distance)  # Pass the max_distance to solve function

        # Return the result to the user
        return render_template('result.html', result=result)

    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    distance_matrix = data.get('distance_matrix')
    num_vehicles = int(data.get('num_vehicles'))
    depot = int(data.get('depot'))
    max_distance = int(data.get('max_distance'))  # Get the maximum travel distance from the request

    # Call the solve function from vrp.py
    result = vrp.solve(distance_matrix, num_vehicles, depot, max_distance)  # Pass the max_distance to solve function

    # Return the result as JSON response
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
