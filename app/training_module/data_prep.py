import csv

from . import csv_location

'''
0 sentence #
1 word
2 pos
3 tag

'''
def csv_to_json():
    csv_data = __read_csv_file()
    return 'test'


def __read_csv_file():
    data = list()
    with open(csv_location, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            data.append(line)
    return data

def __convert_to_json(csv_data):
    training_data = list()
    for line in csv_data:
        pass
