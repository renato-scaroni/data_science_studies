# Various ds studies

---

-> how to run env:

## Pyenv

A instalação do pyenv consiste em 4 pequenos e bem definidos passos. Veremos a seguir:
1)Instalação das dependências

Como mostra esta página do github, são necessárias algumas instalações antes do pyenv.

    $ sudo apt-get update$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev git

2) Instalação do Pyenv

Baseado no projeto rbenv-installer o pyenv-installer deixa o processo de instalação bem mais fácil. Com um único e simples comando, você tem o pyenv instalado em sua máquina. Basta executar o comando abaixo no terminal, que baixa e executa o instalador.

    $ curl https://pyenv.run | bash

3) Configurando o ambiente

Cole o conteúdo abaixo no final do arquivo ‘~/.bashrc’

    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

Os comandos deste arquivo são executados no momento em que o usuário inicia um terminal de comando. O ponto no início do nome indica que ele é um arquivo oculto.

Se você nunca editou este arquivo e tem dúvidas em relação a sua edição, digite no terminal o comando ‘gedit ~/.bashrc’. Um arquivo texto abrirá, e bastará você colar o conteúdo acima no final do arquivo.
4) Reinicie o terminal

Para que o comando pyenv seja interpretado, é necessário abrir ou terminal. Outra opção seria executar o comando

    $ exec "$SHELL"

Ao completar estes passos o pyenv está pronto para ser utilizado. Ao final do processo o diretório criado .pyenv no seu home.


-  refs

[1] https://medium.com/data-hackers/guia-de-instala%C3%A7%C3%A3o-do-pyenv-no-ubuntu-16-04-18-04-33a33faa4d5

## Poetry

Baixe poetry via pip ou pip3
    
    pip install poetry
    
Inicialize o projeto e instale as dependencias
    
    poetry init
    
Crie o ambiente

    poetry install
    
Adicionar pacotes ao pacote posteriormente
    
    poetry add [--dev] <nome_do_pacote_python>
    
    
-  refs

[1] https://python-poetry.org/docs/basic-usage/
[2] https://towardsdatascience.com/poetry-to-complement-virtualenv-44088cc78fd1

