from Cadastro import *
import os

def res_pass():
    print('Digite 1 - Para fazer login')
    print('Digite 2 - Para cadastrar')
    print('Digite 3 - Para sair')
    resp = input()
    return resp


def fazer_login(login):
    for arquivo in os.listdir('Cadastros\\'):
        if arquivo == login.upper() + '.txt':
            senha = input('Digite sua senha: ')
            with open('Cadastros\\' + arquivo, 'r') as arquivo_login:
                linhas = arquivo_login.read().split('\n')
                senha_cadastrada = linhas[2]
                while senha != senha_cadastrada:
                    print('Senha incorreta!')
                    senha = input('Digite sua senha novamente: ')
            print('Bem-vindo!')
            return

    print('Usuário não encontrado.')


while True:
    resp = res_pass()
    if resp == '1':
        print('Bem-vindo ao nosso programa')
        login = input('Digite seu login: ')
        fazer_login(login)
    elif resp == '2':
        cadastrar_pessoas()
    elif resp == '3':
        break

