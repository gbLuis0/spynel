from requests import get
from os import system, execv
from sys import argv, executable
from random import choice
f = '\033[m'
vermelho = '\033[31m'
v = '\033[92;1m'
amarelo = '\033[33m'
azul = '\033[34m'
roxo = '\033[35m'
b = '\033[1m'

def clear():
	system('clear')

def restart():
	execv(executable, ['python3'] + argv)

def baner():
	system('cat banner | lolcat')

def ent():
	input('\nenter para continuar')

def crd():
	print(f'by: \033[94;1;4mSpyware{f}')

clear()
baner()
crd()
cores = ['\033[91;1m', '\033[92;1m', '\033[93;1m', '\033[94;1m', '\033[95;1m', '\033[96;1m']
cor = choice(cores)
try:
	opc = input(f'{b}[{f} {cor}1{f} {b}] >{f} {cor}IP{f} ({v}ON{f})\n{b}[{f} {cor}2{f} {b}] >{f} {cor}CEP{f} ({v}ON{f})\n{b}[{f} {cor}3{f} {b}] >{f} {cor}PLACA DE CARRO{f} ({v}ON{f})\n{b}[{f} {cor}4{f} {b}] >{f} {cor}CNPJ{f} ({v}ON{f})({v}EM TESTE{f})\n\n{b}[{f} {cor}0{f} {b}] >{f} {cor}SAIR{f}\n{b}[{f} {cor}99{f} {b}] >{f} {cor}ATUALIZAR{f}\n\n{b}>>>{f} ').strip()
except:
	restart()
if opc == '':
	restart()

if opc[0] == '1':
	while True:
		clear()
		crd()
		opc = input(f'{b}[{f} {cor}1{f} {b}] >{f} {cor}IP 1{f}\n{b}[{f} {cor}2{f} {b}] >{f} {cor}IP 2{f}\n{b}[{f} {cor}3{f} {b}] >{f} {cor}MEU IP{f}\n\n{b}[{f} {cor}0{f} {b}] >{f} {cor}SAIR{f}\n\n{b}>>>{f} ').strip()[0]
		if opc == '1':
			ip = input('IP: ').strip()
			da = get(f'https://ipinfo.io/{ip}/json').json()
			for c in da:
				if c != 'readme' and da[c] != '':
					print(f'{v}{c}:{f} {b}{da[c]}{f}')
		elif opc == '2':
			ip = input('IP: ').strip()
			da = get(f'https://api.ipfind.com/?ip={ip}').json()
			for c in da:
				if c != 'warning' and da[c] != '':
					print(f'{v}{c}:{f} {b}{da[c]}{f}')
		elif opc == '3':
			ip = get(f'https://ipinfo.io/what-is-my-ip').json()
			for i in ip:
				if i != 'readme' and ip[i] != '':
					print(f'{v}{i}:{f} {b}{ip[i]}{f}')
		elif opc == '0':
			restart()
		ent()

elif opc[0] == '2':
	while True:
		clear()
		crd()
		opc = input(f'{b}[{f} {cor}1{f} {b}] >{f} {cor}CEP 1{f}\n{b}[{f} {cor}2{f} {b}] >{f} {cor}CEP 2{f}\n\n{b}[{f} {cor}0{f} {b}] >{f} {cor}SAIR{f}\n\n{b}>>>{f} ').strip()[0]
		if opc == '1':
			cep = input(f'{b}ex:{f} 65695000\nCEP: ').strip()
			d = get(f'https://viacep.com.br/ws/{cep}/json').json()
			for c in d:
				if d[c] != '':
					print(f'{v}{c}:{f} {b}{d[c]}{f}')
		elif opc == '2':
			cep = input(f'{b}ex:{f} 65695000\nCEP: ').strip()
			d = get(f'https://trial.api.findcep.com/v1/cep/{cep}.json').json()
			for i in d:
				if d[i] != '':
					print(f'{v}{i}:{f} {b}{d[i]}{f}')
		elif opc == '0':
			restart()
		ent()

elif opc[0] == '3':
	plc = input(f'{b}ex:{f} ATJ8617\nPLACA: ').strip().upper()
	r = get(f'https://apicarros.com/v1/consulta/{plc}/json', verify=False).json()
	c = 0
	for i in r:
		if c == 0: clear(); crd()
		if r[i] != '':
			print(f'{v}{i}:{f} {b}{r[i]}{f}')
		c += 1

elif opc[0] == '4':
	cnpj = input(f'{b}ex:{f} 03778130000148\nCNPJ: ').strip()
	da = get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}/').json()
	for i in da:
		if da[i] != '':
			if type(da[i]) == str or int:
				print(f'{v}{i}:{f} {b}{da[i]}{f}')
	crd()

elif opc[0] == '0':
	clear()
	print(f'{v}Obrigado por usar o meu painel! deixe sua estrela no github e volte sempre :){f}')
	exit()

elif opc[:2] == '99':
	system('mv a.sh $HOME && cd && bash a.sh')

else:
	restart()

ent()
restart()
