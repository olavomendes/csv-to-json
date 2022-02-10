import csv
import json


def csv2json(csv_filepath):
    csv_file = open(csv_filepath, 'r', errors="ignore")
    json_file = open(r'resultado.json', 'w')

    # caso necessário, mude o DELIMITER para ";"
    reader = csv.DictReader(csv_file, delimiter=",")
    archive = json.dumps([row for row in reader], ensure_ascii=False)
    json_file.write(archive)


csv2json(r'obligation_template.csv')
