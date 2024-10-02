#!/usr/bin/env python3

import json
import csv
def convert_csv_to_json(csv_file):
    try: 
        data = []
        with open(csv_file, 'r') as fric:
            csv_reader = csv.DictReader(fric)
            for row in csv_reader:
                data.append(row)

        with open("data.json", 'w') as fric:
            json.dump(data, fric, indent= 4)
            return True
    except FileNotFoundError:
        return False