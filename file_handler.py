import json

def write_file(in_list, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for e in in_list:
            f.write(f"{e}\n")
        print(f"File {filename} written")


def read_file(filename):
    temp_list = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                element = line.strip()
                if not element:
                    continue
# fant ikke noen penere måte å sikre samme datatype tilbake på
                try:
                    temp_list.append(int(element))
                except ValueError:
                    try:
                        temp_list.append(float(element))
                    except ValueError:
                        temp_list.append(element)

        return temp_list
    except FileNotFoundError:
        print(f"File {filename} not found")


def write_json(in_dict, filename):
    if isinstance(in_dict, dict):
        with open(filename, "w", encoding="utf-8") as f: # f"{filename}.json" hvis man vil slippe å skrive filtype hver gang? x)
            json.dump(in_dict, f, indent=4)
            print(f"File {filename} written")
    else:
        print(f"Input is not a dictionary")

def read_json(filename):
    out_dict = json.load(open(filename, "r", encoding="utf-8"))
    return out_dict