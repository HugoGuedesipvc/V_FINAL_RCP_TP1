from lxml import etree

def list_ordered_people(xml_list):
    all_results = []

    for xml_string in xml_list:
        try:
            root = etree.fromstring(xml_string)
            persons = root.xpath("/Data/Persons/Person")

            if not persons:
                all_results.append(None)
                continue

            sorted_persons = sorted(persons, key=lambda x: x.get("first_name"))

            result = []
            for person in sorted_persons:
                person_info = {
                    'id': person.get("id"),
                    'first_name': person.get("first_name"),
                    'last_name': person.get("last_name"),
                    'country': person.get("country"),
                    # Adicione outros campos essenciais conforme necessário
                }
                result.append(person_info)

            all_results.append(result)

        except Exception as e:
            print(f"Erro na consulta: {str(e)}")
            all_results.append(None)

    return all_results