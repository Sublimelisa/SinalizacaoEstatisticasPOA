class Signs:
  def __init__(self, id, tipo, descricao, latitude, longitude, data):
    self.id = id
    self.tipo = tipo
    self.descricao = descricao
    self.latitude = latitude
    self.longitude = longitude
    self.data = data
  
# Open library to read csv file
f = open("sinalizacao.csv")


antiga = ''
primeira = True
ausentes = []
for line in f:
  if primeira:
    primeira = False
    continue
  lista = line.strip().split(';')
  if len(lista) > 4:  
    # Check if list has at least 5 elements (index 4)
    if antiga == '' or antiga > lista[4]:
      antiga = lista[4]
  if len(lista) > 14 and (lista[13].strip() == '' or lista[14].strip() == ''):
      # Your logic here
    ausentes.append(lista)
  else:
    print(lista)
    
# Show data

print(antiga)
print(ausentes)



