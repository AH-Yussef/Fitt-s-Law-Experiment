import csv
from os import write

def setup_heaedr_individual_test(max_clicks):
    header = ["test_id", "parameter"]
    i = 1
    while i < max_clicks:
        label = "click{}".format(i)
        header.append(label)
        i += 1

    with open('data/individual_tests.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)

def append_indvidual_test(test_id, index_D, movement_t, width, dist):
    index_D.insert(0, test_id)
    index_D.insert(1, "ID")
    movement_t.insert(0, test_id)
    movement_t.insert(1, "MT")
    width.insert(0, test_id)
    width.insert(1, "W")
    dist.insert(0, test_id)
    dist.insert(1, "D")
    with open('data/individual_tests.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(index_D)
        writer.writerow(movement_t)
        writer.writerow(width)
        writer.writerow(dist)

def setup_header_all_data():
    with open('data/all_data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["No.", "ID", "MT", "W", "D"])

def append_all_data(index_D, movement_t, width, dist):
    file = open("sys_settings/no_clicks.txt", "r")
    row_id = int(file.readline())
    file.close()

    with open('data/all_data.csv', 'a') as file:
        writer = csv.writer(file)
        for i in range(len(index_D)):
            row = [row_id, index_D[i], movement_t[i], width[i], dist[i]]
            writer.writerow(row)
            row_id += 1
    
    file = open("sys_settings/no_clicks.txt", "w")
    file.write(str(row_id))
    file.close()
