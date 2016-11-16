import lib
import highcharts
import json

translate = dict()
translate["Южно-Казахстанская"] = "South Kazakhstan Region"  # https://en.wikipedia.org/wiki/South_Kazakhstan_Region
translate["Атырауская"] = "Atyrau Region"  # https://en.wikipedia.org/wiki/Atyrau_Region
translate["Актюбинская"] = "Aktobe Region"  # https://en.wikipedia.org/wiki/Aktobe_Region
translate["г. Алматы"] = "Almaty"  # https://en.wikipedia.org/wiki/Almaty
translate["Республика Казахстан"] = "Kazakhstan"   # https://en.wikipedia.org/wiki/Kazakhstan
translate["Восточно-Казахстанская"] = "East Kazakhstan Region"  # https://en.wikipedia.org/wiki/East_Kazakhstan_Region
translate["Кызылординская"] = "Kyzylorda Region"  # https://en.wikipedia.org/wiki/Kyzylorda_Region
translate["Мангыстауская"] = "Mangystau Region"  # https://en.wikipedia.org/wiki/Mangystau_Region
translate["Западно-Казахстанская"] = "West Kazakhstan Region"  # https://en.wikipedia.org/wiki/West_Kazakhstan_Region
translate["Северо-Казахстанская"] = "North Kazakhstan Region"  # https://en.wikipedia.org/wiki/North_Kazakhstan_Region
translate["Акмолинская"] = "Akmola Region"  # https://en.wikipedia.org/wiki/Akmola_Region
translate["Жамбылская"] = "Jambyl Region"  # https://en.wikipedia.org/wiki/Jambyl_Region
translate["Карагандинская"] = "Karaganda Region"  # https://en.wikipedia.org/wiki/Karaganda_Region
translate["Костанайская"] = "Kostanay Region"  # https://en.wikipedia.org/wiki/Kostanay_Region
translate["Павлодарская"] = "Pavlodar Region"  # https://en.wikipedia.org/wiki/Pavlodar_Region
translate["г. Астана"] = "Astana"  # https://en.wikipedia.org/wiki/Astana
translate["Алматинская"] = "Almaty Region"  # https://en.wikipedia.org/wiki/Almaty_Region


mapping = dict()

mapping["Наименование областей"] = {'dimensions': ['region']}

# COLORS: http://stackoverflow.com/a/4382138

# https://en.wikipedia.org/wiki/ICD-10_Chapter_XIII:_Diseases_of_the_musculoskeletal_system_and_connective_tissue
mapping["Болезни костно-мышечной системы и соединительной ткани 2014 год    "] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Diseases of the musculoskeletal system and connective tissue', 'color': '#FFB300', 'selected': True}
mapping["Болезни костно-мышечной системы и соединительной ткани 2015 год    "] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Diseases of the musculoskeletal system and connective tissue', 'color': '#FFB300', 'selected': True}

# http://www.multitran.ru/c/m.exe?l1=1&l2=2&s=diseases%20of%20the%20circulatory%20system
mapping["Болезни системы кровообращения  2014 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Diseases of the circulatory system', 'color': '#803E75', 'selected': True}
mapping["Болезни системы кровообращения  2015 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Diseases of the circulatory system', 'color': '#803E75', 'selected': True}

# http://www.multitran.ru/c/m.exe?l1=1&l2=2&s=essential%20hypertension
mapping["  Гипертоническая болезнь 2014 год "] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Essential hypertension', 'color': '#FF6800', 'selected': True}
mapping["  Гипертоническая болезнь 2015 год "] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Essential hypertension', 'color': '#FF6800', 'selected': True}

# http://www.multitran.ru/c/m.exe?l1=1&l2=2&s=malignant%20neoplasms
mapping["Злокачественные новообразования  2014 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Malignant neoplasms', 'color': '#A6BDD7', 'selected': True}
mapping["Злокачественные новообразования  2015 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Malignant neoplasms', 'color': '#A6BDD7', 'selected': True}

# https://en.wikipedia.org/wiki/Myocardial_infarction
mapping["инфаркт миокарда 2014 год "] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Myocardial infarction', 'color': '#C10020', 'selected': False}
mapping["инфаркт миокарда 2015 год "] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Myocardial infarction', 'color': '#C10020', 'selected': False}

# https://en.wikipedia.org/wiki/Ischemia#Cardiac_ischemia
# http://www.multitran.ru/c/m.exe?l1=1&l2=2&s=Cardiac%20ischemia
mapping["Ишемическая болезнь сердца 2014  год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Cardiac ischemia', 'color': '#CEA262', 'selected': True}
mapping["Ишемическая болезнь сердца 2015  год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Cardiac ischemia', 'color': '#CEA262', 'selected': True}

# http://www.multitran.ru/c/m.exe?l1=1&l2=2&s=mental%20and%20behavioural%20disorders
mapping["Психические расстройства и расстройства поведения  2014  год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Mental and behavioural disorders', 'color': '#817066', 'selected': False}
mapping["Психические расстройства и расстройства поведения  2015  год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Mental and behavioural disorders', 'color': '#817066', 'selected': False}

# http://www.samhsa.gov/disorders
mapping["Психические расстройства и расстройства, связанные с употреблением психоактивных веществ  2014 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Mental and substance use disorders', 'color': '#007D34', 'selected': False}
mapping["Психические расстройства и расстройства, связанные с употреблением психоактивных веществ  2015 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Mental and substance use disorders', 'color': '#007D34', 'selected': False}

# https://en.wikipedia.org/wiki/Diabetes_mellitus
mapping["Сахарный диабет 2014 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Diabetes mellitus', 'color': '#F6768E', 'selected': True}
mapping["Сахарный диабет 2015 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Diabetes mellitus', 'color': '#F6768E', 'selected': True}

# https://en.wikipedia.org/wiki/Syphilis
mapping["Сифилис 2014 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Syphilis', 'color': '#00538A', 'selected': False}
mapping["Сифилис 2015 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Syphilis', 'color': '#00538A', 'selected': False}

# https://en.wikipedia.org/wiki/List_of_ICD-9_codes_800%E2%80%93999:_injury_and_poisoning
mapping["Травмы и отравления 2014 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Injury and poisoning', 'color': '#FF7A5C', 'selected': True}
mapping["Травмы и отравления 2015 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Injury and poisoning', 'color': '#FF7A5C', 'selected': True}

# https://en.wikipedia.org/wiki/Tuberculosis
mapping["Туберкулез  2015 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Tuberculosis', 'color': '#53377A', 'selected': False}

mapping["Всего заболеваний 2014 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Total', 'color': '#FF8E00', 'selected': False}
mapping["Всего заболеваний 2015 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2015, 'scope': 'Total', 'color': '#FF8E00', 'selected': False}

# https://en.wikipedia.org/wiki/Anemia
mapping["Анемии  2014 год"] = {'dimensions': ['scope', 'year', 'value'], 'year': 2014, 'scope': 'Anemia', 'color': '#B32851', 'selected': True}
duplicatedColumns = ['Анемии 2014 год']

key2map = {}


def check_and_enrich_mapping(url):
    metadata = lib.get_json_as_dict_by_url(url)
    for fieldKey in metadata["fields"]:
        field = metadata["fields"][fieldKey]
        labelRu = field["labelRu"]
        m = mapping[labelRu]
        key2map[fieldKey] = m


def process_records(cnt_url, info_url):
    result = []
    total_count = lib.get_total_num_of_records_in_dataset(cnt_url)
    records = lib.get_records_from_dataset(total_count, info_url)
    for rec in records:
        region = rec["region"]
        for field_key in rec:
            m = key2map[field_key]

            if any("region" in d for d in m['dimensions']):
                continue

            if m["scope"] == "Anemia":  # FIX THIS: duplicated columns
                continue

            new_obj = {'region': translate[region], 'color': m['color'], 'selected': m['selected']}
            for d in m['dimensions']:
                if d in m:
                    new_obj[d] = m[d]
                else:
                    new_obj[d] = rec[field_key]
            result.append(new_obj)

    def foo(el):
        if el['region'] == 'Kazakhstan':
            return '1'
        elif el['region'] == 'Astana':
            return '2'
        elif el['region'] == 'Almaty':
            return '3'
        else:
            return el['region']

    result = sorted(result, key=foo)

    # print(json.dumps(result, indent=4, sort_keys=True))
    return result

check_and_enrich_mapping('https://data.egov.kz/meta/turleri_onirler_men_zhyldar_b/v2?pretty')
new_records = process_records("turleri_onirler_men_zhyldar_b/v2", "v2/turleri_onirler_men_zhyldar_b/v2")
highcharts.save_stack_and_grp_col_chart('disease-statistics-by-year-and-by-region.js',
                                        new_records,
                                        'region',
                                        'scope',
                                        'year',
                                        'value',
                                        'Disease Statistics by Year 2014-2015 and by Region for Kazakhstan')
