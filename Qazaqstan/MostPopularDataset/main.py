import requests
import json
import sys
from functools import reduce

INT_MIN_VAL = -sys.maxsize - 1
DEFAULT_COUNT = 20


def make_url(page=1, count=DEFAULT_COUNT, by_gov_agencies=True, by_external_users=True, sort_by="createdDateDesc"):
    return "https://data.egov.kz/datasets/getdatasets?page={}&count={}&byGovAgencies={}&byExternalUsers={}&sortBy={}"\
        .format(str(page), str(count), str(by_gov_agencies), str(by_external_users), sort_by)


def get_dataset(url):
    res = requests.get(url)
    data_json = res.text
    data = json.loads(data_json)
    return data

    
def get_total_count():
    url = make_url(1, 1)
    data = get_dataset(url)
    return data["totalCount"]


def loop_datasets():
    total_count = get_total_count()
    passed = 0
    page_idx = 1
    max_views = INT_MIN_VAL
    dataset_with_max_views = None
    while passed != total_count:
        url = make_url(page_idx)
        data = get_dataset(url)
        views = list(map(lambda dataset: dataset["views"] if "views" in dataset else INT_MIN_VAL, data["datasets"]))
        max_value, max_index = reduce(
            lambda p1, p2: max(p1, p2),
            ((x, i) for i, x in enumerate(views))
        )
        if max_value > max_views:
            max_views = max_value
            dataset_with_max_views = data["datasets"][max_index]
        passed += len(data["datasets"])
        page_idx += 1
    return dataset_with_max_views


def get_url_of_most_popular_dataset():
    most_popular_dataset = loop_datasets()
    return "https://data.egov.kz/datasets/view?index={}".format(most_popular_dataset["apiUri"])


def create_internet_shortcut(url):
    with open("most_popular_dataset.url", "w") as internet_shortcut:
        internet_shortcut.write("[InternetShortcut]\nURL={}\n".format(url))


url = get_url_of_most_popular_dataset()
print(url)
create_internet_shortcut(url)
