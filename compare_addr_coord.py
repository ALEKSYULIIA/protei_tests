from function_geocode_address import get_location_info_addr
from function_geocode_coord import get_location_info_coord

result_1 = get_location_info_addr('Россия, Санкт-Петербург, Ипподромный переулок, 1 к1')
result_2 = get_location_info_coord(60.0007332, 30.3092082)

# Compare lat and lon from both results
coord_equal = (result_1.get('lat') == result_2.get('lat')) and (result_1.get('lon') == result_2.get('lon'))
# Compare address with display_name
address_equal = (result_1.get('address') == result_2.get('display_name'))

if coord_equal and address_equal:
        print("Results are the same")
else:
        print("Results are different")
        print("Address result:", result_1)
        print("Coord result:", result_2)

