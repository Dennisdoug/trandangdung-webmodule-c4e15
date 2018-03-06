import mlab
from models.service import Service

mlab.connect()

# all_services = Service.objects()
#
# first_service = all_services[0]
#
# print(first_service.name)

# #Read
# id_to_find = "5a955da4d0fb5d27c8360c04"
# Hera = Service.objects.get(id=id_to_find)

# print(Hera.to_mongo())

# #Delete
# Hera.delete()

#Update
id_to_find = "5a9563afd0fb5d0cbc4faa66"
service = Service.objects().with_id(id_to_find)

print(service.to_mongo())

if service is not None:
    # service.delete()
    service.update(set__status=True)
    service.reload()
    print(service.to_mongo())
else:
    print("Not found")
