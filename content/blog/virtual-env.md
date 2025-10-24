Title: Primeiro Ambiente Vitual
Date: 2025-10-23 08:30
Modified: 2025-10-23 11:30
Category: Blog
Authors: Perceu Bertoletti
Summary: Vamos aprender como criar o primeiro virtual enviroment.

No desenvolvilmento de aplicações com python é muito importante sempre trabalharmos com ambientes isolados, tanto para mapear as dependencias do projeto, como para poder trabalhar com multiplas versões de uma mesma biblioteca. 
ex: Django 4.0, Django 5.0

Vamos começar vendo se o pacote de virtual env esta instalado no nosso sistema, para isso execute:

```bash
python3 -m venv
```

Se a saida for parecida com a abaixo seu pacote esta configurado com sucesso.

```bash
usage: venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear] [--upgrade] [--without-pip] [--prompt PROMPT] [--upgrade-deps] ENV_DIR [ENV_DIR ...]
venv: error: the following arguments are required: ENV_DIR
```

Caso não apareça uma resposta como essa, é importante que que veja como instalar esse pacote no seu sistema operacional, normalmente em distribuições ubuntu o comando é:

```bash
sudo apt install python3-venv
```

Para começar vamos criar um ambiente virtual com o nome de `meuambiente` 

```bash
python3 -m venv meuambiente
```

Ativando o virtual enviroment, entenda que esse tutorial é todo baseado em um sistema operacional linux ubuntu, existem algumas peculiariedades em ambiente windows mas os comandos são os mesmos para o **IOS**

```bash
source meuambiente/bin/activate
```

##### No windows

```bash
./meuambiente/Scripts/activate
```

Com o ambiente ativo você pode verificar os pacotes instalados no nosso ambiente recem criado.

```bash
pip freeze
```

Todos os pacotes pode ser instalados via `pip install` veja os pacotes em officiais em [pypi.org](https://pypi.org/)

### Exemplo de como instalar a biblioteca request

```bash
pip install requests
```

existe tambem uma forma de instalar varios pacotes apartir de um arquivo usando o comando 

```bash
pip install -r requirements.txt
```

existem muitos outras formas de gerenciar pacotes no python atravez de varios outros pacotes mas sempre acontelho usar o pacote venv para evitar dependencias para gerenciar dependencias o venv é o pacote principal e funciona muito bem.

Tenha sempre cautela para não sobrecarregar seu projeto com varios pacotes.

Para criar um arquivo com todas as dependencias você pode usar o comando:

```bash
pip freeze > requirements.txt
```

isso gera o arquivo ja com todas as dependencias e suas versões, as vezes pode ser importante limpar esse arquivo para limpar dependencias de dependencias. mas não faça isso sem ter certeza do que esta fazendo.

outra recomendação é que é possivel fazer herança nesses arquivos as vezes é preciso ter um requirements-dev e um requirements
para isso você pode colocar uma dependencia dentro da outra ex:

##### requirements-dev.txt
```
-r requirements.txt
anyio==4.3.0
blinker==1.7.0
docutils==0.20.1
feedgenerator==2.1.0
```

Assim todos os pacotes de requirements são instalados e os especificos de desenvolvimento tambem.

Sugestões e melhorias podem ser enviadas para via Pull Request no [repositorio](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io)