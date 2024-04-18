from time import sleep
import os

restaurantes = [
    
    {'nome':'Livota Gourmet', 'categoria':'Japonesa Premium', 'ativo':False},
    {'nome':'Fredoca Restaurante', 'categoria':'Brasileira', 'ativo':False},
    {'nome':'Batatinha Express', 'categoria':'Fast-Food', 'ativo':True}
    
]

def exibir_nome_programa():
    print('''
        
    █▀ ▄▀█ █▄▄ █▀█ █▀█   █▀▀ ▀▄▀ █▀█ █▀█ █▀▀ █▀ █▀
    ▄█ █▀█ █▄█ █▄█ █▀▄   ██▄ █░█ █▀▀ █▀▄ ██▄ ▄█ ▄█

        ''')

def exibe_menu():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair...')

def finalizar_app():
    exibir_subtitulo('Finalizando o app')
    sleep(2)

def opcao_invalida():
    exibir_subtitulo('Opção inválida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(f'* {texto} *')
    print(linha)
    
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante!')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- Nome: {nome_restaurante.ljust(20)} | categoria: {categoria_restaurante.ljust(20)} | ativo: {ativo}')
        
    voltar_ao_menu_principal()

def escolher_opcao():
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
    
        else:
            opcao_invalida()
    except:
        print('Opção inválida')
        voltar_ao_menu_principal()

def alternar_status_restaurante():
    exibir_subtitulo('Alternando status do Restautante...')
    nome_restaurante = input('Qual o nome do Restaurante que deseja alterar o status: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O Restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O Restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')    
    voltar_ao_menu_principal()
    

def main():
    os.system('cls')
    exibir_nome_programa()
    exibe_menu()
    escolher_opcao()


if __name__ == '__main__':
    main()
