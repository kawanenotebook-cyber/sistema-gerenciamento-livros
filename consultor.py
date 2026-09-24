print('Seja bem-vindo ao controle de livros da Kawane Maciel !')
lista_livros = []
id_global = 2222

def cadastrar_livro(id):
    print(' | ********** MENU CADASTRAR LIVRO ********** | ')
    print(f'Id do livro: {id}')
    nome = input('Por favor, digite o nome do LIVRO: ')
    autor = input('Por favor, digite o nome do AUTOR: ')
    editora = input('Por favor, digite o nome da EDITORA: ')
    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }
    lista_livros.append(livro.copy())

def consultar_livro():
    print(' | 1.Consultar todos | 2.Consultar por ID | 3.Consultar por autor | 4.Retornar ao menu principal |')
    opcao = input('Digite aqui a opção que deseja consultar:  ')
    print(' Todos os livros:  ')


    if opcao == '1':
        print(' Todos os livros:  ')
        for livro in lista_livros:
         print(f'ID: {livro['id']}, | NOME: {livro['nome']}, | AUTOR: {livro['autor']}, EDITORA: {livro['editora']}')

    elif opcao == '2':
        print(' Consultar por ID:  ')
        id_busca = int(input('ID do livro: '))
        for livro in lista_livros:
          if livro['id'] == id_busca:
           print(f'ID: {livro['id']}, | NOME: {livro['nome']}, | AUTOR: {livro['autor']}, EDITORA: {livro['editora']}')

    elif opcao == '3':
        print(' Consultar por autor:  ')
        autor_busca = input('Digite o nome do autor: ')
        for livro in lista_livros:
            if livro ['autor'] == autor_busca:
              print(f'ID: {livro['id']}, | NOME: {livro['nome']}, | AUTOR: {livro['autor']}, EDITORA: {livro['editora']}')

    elif opcao == '4':
        return
    else:
        print('Opção inválida! Tente novamente!')

def remover_livro():
    print('|  Menu de remoção de livros  |')
    remove= int(input('Digite o ID do livro que deseja remover:  '))
    achou_livro = False
    for livro in lista_livros:
        if livro ['id'] == remove:
            lista_livros.remove(livro)
        print('Livro removido com sucesso!')
        achou_livro = True
        break
    if achou_livro == False:
        print('ID inválido!')

#codigo principal
while True:
    print('---------------------------------------------------------')
    print('--------------- MENU PRINCIPAL --------------------------')
    print('1 - Cadastrar livros')
    print('2 - Consultar livros')
    print('3 - Remover livros')
    print('4 - Sair')

    opcao_main = input('Escolha a opção que deseja: ')
    if opcao_main == '1':
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao_main == '2':
        consultar_livro()
    elif opcao_main == '3':
        remover_livro()
    elif opcao_main == '4':
        print('Encerrrando o programa!')
        break


















