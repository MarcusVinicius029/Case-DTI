# 📚 BookManager - Sistema de Cadastro e Busca de Livros Pessoais

Um sistema simples e interativo de linha de comando para cadastro, busca e gerenciamento de livros pessoais, utilizando **Python** e 
banco de dados **SQLite**. Também oferece funções administrativas avançadas e suporte a contêineres **Docker**.

---

## ⚙️ Funcionalidades

### 👤 Usuário
- Cadastro de novo usuário
- Login com autenticação
- Cadastro de livros com nome, autor e data de leitura
- Busca de livros por nome, autor ou a exibição de todos os livros registrados pelo usuário
- Atualização de senha
- Exclusão de livros

### 🛡️ Administrador
- Visualização de todos os usuários cadastrados
- Visualização de todos os livros registrados
- Exclusão de usuários específicos ou de todos os usuários
- Exclusão de todos os livros

---

## 🏁 Como rodar o projeto

### 🔧 Requisitos
- Python 3.10.12 ou superior
- Biblioteca SQLITE3 do python (Já incluída na linguagem)
- Docker (opcional, recomendado para execução isolada)

### 💻 Rodando localmente (sem Docker)

1. Clone o repositório:
```bash
git clone https://github.com/MarcusVinicius029/Case-DTI.git
cd Case-DTI

