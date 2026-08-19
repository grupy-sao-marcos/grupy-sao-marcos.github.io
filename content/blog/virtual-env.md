Title: Primeiro Ambiente Virtual
Date: 2025-10-23 08:30
Modified: 2025-10-23 11:30
Category: Blog
Authors: Perceu Bertoletti
Summary: Vamos aprender como criar o primeiro ambiente virtual.

No desenvolvimento de aplicações com Python é muito importante sempre trabalharmos com ambientes isolados, tanto para mapear as dependências do projeto, como para poder trabalhar com múltiplas versões de uma mesma biblioteca. 
ex: Django 4.0, Django 5.0

Vamos começar vendo se o pacote de virtual env está instalado no nosso sistema, para isso execute:

```bash
python3 -m venv
```

Se a saída for parecida com a abaixo, seu pacote está configurado com sucesso.

```bash
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear] [--upgrade] [--without-pip] [--prompt PROMPT] [--upgrade-deps] ENV_DIR [ENV_DIR ...]
venv: error: the following arguments are required: ENV_DIR
```

Caso não apareça uma resposta como essa, é importante que veja como instalar esse pacote no seu sistema operacional. Normalmente em distribuições Ubuntu o comando é:

```bash
sudo apt install python3-venv
```

Para começar, vamos criar um ambiente virtual com o nome de `meuambiente` 

```bash
python3 -m venv meuambiente
```

Ativando o virtual environment, entenda que esse tutorial é todo baseado em um sistema operacional Linux Ubuntu. Existem algumas peculiaridades em ambiente Windows, mas os comandos são os mesmos para o **macOS**

```bash
source meuambiente/bin/activate
```

##### No Windows

```bash
./meuambiente/Scripts/activate
```

Com o ambiente ativo, você pode verificar os pacotes instalados no nosso ambiente recente criado.

```bash
pip freeze
```

Todos os pacotes podem ser instalados via `pip install`. Veja os pacotes oficiais em [pypi.org](https://pypi.org/)

### Exemplo de como instalar a biblioteca requests

```bash
pip install requests
```

Existe também uma forma de instalar vários pacotes a partir de um arquivo usando o comando:

```bash
pip install -r requirements.txt
```

Existem muitas outras formas de gerenciar pacotes no Python através de vários outros pacotes, mas sempre aconselho usar o pacote venv para evitar dependências. Para gerenciar dependências, o venv é o pacote principal e funciona muito bem.

Tenha sempre cautela para não sobrecarregar seu projeto com vários pacotes.

Para criar um arquivo com todas as dependências, você pode usar o comando:

```bash
pip freeze > requirements.txt
```

Isso gera o arquivo já com todas as dependências e suas versões. Às vezes pode ser importante limpar esse arquivo para limpar dependências de dependências, mas não faça isso sem ter certeza do que está fazendo.

Outra recomendação é que é possível fazer herança nesses arquivos. Às vezes é preciso ter um requirements-dev e um requirements. Para isso você pode colocar uma dependência dentro da outra, ex:

##### requirements-dev.txt
```
-r requirements.txt
anyio==4.3.0
blinker==1.7.0
docutils==0.20.1
feedgenerator==2.1.0
```

Assim todos os pacotes de requirements são instalados e os específicos de desenvolvimento também.

Sugestões e melhorias podem ser enviadas via Pull Request no [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io)
