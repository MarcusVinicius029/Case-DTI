class Interface:
    """
    Classe responsável por lidar com a interface de texto do aplicativo de leitura,
    exibindo menus e capturando entradas do usuário.
    """

    def __init__(self):
        """
        Inicializa a instância da interface.
        Atualmente não realiza nenhuma configuração adicional.
        """
        pass

    def createInitialScreen(self):
        """
        Exibe a tela inicial do aplicativo com as opções principais.

        Returns:
            int: Opção escolhida pelo usuário:
                - 1: Cadastrar novo usuário.
                - 2: Fazer login.
                - 3: Encerrar o programa.
        """
        print("Seja Bem Vindo!!")
        print("1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Sair")
        return input("Escolha uma opção: ")
    
    def createUserMenu(self):
        """
        Exibe o menu de funcionalidades disponíveis para o usuário logado.

        Returns:
            int: Opção escolhida pelo usuário:
                - 1: Cadastrar livro.
                - 2: Buscar livro.
                - 3: Buscar usuário.
                - 4: Atualizar senha.
                - 5: Excluir livro.
                - 6: Sair da conta.
        """
        print("Menu do Usuário")
        print("1. Cadastrar Livro")
        print("2. Buscar Livro")
        print("3. Buscar Usuário")
        print("4. Atualizar Senha")
        print("5. Excluir Livro")
        print("6. Sair")
        return input("Escolha uma opção: ")
    
    def createRegisterScreen(self):
        """
        Exibe a tela de cadastro de usuário.

        Returns:
            tuple: Contém:
                - name (str): Nome do usuário.
                - password (str): Senha do usuário.
        """
        print("Tela de Cadastro de Usuário")
        name = input("Digite seu nome: ").replace(" ", "")
        password = input("Digite sua senha: ").replace(" ", "")
        return name, password
    
    def createLoginScreen(self):
        """
        Exibe a tela de login para usuários existentes.

        Returns:
            tuple: Contém:
                - name (str): Nome de login.
                - password (str): Senha.
        """
        print("Tela de Login")
        name = input("Digite seu nome: ").replace(" ", "")
        password = input("Digite sua senha: ").replace(" ", "")
        return name, password
    
    def createBookScreen(self):
        """
        Exibe a tela de cadastro de livro.

        Returns:
            tuple: Contém:
                - name (str): Nome do livro.
                - author (str): Nome do autor (opcional).
                - readdate (str): Data de leitura (opcional).
        """
        print("Tela de Cadastro de Livro")
        name = input("Digite o nome do livro: ").strip()
        author = input("Digite o autor do livro (opcional): ").strip()
        readdate = input("Digite a data de leitura (opcional): ").strip()
        return name, author, readdate
    
    def createOptionSerchScreen(self):
        """
        Exibe as opções de busca de livros.

        Returns:
            int: Opção escolhida pelo usuário:
                - 1: Buscar por nome.
                - 2: Buscar por autor.
                - 3: Mostrar todos os livros do usuário.
                - 4: Voltar.
        """
        print("Tela de Opções de Busca de Livros")
        print("1. Buscar por nome")
        print("2. Buscar por autor")
        print("3. Mostrar todos os meus livros")
        print("4. Voltar")
        return input("Escolha uma opção: ")
    
    def createUseroptionSerchScreen(self):
        """
        Exibe as opções de busca de usuários.

        Returns:
            int: Opção escolhida pelo usuário:
                - 1: Buscar por nome.
                - 2: Buscar por ID.
                - 3: Voltar ao menu anterior.
        """
        print("Tela de Opções de Busca de Usuários")
        print("1. Buscar por nome")
        print("2. Buscar por ID")
        print("3. Voltar")
        return input("Escolha uma opção: ")
    
    def createBookSearchScreenName(self):
        """
        Solicita ao usuário o nome do livro a ser buscado.

        Returns:
            str: Nome do livro.
        """
        print("Tela de Busca de Livros")
        search_option = input("Digite o nome do livro: ").strip()
        return search_option
    
    def createBookSearchScreenAuthor(self):
        """
        Solicita ao usuário o nome do autor a ser buscado.

        Returns:
            str: Nome do autor.
        """
        print("Tela de Busca de Livros por Autor")
        search_option = input("Digite o nome do autor: ").strip()
        return search_option
    
    
    def createUserSearchScreen(self):
        """
        Solicita o nome do usuário a ser buscado.

        Returns:
            str: Nome do usuário.
        """
        print("Tela de Busca de Usuários")
        search_option = input("Digite o nome do usuário: ").strip()
        return search_option
    
    def createUserSearchScreenId(self):
        """
        Solicita o ID do usuário a ser buscado.

        Returns:
            str: ID do usuário (deve ser convertido para inteiro no uso, se necessário).
        """
        print("Tela de Busca de Usuários por ID")
        search_option = input("Digite o ID do usuário: ").strip()
        return search_option
    
    def createUpdateScreen(self):
        """
        Exibe a tela de atualização de senha de usuário.

        Returns:
            tuple: Contém:
                - user_name (str): Nome do usuário.
                - past_password (str): Senha atual.
                - new_password (str): Nova senha.
        """
        print("Tela de Atualização de Usuário")
        past_password  = input("Digite a sua senha: ").strip()
        new_password = input("Digite a nova senha: ").strip()
        return past_password, new_password
    
    def createDeleteBookScreen(self):
        """
        Exibe a tela de exclusão de livro.

        Returns:
            tuple: Contém:
                - name (str): Nome do livro.
                - author (str): Nome do autor (opcional).
        """
        print("Tela de Exclusão de Livro")
        name = input("Digite o nome do livro que deseja excluir: ").strip()
        author = input("Digite o autor do livro (opcional): ").strip()
        return name, author
    
    def createExitScreen(self):
        """
        Exibe mensagem de saída do aplicativo e encerra a execução.
        """
        print("Obrigado por usar a aplicação!!")
        print("Saindo...")
