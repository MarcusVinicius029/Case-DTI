import sqlite3 as sql

class dataBase:
    """
    Classe responsável por gerenciar o banco de dados SQLite, incluindo criação de tabelas, 
    inserção, verificação, busca, atualização e remoção de dados de usuários e livros.
    """

    def __init__(self):
        """
        Inicializa a conexão com o banco de dados, define o cursor e cria as tabelas, caso elas não existam.
        """
        self.conexao = sql.connect("app/src/database/banco.sqlite3")
        self.cursor = self.conexao.cursor()
        self.createTable()

    def createTable(self):
        """
        Cria as tabelas 'User' e 'Books' no banco de dados, caso ainda não existam.
        """
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                password TEXT NOT NULL
            )""")
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reader_id INTEGER NOT NULL,
                name TEXT NOT NULL,
                author TEXT,
                readdate TEXT
            )""")
        self.conexao.commit()

    def verifyUser(self, name=None, id=None, selection="name"):
        """
        Verifica se um usuário já existe pelo nome ou ID.

        Args:
            name (str): Nome do usuário.
            id (int): ID do usuário.
            selection (str): Define se a busca será por 'name' ou 'id'.

        Returns:
            Bool: True caso o usuário exista, False caso contrário.
        """
        if selection == "name":
            self.cursor.execute("SELECT 1 FROM User WHERE name LIKE ?", ("%"+name+"%",))
            if self.cursor.fetchall():
                return True
            else:
                return False
        elif selection == "id":
            self.cursor.execute("SELECT 1 FROM User WHERE id = ?", (id,))
            if self.cursor.fetchone():
                return True
            else:
                return False

    def verifyBook(self, reader_id, name):
        """
        Verifica se um livro já foi cadastrado para determinado usuário.

        Args:
            reader_id (int): ID do usuário leitor.
            name (str): Nome do livro.

        Returns:
            Bool: True caso o livro já esteja registrado, False caso contrário.
        """
        self.cursor.execute("SELECT 1 FROM Books WHERE name = ? AND reader_id = ? ", (name, reader_id,))
        if self.cursor.fetchone():
            return True
        else:
            return False

    def insertUser(self, name, password):
        """
        Insere um novo usuário no banco de dados.

        Args:
            name (str): Nome do usuário.
            password (str): Senha do usuário.

        Returns:
            None.
        """
        self.cursor.execute("INSERT INTO User (name, password) VALUES (?, ?)", (name, password,))
        self.conexao.commit()

    def insertBook(self, reader_id, name, readdate=None, author=None):
        """
        Insere um livro associado a um usuário.

        Args:
            reader_id (int): ID do usuário leitor.
            name (str): Nome do livro.
            readdate (str): Data de leitura.
            author (str): Nome do autor.

        Returns:
            None
        """
        self.cursor.execute("INSERT INTO Books (reader_id, name, author, readdate) VALUES (?, ?, ?, ?)",(reader_id, name, author, readdate))
        self.conexao.commit()

    def searchUser(self, name = None, id = None, selection = "name"):
        """
        Pesquisa usuários pelo nome (parcial) ou por ID.

        Args:
            name (str): Nome (ou parte do nome) do usuário.
            id (int): ID do usuário.
            selection (str): 'name' para busca por nome parcial, 'id' para ID exato.

        Returns:
            list or tuple: Resultados encontrados.
        """
        if selection == "name":
            self.cursor.execute("SELECT * FROM User WHERE name LIKE ?", ("%"+name+"%",))
            returnedUser = self.cursor.fetchall()
            return returnedUser
        elif selection == "id":
            self.cursor.execute("SELECT * FROM User WHERE id = ?", (id,))
            returnedUser = self.cursor.fetchone()
            return returnedUser

    def searchBook(self, reader_id, name = None, author = None, selection = "all"):
        """
        Pesquisa livros de um usuário no banco de dados com base no nome ou em todos os livros de um usuário.

        Dependendo do valor do parâmetro `selection`, a função pode procurar um livro específico pelo nome, pelo autor ou retornar todos os livro de um usuário.

        Args:
            reader_id (int): ID do usuário que é o leitor dos livros.
            name (str): Nome ou parte do nome do livro para a busca. Usado apenas quando `selection` é "book".
            author (str): Nome do autor do livro. Usado apenas quando `selection` é "author".
            selection (str): Define o tipo de pesquisa. Pode ser:
                - "book": Busca um livro específico pelo nome.
                - "author": Busca livros de um autor específico.
                - "all": Retorna todos os livros de um usuário, independentemente do nome e do autor.

        Returns:
            list: Uma lista dos livros encontrados. 
        """
        if selection == "book":
            self.cursor.execute("SELECT * FROM Books WHERE reader_id = ? AND name = ?", (reader_id, name,))
            returnedBooks = self.cursor.fetchall()
            return returnedBooks
        elif selection == "author":
            self.cursor.execute("SELECT * FROM Books WHERE reader_id = ? AND author = ?", (reader_id, author,))
            returnedBooks = self.cursor.fetchall()
            return returnedBooks
        elif selection == "all":
            self.cursor.execute("SELECT * FROM Books WHERE reader_id = ?", (reader_id,))
            returnedBooks = self.cursor.fetchall()
            return returnedBooks

    def deleteBook(self, reader_id, name):
        """
        Remove um livro específico associado a um usuário.

        Args:
            reader_id (int): ID do usuário leitor.
            name (str): Nome do livro.

        Returns:
            None
        """
        self.cursor.execute("DELETE FROM Books WHERE reader_id = ? AND name = ?", (reader_id, name,))
        self.conexao.commit()
        
    def getUserId(self, name):
        """
        Retorna o ID de um usuário com base no nome.

        Args:
            name (str): Nome do usuário a ser buscado.

        Returns:
            int: Retorna o ID do usuário.
        """
        self.cursor.execute("SELECT id FROM User WHERE name = ?", (name,))
        result = self.cursor.fetchone()
        return result[0]

    def updateUser(self, id, password):
        """
        Atualiza a senha de um usuário com base no ID.

        Args:
            id (int): ID do usuário.
            password (str): Nova senha.

        Returns:
            bool: False se o usuário não existir; None caso contrário.
        """
        if self.verifyUser("", id, "id"):
            self.cursor.execute("UPDATE User SET password = ? WHERE id = ?", (password, id))
            self.conexao.commit()
        else:
            return False
        
    def login(self, name, password):
        """
        Verifica se as credenciais de login estão corretas.

        Args:
            name (str): Nome do usuário.
            password (str): Senha do usuário.

        Returns:
            bool: True se o login for bem-sucedido, False caso contrário.
        """
        self.cursor.execute("SELECT * FROM User WHERE name = ? AND password = ?", (name, password))
        if self.cursor.fetchone():
            return True
        else:   
            return False
        
    def getAllUserRegistes(self):
        """
        [ADMIN ONLY] Retorna todos os registros da tabela de usuários.

        Returns:
            list: Uma lista de tuplas, cada uma representando um usuário no banco de dados.

        Obs:
            Função destinada ao uso administrativo para fins de auditoria ou visualização geral.
        """
        self.cursor.execute("SELECT * FROM User")
        return self.cursor.fetchall()

    def getAllBooksRegistes(self):
        """
        [ADMIN ONLY] Retorna todos os registros da tabela de livros.

        Returns:
            list: Uma lista de tuplas, cada uma representando um livro no banco de dados.

        Obs:
            Função de uso administrativo para consultas completas no sistema.
        """
        self.cursor.execute("SELECT * FROM Books")
        return self.cursor.fetchall()

    def deleteUser(self, user_name):
        """
        [ADMIN ONLY] Remove um usuário específico do banco de dados, com base no nome.

        Args:
            user_name (str): Nome do usuário a ser removido.

        Obs:
            Esta operação remove permanentemente o usuário e seus dados da tabela.
        """
        self.cursor.execute("DELETE FROM User WHERE name = ?", (user_name,))
        self.conexao.commit()

    def deleteAllBooks(self):
        """
        [ADMIN ONLY] Exclui todos os registros da tabela de livros.

        Obs:
            Esta operação remove todos os livros do sistema e não pode ser desfeita.
        """
        self.cursor.execute("DELETE FROM Books")
        self.conexao.commit()

    def deleteAllUser(self):
        """
        [ADMIN ONLY] Exclui todos os registros da tabela de usuários.

        Obs:
            Esta operação remove todos os usuários e seus dados relacionados do sistema.
            Deve ser usada com extrema cautela.
        """
        self.cursor.execute("DELETE FROM User")
        self.conexao.commit()

    def __del__(self):
        """
        Fecha a conexão com o banco de dados quando o objeto é destruído.
        """
        self.conexao.close()
