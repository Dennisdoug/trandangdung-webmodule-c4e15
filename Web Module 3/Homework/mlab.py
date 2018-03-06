import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds161336.mlab.com:61336/dungdeptrai

host = "ds161336.mlab.com"

port = 61336

db_name = "dungdeptrai"

user_name = "dungdeptrai"

password = "gagaga1995"


def connect():

    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):

    import json

    return [json.loads(item.to_json()) for item in l]

def item2json(item):

    import json

    return json.loads(item.to_json())
