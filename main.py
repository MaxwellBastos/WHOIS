import whois
from time import sleep
print('Iniciando o WHOIS...')
sleep(2)
saber = str(input('Você sabe pra que serve o comando WHOIS? (S/N): ')).strip().upper()
if saber == 'S':
    print('Ok, então vamos iniciar a operação: ')
elif saber == 'N':
    print('''
    O WHOIS é um protocolo que armazena as informações sobre domínios na web,
    através desse comando você consegue coletar informações públicas sobre esses domínios.
    É só digitar o site e te mostraremos informações sobre ele: 
    ''')
sleep(1)


dominio = input("Site: ")

coletaWhois = whois.whois(dominio)

print(coletaWhois.text)

saber = str(input('Deseja fazer uma outra operação? (S/N): ')).strip().upper()
while saber == 'S':
    dominio = input("Site: ")
    coletaWhois = whois.whois(dominio)

    print(coletaWhois.text)
    saber = str(input('Deseja fazer uma outra operação? (S/N): ')).strip().upper()
else:
    print('Finalizando...')
    sleep(1)
    print('Espero ter ajudado, volte sempre!!')