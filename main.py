from os import system
try:
	from requests import get
except:
	system('pip install requests')
from random import choice
from consus import *

banner = open('uteis/banner.txt').read()
cores = verm, verd, amar, azul, cian, roxo

while True:
	cls()
	c = choice(cores)
	print(c+banner+f)
	try:
		opc = input(f'{n}[ {c}1{n} ] > {c}IP{n} ({verd}ON{n})\n[ {c}2{n} ] > {c}CEP{n} ({verd}ON{n})\n[ {c}3{n} ] > {c}PLACA{n} ({verd}ON{n})\n[ {c}4{n} ] > {c}CNPJ{n} ({verd}ON{n})\n[ {c}5{n} ] > {c}DDD{n} ({verd}ON{n})\n\n[ {c}S{n} ] > {c}SAIR{n}\n[ {c}A{n} ] > {c}ATUALIZAR\n\n>>>{n} ').strip().lower()[0]
	except: continue

	match opc:
		case '1':
			while True:
				cls()
				try:
					opc = input(f'{n}[ {c}1{n} ] > {c}IP WHOIS{n}\n[ {c}2{n} ] > {c}IP FIND{n}\n[ {c}3{n} ] > {c}IP INFO{n}\n[ {c}4{n} ] > {c}MEU IP{n}\n\n[ {c}0{n} ] > {c}SAIR\n\n>>>{n} ').strip()[0]
				except: continue
				IP = str()
				if not opc in '12340': continue
				if opc == '0': break
				elif opc != '4':
					try:
						IP = input('(ex: 170.0.10.69)\nIP: ').strip()
					except: continue
				ip(IP, opc)
				ent()

		case '2':
			while True:
				cls()
				try:
					opc = input(f'{n}[ {c}1{n} ] > {c}VIA CEP{n}\n[ {c}2{n} ] > {c}POSTMON CEP{n}\n\n[ {c}0{n} ] > {c}SAIR\n\n>>>{n} ').strip()[0]
				except: continue
				if not opc in '120': continue
				if opc == '0': break
				try:
					CEP = input('(ex: 23555240)\nCEP: ').strip()
				except: continue
				cep(CEP, opc)
				ent()

		case '3':
			cls()
			try:
				plc = input('OBS: a api de carros tem limite de consulta por tempo,\nentão espere um pouco caso dê "limite de consultas atingido"\n(ex: hqc5669)\nPLACA: ').strip().lower()
			except: continue
			placa(plc)
			ent()

		case '4':
			try:
				cn = input('(ex: 47960950000121)\nCNPJ: ').strip()
			except: continue
			cls()
			cnpj(cn)
			ent()

		case '5':
			try:
				d = input('(ex: 31)\nDDD: ').strip()[:2]
			except: continue
			cls()
			ddd(d)
			ent()

		case 's': break
		
		case 'a':
			system('mv update.sh ../ && cd - && bash update.sh')
cls()
print(c+'Volte sempre!'+f)
