import csv
import numpy as np

item_to_index = {}
item_index_to_property = {}
property_list = set()   # 157 many unique properties

with open('../Dataset/item_metadata.csv', 'r') as f:
    reader = csv.reader(f)
    reader.__next__()
    index = 0
    for line in reader:
        item_to_index[line[0]] = index
        item_index_to_property[index] = line[1].split('|')

        if len(property_list):
            property_list.update(set(item_index_to_property[index]))
        else:
            property_list = set(item_index_to_property[index])
                
        index += 1

    