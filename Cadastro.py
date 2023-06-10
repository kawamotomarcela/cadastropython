def validar_email(email):

    with open('Cadastros\\todosEmails.txt', 'r') as arquivo:
        emails_cadastrados = arquivo.read().split('\n')
        while email.upper() in emails_cadastrados:
            print('Usuário já cadastrado com esse email.')
            email = input('Digite um email válido: ')
    print('Email válido')
    return email

def cadastrar_pessoas():
    print('Bem Vindo - Área de Cadastro')
    usuario = input('Usuário: ')
    email = input('Email: ')
    email = validar_email(email)

    
    with open('Cadastros\\todosEmails.txt', 'a') as arquivo:
        arquivo.write(email.upper() + '\n')

   
    password1 = input('Senha: ')
    password2 = input('Senha Novamente: ')
    while password1 != password2:
        print('Suas senhas não estão iguais.')
        print('Digite sua senha: ')
        password1 = input()
        print('Digite sua senha novamente: ')
        password2 = input()

    with open('Cadastros\\'+ usuario.upper() + '.txt', 'a') as arquivo:
        arquivo.write(usuario.upper() + '\n' + email.upper() + '\n' + password1.upper())

    print('Cadastrado com sucesso!')

if __name__ == '__main__':
    cadastrar_pessoas()