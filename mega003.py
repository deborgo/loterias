from random import randint
from time import sleep
import emoji
lista = list()
aposta = list()
print('\033[1:32m-*-\033[m'*15)
print(emoji.emojize('\033[1:32:41m        :moneybag:  SORTEADOR DO TUBARÃO!!  :moneybag:              \033[m', use_aliases=True))
print('\033[1:32m-*-\033[m'*15)
jogos = str(input('Qual jogo você quer apostar? ')).lower().strip()
if jogos == mega:

quant = int(input('\033[1:31mQuantas apostas você quer?\033[m '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    aposta.append(lista[:])
    lista.clear()
    tot += 1
print('\033[35m-*-' *3, f'\033[1:34m TUBARÃO ESCOLHENDO {quant} APOSTAS \033[m', '\033[35m-*-' *3)
for i, l in enumerate(aposta) :
    sleep(1)
    print(emoji.emojize(f'\033[1:32m :dollar: Aposta {i+1}: {l} :dollar: \033[m', use_aliases=True))
print('\033[1:32:41m-*-' *5, ' < BOA SORTE ! > ', '\033[1:32:41m-*-\033[m'*5)
