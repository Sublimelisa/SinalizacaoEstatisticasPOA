class Signs:
  pass

# Abrir biblioteca e organizar dados
f = open("sinalizacao.csv")


antiga = ''
primeira = True
ausentes = []
for line in f:
  if primeira:
    primeira = False
    continue
  lista = line.strip().split(';')
  if antiga == '' or antiga > lista[4]:
    antiga = lista[4]
  if len(lista) > 14 and (lista[13].strip() == '' or lista[14].strip() == ''):
      # Your logic here
    ausentes.append(lista)
  else:
    print(lista)
    
# Mostrar dados

print(antiga)
print(ausentes)

# Repositório criado para armazenar o código

