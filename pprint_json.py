import json
import sys


def load_data(filepath):
    file = open(filepath, "r", encoding='utf-8')
    print("opened")
    data = file.read()
    print("readed")
    file.close()
    print("closed")
    return data
    


def pretty_print_json(data):
    print(json.dumps(data,sort_keys=True, indent=4))


if __name__ == '__main__':
    if len (sys.argv) == 1:
        print ("Error: expected path to json-file")
    else:
        file_name = sys.argv[1]
        pretty_print_json(load_data(file_name))

