import xml.etree.ElementTree as ET

def filter_sales_by_country(xml_list, country):
    all_results = []

    for xml_data in xml_list:
        try:
            root = ET.fromstring(xml_data)
            xpath_query = f"./Sales[@country='{country}']"  # Alteração aqui
            sales_elements = root.findall(xpath_query)

            if not sales_elements:
                all_results.append(None)
                continue

            filtered_results = []
            for sales_elem in sales_elements:
                # Extrair informações essenciais
                person_info = sales_elem.get('person_id')
                car_info = sales_elem.get('car_id')
                credit_card_info = sales_elem.get('credit_card_id')

                essential_data = {
                    'person_info': person_info,
                    'car_info': car_info,
                    'credit_card_info': credit_card_info,
                }
                filtered_results.append(essential_data)

            all_results.append(filtered_results)

        except Exception as e:
            print(f"Erro na consulta: {type(e).__name__} - {str(e)}")
            all_results.append(None)

    return all_results
