# Abrir biblioteca e organizar dados
f = open("sinalizacao.csv")

for line in f:
    print(line.strip().split(';'))

# Repositório criado para armazenar o código
