import json


def is_str_in_arr(s, arr):
    for item in arr:
        if item == s:
            return True
    return False


def get_categories_arr(records, categories_key):
    result = []
    for rec in records:
        val = rec[categories_key]
        if not is_str_in_arr(val,result):
            result.append(val)
    return result


def get_series(records, categories, categories_key, series_key, stack_key, value_key):
    result = []
    dict = {}
    colors = {}
    selected={}
    for rec in records:
        name = rec[series_key] + " (" + str(rec[stack_key]) + ")"
        stack = rec[stack_key]

        if name not in dict:
            dict[name] = {}
        if stack not in dict[name]:
            dict[name][stack] = [None] * len(categories)

        idx = categories.index(rec[categories_key])
        dict[name][stack][idx] = float(rec[value_key])

        colors[name] = rec["color"]
        selected[name] = rec["selected"]

    for name in dict:
        for stack in dict[name]:
            obj = {'name': name}
            obj['stack'] = stack
            obj['data'] = dict[name][stack]
            obj['color'] = colors[name]
            obj['visible'] = selected[name]
            result.append(obj)

    def foo(el):
        if el['name'].find('Total') != -1:
            if el['name'].find('2014') != -1:
                return 'Ψ'
            else:
                return 'Ω'
        else:
            return el['name']
    result = sorted(result, key=foo)

    return result


def create_stacked_and_grouped_column_chart(records, categories_key, series_key, stack_key, value_key, title_value):
    result = dict()

    result["chart"] = {}
    chart = result["chart"]
    chart["type"] = 'column'

    result["title"] = {}
    title = result["title"]
    title["text"] = title_value

    result["xAxis"] = {}
    xAxis = result["xAxis"]
    xAxis["categories"] = get_categories_arr(records, categories_key)
    categories = xAxis["categories"]

    result["yAxis"] = {}
    yAxis = result["yAxis"]
    yAxis["allowDecimals"] = False
    yAxis["min"] = 0
    yAxis["title"] = {}
    yAxis["title"]["text"] = "Number of disease cases per 100 000 population"

    result["tooltip"] = {}
    tooltip = result["tooltip"]

    result["plotOptions"] = {}
    plotOptions = result["plotOptions"]
    plotOptions["column"] = {}
    column = plotOptions["column"]
    column["stacking"] = 'normal'

    result["series"] = get_series(records, categories, categories_key, series_key, stack_key, value_key)

    result["legend"] = {}
    legend = result["legend"]
    legend["layout"] = 'horizontal'
    legend["verticalAlign"] = 'top'
    legend["align"] = 'left'
    # legend["floating"] = True
    # legend["enabled"] = False
    legend["backgroundColor"] = '#FFFFFF'
    # legend["padding"] = 8
    legend["x"] = 90
    legend["y"] = 45

    return json.dumps(result, indent=4, sort_keys=True)


def save_stack_and_grp_col_chart(file_name, records, categories_key, series_key, stack_key, value_key, title):
    f = open(file_name, "w")
    json = create_stacked_and_grouped_column_chart(records,
                                                   categories_key,
                                                   series_key,
                                                   stack_key,
                                                   value_key,
                                                   title)
    f.write("\ncallback(\n")
    f.write(json)
    f.write("\n);\n")
    f.close()
