import requests
import json
import sys
from functools import reduce


def ds_catalog_url(page=1, count=20, by_gov_agencies=True, by_external_users=True, sort_by="createdDateDesc"):
    return "https://data.egov.kz/datasets/getdatasets?page={}&count={}&byGovAgencies={}&byExternalUsers={}&sortBy={}"\
        .format(str(page), str(count), str(by_gov_agencies), str(by_external_users), sort_by)


def dl_json_data(url):
    result = requests.get(url)
    json_str = result.text
    data_dict = json.loads(json_str)
    return data_dict


def ds_rec_total_cnt():
    first_record_url = ds_catalog_url(1, 1)
    data = dl_json_data(first_record_url)
    return data["totalCount"]


def merge_pages():
    page_idx = 1
    rec_idx = 0
    rec_cnt = ds_rec_total_cnt()
    all_ds = []
    while rec_idx != rec_cnt:
        page_url = ds_catalog_url(page_idx)
        page = dl_json_data(page_url)
        all_ds += page["datasets"]
        # print(json.dumps(page, indent=4, sort_keys=True))
        # break
        rec_idx += len(page["datasets"])
        page_idx += 1
    return all_ds


def sort_by_views(ds):
    if 'views' in ds:
        return ds['views']
    else:
        return -sys.maxsize - 1


def main():
    all_ds = merge_pages()
    all_ds_sorted = sorted(all_ds, key=sort_by_views)
    with open("all_ds_sorted.html", "w") as html_file:
        html_file.write('<table cellpadding="4" align="center">\n')
        for ds in all_ds_sorted:
            # print(json.dumps(ds, indent=4, sort_keys=True))
            html_file.write('\t<tr>\n')
            html_file.write('\t\t<td width="512">\n')
            html_file.write('\t\t\t<a href=https://data.egov.kz/datasets/view?index={}>{}</a>\n'
                            .format(ds["apiUri"], ds["nameRu"]))
            html_file.write('\t\t</td>\n')
            html_file.write('\t\t<td width="32" align="right">{}</td>'.format(ds["views"] if 'views' in ds else 'None'))
            html_file.write('\t</tr>\n')
        html_file.write('<table>\n')


if __name__ == "__main__":
    main()
