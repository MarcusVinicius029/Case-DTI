# Importa a função 'run' do módulo 'utils' localizado na pasta 'src'
from src.controller import run

# Define a função principal do programa
def main():
    # Chama a função 'run', que provavelmente inicia a aplicação
    run()

# Verifica se o arquivo está sendo executado diretamente (e não importado como módulo)
if __name__ == "__main__":
    # Se for o caso, chama a função principal para iniciar o programa
    main()

