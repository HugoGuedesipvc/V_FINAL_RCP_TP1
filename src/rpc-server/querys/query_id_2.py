from lxml import etree

def filter_sales_by_year(xml_list, year):
    all_results = []

    for xml_data in xml_list:
        try:
            root = etree.fromstring(xml_data)
            xpath_query = f"/Data/Sales/Sales[number(substring-after(@car_id, 'year_of_manufacture: ')) > {year}]"
            result = root.xpath(xpath_query)

            if not result:
                all_results.append(None)
                continue

            essential_data = []
            for elem in result:
                sale_info = {
                    'sale_id': elem.get('id'),
                    'person_info': elem.get('person_id'),
                    'car_info': elem.get('car_id'),
                    'country': elem.get('country'),
                }
                essential_data.append(sale_info)

            all_results.append(essential_data)

        except Exception as e:
            print(f"Erro na consulta: {str(e)}")
            all_results.append(None)

    return all_results
