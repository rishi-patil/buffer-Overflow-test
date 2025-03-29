import xmltodict
import json

input_file = "cppcheck-results.xml"
output_file = "cppcheck-results.json"

with open(input_file, "r") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())

json_output = json.dumps(data_dict, indent=4)

with open(output_file, "w") as json_file:
    json_file.write(json_output)

print("Converted cppcheck results to JSON format.")
