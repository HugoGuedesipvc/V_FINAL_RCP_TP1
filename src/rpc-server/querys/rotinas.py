import os

from querys.query_id_1 import filter_sales_by_country
from querys.query_id_2 import filter_sales_by_year
from querys.query_id_3 import search_cars
from querys.query_id_4 import list_ordered_people
from querys.query_id_5 import filter_cars_by_brand

RESULTS_FILE_PATH = "/src/rpc-base_dados/data"

def save_results_to_file(results, filename):
    full_path = os.path.join(RESULTS_FILE_PATH, filename)

    try:
        with open(full_path, 'w') as file:
            for result in results:
                file.write(result + '\n')
        print(f"Dados salvos com sucesso no arquivo: {full_path}")
    except Exception as e:
        print(f"Erro ao salvar dados no arquivo: {str(e)}")

def run_query(xml_data, query_id):
    results = []

    if query_id == 1:
        country = "Portugal"
        results.extend(filter_sales_by_country(xml_data, country))
    elif query_id == 2:
        year = "1999"
        results.extend(filter_sales_by_year(xml_data, year))
    elif query_id == 3:
        brand = "Audi"
        model = "A4"
        color = "Grey"
        results.extend(search_cars(xml_data, brand, model, color))
    elif query_id == 4:
        results.extend(list_ordered_people(xml_data))
    elif query_id == 5:
        brand = "Audi"
        results.extend(filter_cars_by_brand(xml_data, brand))

    return results


def execute_queries(list_xml, query_id):
    results = []

    for xml_data in list_xml:
        results.extend(run_query(xml_data, query_id))

    save_results_to_file(results, f"resultados_query_{query_id}.txt")
