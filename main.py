from flask import Flask, jsonify
import csv

app = Flask('my_app')



@app.route('/lvp', methods=['GET'])
def get_lvp_data():
    data = []
    with open("data/lvp.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            formatted_row = {f'{key}': value for key, value in row.items()}
            data.append(formatted_row)
    return data


@app.route('/lfl', methods=['GET'])
def get_lfl_data():
    data = []
    with open("data/lfl.csv", 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            formatted_row = {f'{key}': value for key, value in row.items()}
            data.append(formatted_row)
    return data


# Add more routes for each league as needed

if __name__ == '__main__':
    app.run()
