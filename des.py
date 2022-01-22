from cowin_api import CoWinAPI

district_id = '365'
date = '08-05-2021'  # Optional. Takes today's date by default
# Optional. By default returns centers without filtering by min_age_limit
min_age_limit = 18

cowin = CoWinAPI()
available_centers = cowin.get_availability_by_district(district_id, date,min_age_limit)
print(available_centers)
for i in available_centers['centers']:
	print("NAME"+i['name']+"  BLOCK NAME"+i['block_name']+"  PINCODE"+str(i['pincode']))
	