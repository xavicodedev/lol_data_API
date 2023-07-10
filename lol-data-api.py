from flask import Flask, jsonify
import csv

app = Flask('lol-data-api')

def get_league_data(file_name):
    data = []
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data

@app.route('/lvp', methods=['GET'])
def get_lvp_data():
    data = get_league_data('data/lvp.csv')
    return jsonify({'data': data})

@app.route('/lfl', methods=['GET'])
def get_lfl_data():
    data = get_league_data('data/lfl.csv')
    return jsonify({'data': data})

# Add more routes for each league as needed

if __name__ == '__main__':
    app.run()
