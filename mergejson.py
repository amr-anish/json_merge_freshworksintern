import json
import os
import jsonmerge as js
#setting the scheme to append and overwrite with existing json
schema = {'mergeStrategy': 'objectMerge',
                  'properties': {
                      'b': {'mergeStrategy': 'overwrite'}
                  },
                  'additionalProperties': {
                      'mergeStrategy': 'append'
                  }}

base = None
base = js.merge(base, {'a': ["a"]}, schema)
base = js.merge(base, {'a': ["b"], 'b': 'c'}, schema)

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
#To Get folder Path
folder_name=str(input("Folder Path :  [ Example : jsonfiles/ ] : "))
print("Rules : Enter the required json ID one by one and click enter Type M to Merge the json ")

#Getting the value one by one
while(True):
    j_id=str(input(" Enter the json Data ID [eg: 1 or 2] or type  m to merge: "))#press M to merge
    if(j_id=="m"or j_id=="M"):
        break
    my_file = os.path.join(THIS_FOLDER, folder_name+'data'+j_id+'.json' )
    if(int(j_id)==1):
        with open(my_file) as json_file:
             a = json.load(json_file)
    else:
        with open(my_file) as json_file:
            b = json.load(json_file)
            a = js.merge(b, a, schema) 



print(a)
#creating output json file 
print("Output file also created see in the root folder ")
with open('output.json', 'w') as f:
  json.dump(a, f, ensure_ascii=False)
