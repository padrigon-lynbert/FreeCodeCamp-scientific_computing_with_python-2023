import json

data = '''{
    "Name" : "Lynbert", 
    "phone" {
     "type" : "intl",
     "number" : "+1 734 303 4456"
    },
    "email" : {
     "hide" : "yes"
    }
}'''

info = json.loads(data)
print('name:', info["Name"])