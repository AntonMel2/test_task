import requests
import json

def get_list_binary_packages(branch: str):
    url = 'https://rdb.altlinux.org/api'
    response = requests.get(f"{url}/export/branch_binary_packages/{branch}")
    response_json = response.json()
    return response_json.get('packages')


list_p10 = get_list_binary_packages('p10')
list_sisyphus = get_list_binary_packages('sisyphus')

sisyphus_set = set()
for pack in list_sisyphus:
    sisyphus_set.add(pack['name'])

p10_set = set()
for pack in list_p10:
    p10_set.add(pack['name'])

dif_p10_s = list(p10_set.difference(sisyphus_set))
dif_s_p10 = list(sisyphus_set.difference(p10_set))
inter = list(p10_set.intersection(sisyphus_set))

json_dict = {}
json_dict['p10_difference_sisyphus'] = dif_p10_s
json_dict['sisyphus_difference_p10'] = dif_s_p10

with open("data_file.json", "w") as write_file:
   json.dump(json_dict, write_file)