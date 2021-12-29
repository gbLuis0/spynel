from requests import get
from os import system

f = '\033[m'
verm = '\033[31;1m'
verd = '\033[32;1m'
amar = '\033[33;1m'
azul = '\033[34;1m'
cian = '\033[35;1m'
roxo = '\033[36;1m'
n = '\033[37;1m'

def cls():
	system('clear')


def ent():
	input('\nenter para continuar')


def ip(ip='', option=''):
    match option:
        case '1':
            req = get(f'https://ipwhois.app/json/{ip}').json()
            for k, v in req.items():
                print(f'{verd}{k}{n}: {v}')
        case '2':
            req = get(f'https://api.ipfind.com/?ip={ip}').json()
            for k, v in req.items():
                print(f'{verd}{k}{n}: {v}')
        case '3':
            req = get(f'https://ipinfo.io/{ip}/json').json()
            for k, v in req.items():
                print(f'{verd}{k}{n}: {v}')
        case '4':
            req = get(f'https://ipinfo.io/what-is-my-ip').json()
            for k, v in req.items():
                print(f'{verd}{k}{n}: {v}')


def cep(cep='', option=''):
    match option:
        case '1':
            req = get(f'https://viacep.com.br/ws/{cep}/json').json()
            for k, v in req.items():
                print(f'{verd}{k}{n}: {v}')
        case '2':
            req = get(f'https://api.postmon.com.br/v1/cep/{cep}').json()
            for k, v in req.items():
                if type(v) == dict:
                    for ch, vl in v.items():
                        print(f'\t{verd}{ch}{n}: {vl}')
                else:
                    print(f'{verd}{k}{n}: {v}')


def placa(plc=''):
    req = get(f'https://apicarros.com/v1/consulta/{placa}', verify=False).json()
    co = 0
    for k, v in req.items():
        if co == 0: cls()
        print(f'{verd}{k}{n}: {v}')
        co += 1


def cnpj(cn=''):
    req = get(f'https://www.receitaws.com.br/v1/cnpj/{cn}').json()
    for k, v in req.items():
        if type(v) == dict:
            for ch, vl in v.items():
                print(f'\t{verd}{ch}{n}: {vl}')
        elif type(v) == list:
            for its in v:
                for ch, vl in its.items():
                    print(f'\t{verd}{ch}{n}: {vl}')
        else:
            print(f'{verd}{k}{n}: {v}')


def ddd(d=''):
    req = get(f'https://brasilapi.com.br/api/ddd/v1/{d}').json()
    for k, v in req.items():
        if type(v) == list:
            print(verd+k+n+':')
            for s in v:
                print(s)
        else:
            print(f'{verd}{k}{n}: {v}')
