from lxml import etree

def search_cars(xml_list, brand, model, color):
    all_results = []

    for xml_data in xml_list:
        try:
            root = etree.fromstring(xml_data)
            query = f"/Data/Sales/Sales[contains(@car_id, 'brand: {brand}') and contains(@car_id, 'model: {model}') and contains(@car_id, 'color: {color}')]"
            results = root.xpath(query)

            if not results:
                all_results.append(None)
                continue

            essential_data = []
            for result in results:
                sale_info = {
                    'sale_id': result.get('id'),
                    'person_info': result.get('person_id'),
                    'car_info': result.get('car_id'),
                    # Adicione outros campos essenciais conforme necessário
                }
                essential_data.append(sale_info)

            all_results.append(essential_data)

        except Exception as e:
            print(f"Erro na consulta: {str(e)}")
            all_results.append(None)

    return all_results
