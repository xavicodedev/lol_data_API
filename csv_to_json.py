from flask import Flask, jsonify
import csv

app = Flask('my_app')

file = "data/lvp.csv"

def convert_csv_to_json(file_name):
    data = []
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            formatted_row = {f'"{key}"': value for key, value in row.items()}
            data.append(formatted_row)
            print(data)
    return jsonify(data)

convert_csv_to_json(file)
