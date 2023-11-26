import xml.etree.ElementTree as ET

def filter_cars_by_brand(xml_list, brand):
    try:
        total_count = 0

        for xml_data in xml_list:
            root = ET.fromstring(xml_data)
            xpath_query = f"count(/Data/Cars/Car[@brand='{brand}'])"
            count_result = root.xpath(xpath_query)

            count = int(count_result[0]) if count_result else 0
            total_count += count

        if total_count == 0:
            return None

        return f"({brand}):({total_count})"

    except Exception as e:
        return str(e)