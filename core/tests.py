from djangoProject.wsgi import *
from core.models import Type, EmpleadosModel

# Create your tests here.
    #Listar
# query= Type.objects.all()
# print(query)
    #Filtrar
obj = Type.objects.filter(name__contains= 'Dev')
obj2 = Type.objects.filter(name__icontains= 'pr') #Mayus y minus
obj3 = Type.objects.filter(name__startswith= 'G')
obj4 = Type.objects.filter(name__endswith= 'p')
obj5 = Type.objects.filter(name__in= ['Develop', 'Presidente'])
obj6 = Type.objects.filter(name__startswith='P').exclude(id= 5)
for i in  Type.objects.filter(name__startswith='P'):
    print(i.id)
    #Insert
t = Type()
t.name = 'Gobernador'
t.save()
    #Update
# try:
#      t = Type.objects.get(id=2)
#      t.name = 'Back-end'
#      t.save()
#      print(t.name)
# except Exception as e:
#     print(e)
#     #Delete
# t = Type.objects.get(id=2)
# t.delete()
    #Con tablas relacionadas
EmpleadosModel.objects.filter(type_id=3, data_create__day=2)
t = EmpleadosModel.objects.filter(type_id=3).query
print(t)


