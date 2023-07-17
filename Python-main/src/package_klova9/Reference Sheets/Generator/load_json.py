import json
from json2table import convert
with open('Python-main\Reference Sheets\content.json') as fn:
    dt = json.load(fn)
    page =json.load(dt['pages'])
    
    json_object = {"key" : "value"}
    build_direction = "LEFT_TO_RIGHT"
    table_attributes = {"style" : "width:100%"}
    html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
    print(html)