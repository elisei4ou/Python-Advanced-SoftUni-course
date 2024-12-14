import os

dict_files = {}


def directory_traversal(directory_name, is_first_level=False):
    all_files = os.listdir(directory_name)

    for every_file in all_files:

        if "." in every_file:
            extension = every_file.split(".")[-1]

            if extension not in dict_files.keys():
                dict_files[extension] = []
            dict_files[extension].append(every_file)

        if "." not in every_file and is_first_level is False:
            directory_name = os.path.join(directory_name, every_file)
            directory_traversal(directory_name, is_first_level=True)

    return dict_files


directory = input()
ABSOLUTE_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ABSOLUTE_DIR_PATH, directory)
path_1 = os.path.join(path, "report.txt")
returned_dict = directory_traversal(path)

sorted_dict = sorted(returned_dict.items(), key=lambda x: x[0])

with open(path_1, "w") as file:
    result = ""

    for ext, files in sorted_dict:
        result += f".{ext}\n"

        for f in sorted(files):
            result += f"- - - {f}\n"

    file.write(result)

