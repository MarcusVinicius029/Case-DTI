from src.database.database import dataBase

def runAdminMenu():
    """
    Interface de console para o administrador interagir com o banco de dados.
    Permite visualizar e deletar usuários e livros.
    """
    db = dataBase()
    
    while True:
        print("\n=== MENU ADMINISTRATIVO ===")
        print("1. Ver todos os usuários")
        print("2. Ver todos os livros")
        print("3. Deletar um usuário")
        print("4. Deletar todos os usuários")
        print("5. Deletar todos os livros")
        print("6. Sair")
        option = input("Escolha uma opção: ")

        if option == "1":
            users = db.getAllUserRegistes()
            if users:
                print("\n=== TODOS OS USUÁRIOS ===")
                for user in users:
                    print(f"ID: {user[0]}, Nome: {user[1]}, Senha: {user[2]}")
            else:
                print("Nenhum usuário encontrado.")

        elif option == "2":
            books = db.getAllBooksRegistes()
            if books:
                print("\n=== TODOS OS LIVROS ===")
                for book in books:
                    print(f"ID: {book[0]}, Leitor ID: {book[1]}, Nome: {book[2]}, Autor: {book[3]}, Data: {book[4]}")
            else:
                print("Nenhum livro encontrado.")

        elif option == "3":
            user_name = input("Digite o nome do usuário a ser deletado: ").strip()
            if user_name:
                db.deleteUser(user_name)
                print(f"Usuário '{user_name}' deletado com sucesso.")
            else:
                print("Nome inválido.")

        elif option == "4":
            confirm = input("Tem certeza que deseja deletar TODOS os usuários? (s/n): ").lower()
            if confirm == "s":
                db.deleteAllUser()
                print("Todos os usuários foram deletados.")
            else:
                print("Operação cancelada.")

        elif option == "5":
            confirm = input("Tem certeza que deseja deletar TODOS os livros? (s/n): ").lower()
            if confirm == "s":
                db.deleteAllBooks()
                print("Todos os livros foram deletados.")
            else:
                print("Operação cancelada.")

        elif option == "6":
            print("Saindo do modo administrador.")
            break

        else:
            print("Opção inválida. Tente novamente.")

    db.__del__()