import csv

from . import csv_location

def csv_to_spacy() -> (list, list):
    csv_data = __read_csv_file()
    spacy_data, labels = __convert_to_spacy(csv_data)
    return spacy_data, labels

def __read_csv_file() -> list:
    data = list()
    with open(csv_location, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            data.append(line)
    return data[1:]

def __convert_to_spacy(csv_data: list) -> (list, list):
    '''
    csv column ref
    0 sentence #
    1 word
    2 pos
    3 tag
    '''
    training_data = list()
    labels = set()

    line = list()
    entities = list()
    current_index = 0
    for data in csv_data:
        if data[0] and len(line) > 0:
            data_entry = (' '.join(line), { "entities": entities })
            training_data.append(data_entry)
            line = list()
            entities = list()
            current_index = 0
        line.append(data[1])
        if data[3] != 'O':
            entity = (
                current_index, 
                current_index+len(data[1]), 
                data[3])
            entities.append(entity)
            labels.add(data[3])
        current_index += (len(data[1])+1)
    return training_data, labels
        
        
        
        
