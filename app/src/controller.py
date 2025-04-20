# Importa o banco de dados e a interface da aplicação
from src.database.database import dataBase
from src.screen.screen import Interface
from src.database.admin import runAdminMenu
from src.utils import testType

# Instancia objetos da interface gráfica e do banco de dados
interface = Interface()
db = dataBase()

def runBookSearchMenu(user_name):
    """
    Executa o menu de busca de livros do usuário autenticado.

    Permite a busca por:
        - Nome do livro
        - Autor
        - Todos os livros cadastrados pelo usuário

    Args:
        user_name (str): Nome do usuário logado
    """
    # Obtém o ID do usuário
    reader_id_target = db.getUserId(user_name)

    while True:
        # Exibe o menu de busca
        option = interface.createOptionSerchScreen()

        if option == "1":
            # Busca por nome do livro
            name = interface.createBookSearchScreenName()
            if name != "" and isinstance(name, str):
                books = db.searchBook(reader_id=reader_id_target, name=name, selection="book")
                if books:
                    print("Livros encontrados:")
                    for book in books:
                        print(f"Nome: {book[2]}, Autor: {book[3]}, Data de Leitura: {book[4]}\n")
                else:
                    print("Nenhum livro encontrado.")
            else:
                print("Nome do livro inválido.")

        elif option == "2":
            # Busca por autor
            author = interface.createBookSearchScreenAuthor()
            if author != "" and isinstance(author, str) and testType(author):
                books = db.searchBook(reader_id=reader_id_target, author=author)
                if books:
                    print("Livros encontrados:")
                    for book in books:
                        print(f"Nome: {book[2]}, Autor: {book[3]}, Data de Leitura: {book[4]}\n")
                else:
                    print("Nenhum livro encontrado.")
                    runBookSearchMenu(user_name)
            else:
                print("Nome do autor inválido.")

        elif option == "3":
            # Busca todos os livros cadastrados
            books = db.searchBook(reader_id=reader_id_target, selection="all")
            if books:
                print("Livros encontrados:")
                for book in books:
                    print(f"Nome: {book[2]}, Autor: {book[3]}, Data de Leitura: {book[4]}\n")
            else:
                print("Nenhum livro encontrado.")
                break

        elif option == "4":
            # Retorna ao menu anterior
            break

        else:
            print("Opção inválida. Tente novamente.")

def runUserMenu(user_name):
    """
    Executa o menu principal de funcionalidades para o usuário autenticado.

    Permite:
        - Cadastrar livros
        - Buscar livros
        - Buscar usuários
        - Alterar senha
        - Excluir livro cadastrado
        - Sair do sistema

    Args:
        user_name (str): Nome do usuário logado
    """
    while True:
        option = interface.createUserMenu()

        if option == "1":
            # Cadastro de novo livro
            name, author, readdate = interface.createBookScreen()
            if name != "" and testType(name) and testType(author) and testType(readdate):
                user_id = db.getUserId(user_name)
                if not db.verifyBook(user_id, name):
                    db.insertBook(reader_id=user_id, name=name, author=author, readdate=readdate)
                    print("Livro cadastrado com sucesso!")
                else:
                    print("Livro já cadastrado")
            else:
                print("Dados inválidos.")
                runUserMenu(user_name)

        elif option == "2":
            # Acesso ao menu de busca de livros
            runBookSearchMenu(user_name)

        elif option == "3":
            # Busca por outro usuário pelo nome
            name_target = interface.createUserSearchScreen()
            if name_target != "" and isinstance(name_target, str):
                if db.verifyUser(name=name_target):
                    users = db.searchUser(name=name_target)
                    for user in users:
                        print(f'Nome: {user[1]}')
                else:
                    print("Usuário não encontrado.")
            else:
                print("Nome do usuário inválido.")

        elif option == "4":
            # Atualização de senha do usuário
            past_password, new_password = interface.createUpdateScreen()
            if past_password != "" and new_password != "":
                if db.login(name=user_name, password=past_password):
                    db.updateUser(id=db.getUserId(user_name), password=new_password)
                    print("Senha atualizada com sucesso!")
                else:
                    print("Usuário ou senha incorretos.")
            else:
                print("Senha inválida")

        elif option == "5":
            # Exclusão de um livro específico
            book_target, author_target = interface.createDeleteBookScreen()
            if book_target != "" and testType(book_target):
                if not db.verifyBook(reader_id=db.getUserId(user_name), name=book_target, author=author_target):
                    db.deleteBook(reader_id=db.getUserId(user_name), name=book_target)
                    print("Livro excluído com sucesso!")
                else:
                    print("Livro não encontrado ou autor não reconhecido.")

        elif option == "6":
            # Saída do sistema
            interface.createExitScreen()
            break

        else:
            print("Opção inválida. Tente novamente.")

def run():
    """
    Função principal da aplicação. Responsável pelo fluxo inicial de:
        - Cadastro de usuários
        - Login de usuários
        - Encerramento da aplicação
    """
    while True:
        option = interface.createInitialScreen()

        if option == "1":
            # Cadastro de novo usuário
            name, password = interface.createRegisterScreen()
            if name != "0":
                if name != "" and password != "" and testType(name) and isinstance(name, str) and isinstance(password, str):
                    if db.verifyUser(name=name):
                        print("Nome de usuário já cadastrado.")
                    else:
                        db.insertUser(name, password)
                        print("Usuário cadastrado com sucesso!")
                        runUserMenu(name)
                else:
                    print("Nome de usuário ou senha inválidos.")

        elif option == "2":
            # Login de usuário
            name, password = interface.createLoginScreen()
            if name != "" and password != "" and testType(name) and isinstance(name, str) and isinstance(password, str):
                if db.login(name, password):
                    print("Login bem-sucedido!")
                    runUserMenu(name)
                else:
                    print("Nome de usuário ou senha incorretos.")

        elif option == "3":
            # Encerrar sistema
            interface.createExitScreen()
            db.__del__()
            break
        
        elif option == "0000":
            runAdminMenu()
        else:
            print("Opção inválida. Tente novamente.")
