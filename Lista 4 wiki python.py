""
#Exercício 1:

lista = []
for i in range (5):
    num = float(input(f'Digite o {i+1}º número: '))
    lista.append(num)

print(lista)


""

#Exercício 2:

lista = []
for i in range (5):
    num = float(input(f'Digite o {i+1}º número: '))
    lista.append(num)

print('Sequência invertida: ', lista[:: -1])


""

#Exercício 3:

lista = []
for i in range (5):
    num = float(input(f'Digite a {i+1}º nota: '))
    lista.append(num)

print(sum(lista)/len(lista))

""

#Exercício 4:

listaConsoantes = ['q','w','r','t','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
lista = []
cont = 0

for i in range (10):
    caractere = str(input(f'Digite o {i+1} caractere: '))
    if caractere in listaConsoantes:
        cont += 1
        lista.append(caractere)

print(lista, cont, ' Consoantes')


""

#Exercício 5:

lista = []
listaPar = []
listaImpar = []

for i in range (20):

    num = int(input(f'Digite o {i+1}º número: '))
    lista.append(num)

    if num % 2 == 0:

        listaPar.append(num)

    elif num % 2 == 1:

        listaImpar.append(num)

print(f'Lista: {lista}\nLista impar: {listaImpar}\nLista par: {listaPar}')


""

#Exercício 6:

listaMedia = []
cont = 0
for i in range (3):

    nota1 = float(input(f'Digite a primeira nota {i+1}º do  aluno: '))
    nota2 = float(input(f'Digite a segunda nota do {i+1}º aluno: '))
    nota3 = float(input(f'Digite a terceira nota do {i+1}º aluno: '))
    nota4 = float(input(f'Digite a quarta nota do {i+1}º aluno: ' ))
    listaMedia.append(((nota1+nota2+nota3+nota4)/4))

for i in listaMedia:
    if i >= 7:
        cont += 1

print(cont)


""

#Exercício 7:

multiplicacao = 1
listaNum = []

for i in range (5):
    num = float(input(f'Digite o {i+1}º número: '))
    multiplicacao *= num
    listaNum.append(num)
print(f'Lista: {listaNum}\nSoma: {sum(listaNum)}\nMultiplicação: {multiplicacao}')


""

#Exercício 8:

listaIdades = []
listaAlturas = []

for i in range (5):
    idade = int(input('Digite sua idade: '))
    listaIdades.append(idade)
    altura = int(input('Digite sua altura em cm: '))
    listaAlturas.append(altura)

for i in range (5):
    print(f'Altura: {listaAlturas[i]}\nIdade: {listaIdades[i]}')


""

#Exercício 9:

listaQuadrados = []

for i in range (10):

    num = float(input(f'Digite o {i+1}º número: '))

    listaQuadrados.append(num**2)

print(listaQuadrados)


""

#Exercício 10:

lista1 = []
lista2 = []

for i in range(20):
    if i < 10:
        num = float(input(f'Digite o {i+1}º número da primeira lista: '))
        lista1.append(num)

    else:
        num = float(input(f'Digite o {i-9}º número da segunda lista: '))
        lista2.append(num)

print(lista1 + lista2)


""

#Exercício 11:

lista1 = []
lista2 = []
lista3 = []

for i in range(30):
    if i < 10:
        num = float(input(f'Digite o {i+1}º número da primeira lista: '))
        lista1.append(num)

    elif i < 20:
        num = float(input(f'Digite o {i-9}º número da segunda lista: '))
        lista2.append(num)

    else:
        num = float(input(f'Digite o {i - 19}º número da terceira lista: '))
        lista3.append(num)

for i in range(10):
    print(lista1[i],lista2[i],lista3[i],end=' ')

""

#Exercício 12:

listaIdades = []
listaAlturas = []
cont = 0

for i in range (5):
    idade = int(input('Digite sua idade: '))
    listaIdades.append(idade)
    altura = int(input('Digite sua altura em cm: '))
    listaAlturas.append(altura)


for i in range(5):
    if listaIdades[i] >= 13 and listaAlturas[i] <= ((sum(listaAlturas))/len(listaAlturas)):
        cont += 1

print(cont)


""


#Exercício 13:

listaTemperaturas = []
listaMeses = []

for i in range (12):
    temperatura = int(input('Digite a temperatura: '))
    listaTemperaturas.append(temperatura)
    mes = str(input('Digite o mês: '))
    listaMeses.append(mes)


for i in range(12):
    if listaTemperaturas[i] >= ((sum(listaTemperaturas))/len(listaTemperaturas)):
        print(f'[{listaMeses[i]} - {listaTemperaturas[i]}]',end=' ')


""

#Exercício 14:

lista = []

print('Responda as seguinte perguntar com ''S'' ou ''N'', para sim ou não. ')
a = str(input('Você telefonou para vitima? '))
if (a.upper()) == 'S':
    lista.append(a)
b = str(input('Você esteve no local do crime? '))
if (b.upper()) == 'S':
    lista.append(b)
c = str(input('Você mora perto da vitima? '))
if (c.upper()) == 'S':
    lista.append(c)
d = str(input('Você devia dinheiro para vitima? '))
if (d.upper()) == 'S':
    lista.append(d)
e = str(input('Ja trabalhou com a vitima? '))
if (e.upper()) == 'S':
    lista.append(e)


if len(lista) == 5:
    print('Assassino')

elif 3 <= (len(lista)) <= 4:
    print('Cúmplice')

elif len(lista) == 2:
    print('Suspeito')

else:
    print('Inocente')


""

#Exercício 15:

cont0 = 0
cont = 0
listaValores = []

while True:

    valores = int(input('Digite quantos valores quiser '))
    if valores == -1:
        break

    listaValores.append(valores)

print(f'{len(listaValores)}\n{(sum(listaValores))}\n{sum(listaValores)/len(listaValores)}')

for i in listaValores:
    print(i,end=' ')
print()


for i in reversed(listaValores):

    print(i)


for i in listaValores:

    if i >= ((sum(listaValores))/len(listaValores)):

        cont0 += 1
        print(i,end=' ')
print()
print(cont0)

for i in listaValores:

    if i >= 7:

        cont += 1

print(cont)

print('Encerrando o programa com uma mensagem')

""


#Exercício 16:

listaContadores = []

conta = 0
contb = 0
contc = 0
contd = 0
conte = 0
contf = 0
contg = 0
conth = 0
conti = 0


while True:

    vendas = int(input('Digite o valor de vendas brutas do vendedor: '))

    if vendas == 0:
        break

    if 200 <= (vendas*0.09 +200) <= 299:

        conta += 1

    elif 300 <= (vendas*0.09 +200) <= 399:

        contb += 1

    elif 400 <= (vendas*0.09 +200) <= 499:

        contc += 1

    elif 500 <= (vendas*0.09 +200) <= 599:

        contd += 1

    elif 600 <= (vendas*0.09 +200) <= 699:

        conte += 1

    elif 700 <= (vendas*0.09 +200) <= 799:

        contf += 1

    elif 800 <= (vendas*0.09 +200) <= 899:

        contg += 1

    elif 900 <= (vendas*0.09 +200) <= 999:

        conth += 1

    elif (vendas*0.09 +200) >= 1000:

        conti += 1

listaContadores.extend((conta,contb,contc,contd,conte,contf,contg,conth,conti))

print(f'{listaContadores[0]} recebem de 200 R$ a 299 R$\n{listaContadores[1]} recebem de 300 R$ até 399 R$\n{listaContadores[2]} recebem de 400 R$ a 499 R$'
      f'\n{listaContadores[3]} recebem de 500 R$ até 599 R$\n{listaContadores[4]} recebem de 600 R$ até 699 R$\n{listaContadores[5]} recebem de 700 R$ até 799 R$'
      f'\n{listaContadores[6]} recebem de 800 R$ até 899 R$\n{listaContadores[7]} recebem de 900 R$ até 999 R$\n{listaContadores[8]} recebem acima de 1000 R$')


""

#Exercício 17:

saltos = str(input(f'Digite a distância dos saltos do atleta: '))
listaSaltos = saltos.split()

print(f'Primeiro salto: {listaSaltos[0]}m\nSegundo salto: {listaSaltos[1]}m\nTerceiro salto: {listaSaltos[2]}m\nQuarto salto: {listaSaltos[3]}m\nQuinto salto: {listaSaltos[4]}m')

listaSaltos.sort()

print(f'\nMelhor salto: {listaSaltos[4]}m\nPior salto: {listaSaltos[0]}m\nMédia dos demais saltos: {((float(listaSaltos[1]))+float(listaSaltos[2])+float(listaSaltos[3]))/3}')


""


#Exercício 18:

listaVotos = []

while True:

    num = int(input('Digite um número de 1 a 23: '))

    if num == 0:
        break

    if  1 > num or num > 23:

        print('Número inválido, digite novamente')

    if 1 <= num <= 23:

        listaVotos.append(num)

print(f'O total de votos foi de {len(listaVotos)}\n')

tamanho = len(listaVotos)

for i in listaVotos:

    cont = 0
    cont = listaVotos.count(i)
    print(f'{cont} para o jogador da camisa {i}\nPorcentagem: {round((cont*100/tamanho),2)} %')
    conta = 0

    while i in listaVotos:

        if listaVotos[conta] == i:
            del (listaVotos[conta])

            conta -= 1

        conta += 1


""


#Exercício 19:

listaVotos = []
campeao = '0'
pontos = 0

while True:

    num = int(input('Digite um número de 1 a 6, ou 0 se quiser sair: '))

    if num == 0:
        break

    if  1 > num or num > 6:

        print('Número inválido, digite novamente')

    if 1 <= num <= 6:

        listaVotos.append(num)

print(f'O total de votos foi de {len(listaVotos)}\n')

tamanho = len(listaVotos)

if listaVotos.count(1) >= listaVotos.count(2) and listaVotos.count(3) and listaVotos.count(4) and listaVotos.count(5) and listaVotos.count(6):

    campeao = 'Windows Server'
    pontos = listaVotos.count(1)

elif listaVotos.count(2) >= listaVotos.count(1) and listaVotos.count(3) and listaVotos.count(4) and listaVotos.count(5) and listaVotos.count(6):

    campeao = 'Unix'
    pontos = listaVotos.count(2)

elif listaVotos.count(3) >= listaVotos.count(1) and listaVotos.count(2) and listaVotos.count(4) and listaVotos.count(5) and listaVotos.count(6):

    campeao = 'Linux'
    pontos = listaVotos.count(3)

elif listaVotos.count(4) >= listaVotos.count(1) and listaVotos.count(2) and listaVotos.count(3) and listaVotos.count(5) and listaVotos.count(6):

    campeao = 'Netware'
    pontos = listaVotos.count(4)

elif listaVotos.count(5) >= listaVotos.count(1) and listaVotos.count(2) and listaVotos.count(3) and  listaVotos.count(4) and listaVotos.count(6):

    campeao = 'Mac OS'
    pontos = listaVotos.count(5)

elif listaVotos.count(6) >= listaVotos.count(1) and listaVotos.count(2) and listaVotos.count(3) and listaVotos.count(4) and listaVotos.count(5):

    campeao = 'Outro'
    pontos = listaVotos.count(6)

for i in listaVotos:

    cont = 0
    cont = listaVotos.count(i)

    if i == 1:
        print(f'{cont} para o sistema Windows Server\nPorcentagem: {round((cont*100/tamanho),2)} %')

    if i == 2:
        print(f'{cont} para o sistema Unix\nPorcentagem: {round((cont*100/tamanho),2)} %')

    if i == 3:
        print(f'{cont} para o sistema Linux\nPorcentagem: {round((cont*100/tamanho),2)} %')

    if i == 4:
        print(f'{cont} para o sistema Netware\nPorcentagem: {round((cont*100/tamanho),2)} %')

    if i == 5:
        print(f'{cont} para o sistema Mac OS\nPorcentagem: {round((cont*100/tamanho),2)} %')

    if i == 6:
        print(f'{cont} para Outro\nPorcentagem: {round((cont*100/tamanho),2)} %')

    conta = 0

    while i in listaVotos:

        if listaVotos[conta] == i:
            del (listaVotos[conta])

            conta -= 1

        conta += 1

for i in listaVotos:

    cont = 0
    cont = listaVotos.count(i)

    if i == 1:
        print(f'{cont} para o sistema Windows Server\nPorcentagem: {round((cont * 100 / tamanho), 2)} %')

    if i == 2:
        print(f'{cont} para o sistema Unix \nPorcentagem: {round((cont * 100 / tamanho), 2)} %')

    if i == 3:
        print(f'{cont} para o sistema Linux\nPorcentagem: {round((cont * 100 / tamanho), 2)} %')

    if i == 4:
        print(f'{cont} para o sistema Netware\nPorcentagem: {round((cont * 100 / tamanho), 2)} %')

    if i == 5:
        print(f'{cont} para o sistema Mac OS\nPorcentagem: {round((cont * 100 / tamanho), 2)} %')

    if i == 6:
        print(f'{cont} para Outro\nPorcentagem: {round((cont * 100 / tamanho), 2)} %')

    conta = 0

    while i in listaVotos:

        if listaVotos[conta] == i:
            del (listaVotos[conta])

            conta -= 1

        conta += 1

print(f'Total: {tamanho}\nO sistema operacional mais votado foi: {campeao}, com {pontos} votos, correspondendo a {round((pontos*100/tamanho),2)}')


""


#Exercício 20:

listaSalario = []
listaAbono = []
cont100 = 0
maiorAbono = 100

while True:

    salario = int(input('Digite o valor do salário do funcionário: '))

    if salario == 0:
        break

    if salario < 0:
        print('Dados inválidos ')

    listaSalario.append(salario)

for i in range (len(listaSalario)):

    if listaSalario[i]*0.2 >= 100:

        listaAbono.append(0.2*listaSalario[i])

    else:

        listaAbono.append(100)

for i in range(len(listaAbono)):

    if listaAbono[i] >= maiorAbono:

        maiorAbono = listaAbono[i]

for i in range(len(listaSalario)):

    cont100 = listaAbono.count(100)
    print(f'Funcionário {i+1}, salário: R$ {listaSalario[i]} - abono: R$ {listaAbono[i]}\n')

print(f'Foram processados {len(listaSalario)} colaboradores\nTotal gasto com abonos: {sum(listaAbono)}\nValor mínimo pago a {cont100} colaboradores\nMaior valor de abono pago: R$ {maiorAbono}')


""

#Exercício 21:

listaConsumoOrdenada = []
listaCarros = []
listaConsumo = []

while True:

    carro = str(input('Digite o nome do carro: '))

    if carro == '0':

        break

    consumo = float(input('Digite o consumo km/l do carro: '))

    listaCarros.append(carro)
    listaConsumo.append(consumo)


listaConsumoOrdenada = sorted(listaConsumo)
listaNovaCarros = []
listaPreco = []

for i in range(len(listaConsumo)):

    if listaConsumo[i] == listaConsumoOrdenada[0]:

        listaNovaCarros.insert(0,f'{listaCarros[i]}')

    elif listaConsumo[i] == listaConsumoOrdenada[1]:

        listaNovaCarros.insert(1,f'{listaCarros[i]}')

    elif listaConsumo[i] == listaConsumoOrdenada[2]:

        listaNovaCarros.insert(2,f'{listaCarros[i]}')

    elif listaConsumo[i] == listaConsumoOrdenada[3]:

        listaNovaCarros.insert(3,f'{listaCarros[i]}')

    elif listaConsumo[i] == listaConsumoOrdenada[4]:

        listaNovaCarros.insert(4,f'{listaCarros[i]}')


print('Relatório final: ')

for i in range(len(listaNovaCarros)):
    print(f'{i+1} - {listaNovaCarros[i]}                  -    {listaConsumoOrdenada[i]} km/l - {round(((1000/listaConsumo[i])),1)} Litros - R$ {round(((1000/listaConsumo[i]*2.25)),2)}')

print(f'O menor consumo é do {listaNovaCarros[-1]}.')



""


#Exercício 22:

from random import randint

listaDefeitos = ['Necessita de esfera', 'Necessita de limpeza', 'Necessita troca do cabo ou conector', 'Quebrado ou inutilizado']
listaQtidade = []
mouse = int(input('Digite a quantidade de mouses que serão avaliados: '))

for i in range (mouse):

    listaQtidade.append(randint(1,4))


print('Situação                        Quantidade                 Percentual')


for i in range (1,5):

    print(f'{i}- {listaDefeitos[i-1]}           {listaQtidade.count(i)}               {(listaQtidade.count(i)*100)/len(listaQtidade)}%')



""


#Exercício 23:

listaEspaco = []
listaUsuario = []


def conversor (espaco):

    espaco /= 2**20

    return espaco

while True:

    usuario = str(input('Digite o nome do usuário: '))

    if usuario == '0':

        break

    arquivos = int(input('Digite o espaço utilizado pelo usuário: '))

    listaUsuario.append(usuario)
    listaEspaco.append(arquivos)

for i in range (len(listaEspaco)):

    listaEspaco[i] = conversor(listaEspaco[i])

for i in range (len(listaEspaco)):

    print(f'{i+1}   {listaUsuario[i]}          {round((listaEspaco[i]),2)} MB           {round((listaEspaco[i]*100/sum(listaEspaco)),2)}%')


""


#Exercício 24:

from random import randint

listaValores = []

for i in range (200):

    listaValores.append(randint(1,6))


for i in range (0,6):

    print(f'O número {i+1} foi tirado {listaValores.count(i+1)} vezes')



""