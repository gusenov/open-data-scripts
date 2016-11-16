import requests
import json


def get_json_as_dict_by_url(url):
    res = requests.get(url)
    data_json = res.text
    data = json.loads(data_json)
    return data


def get_total_num_of_records_in_dataset(key_and_version):
    dict = get_json_as_dict_by_url("https://data.egov.kz/api/detailed/{}".format(key_and_version))
    return dict["totalCount"]


def get_records_from_dataset(num, part_of_url):
    url = 'https://data.egov.kz/api/' + part_of_url + '?source={"size":' + str(num) + ',"query": {"match_all":{}}}'
    data = get_json_as_dict_by_url(url)
    return data
