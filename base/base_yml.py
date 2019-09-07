import yaml


def yml_data_with_file(file_name):

    with open("data/" + file_name + ".yml", 'r', encoding='UTF-8') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        return data
