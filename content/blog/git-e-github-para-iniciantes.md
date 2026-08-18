Title: Git e GitHub para iniciantes: versione seu código e colabore com a comunidade
Date: 2026-08-23 09:00
Modified: 2026-08-23 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda os fundamentos de Git e GitHub para versionar seus projetos e contribuir com projetos open source como o Grupy São Marcos.

Se você já Programou algo e precisou voltar uma versão anterior do código, provavelmente já criou uma pasta chamada `projeto_v2`, `projeto_v3_final`, `projeto_v3_final_real`. Todo mundo já passou por isso.

O **Git** resolve esse problema de forma profissional. Ele é um sistema de **controle de versão** que registra cada mudança que você faz no código, permitindo voltar a qualquer momento e trabalhar em equipo sem conflitos. O **GitHub** é a plataforma onde você hospeda seus projetos Git e colabora com outras pessoas.

## Instalando o Git

No Linux (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install git
```

No Mac (com Homebrew):

```bash
brew install git
```

No Windows, baixe o instalador em [git-scm.com](https://git-scm.com).

Após instalar, configure seu nome e email (esses dados aparecem nas suas contribuições):

```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"
```

## Criando seu primeiro repositório

Para iniciar um projeto com Git, crie uma pasta e rode:

```bash
mkdir meu-projeto
cd meu-projeto
git init
```

Isso cria uma pasta oculta `.git` que guarda todo o histórico do projeto. A partir daqui, o Git começa a rastrear seus arquivos.

## O ciclo básico: add, commit, push

O fluxo de trabalho do Git tem três passos principais:

```bash
# 1. Selecionar o que vai ser salvo
git add arquivo.py

# 2. Registrar uma "foto" do momento
git commit -m "Adiciona funcionalidade de login"

# 3. Enviar para o GitHub
git push origin main
```

Pense no `commit` como um **ponto de salvação** no jogo. Você pode criar quantos commits quiser e voltar a qualquer um deles.

## Trabalhando com branches

Uma **branch** é uma linha de desenvolvimento separada. Em vez de mexer direto no código principal, você cria uma branch para experimentar, e só mescla (merge) quando estiver pronto.

```bash
# Criar e mudar para uma nova branch
git checkout -b nova-funcionalidade

# ... fazer alterações ...

# Adicionar e commitar
git add .
git commit -m "Implementa busca de artigos"

# Enviar a branch para o GitHub
git push origin nova-funcionalidade
```

No GitHub, você abre um **Pull Request** (PR) para que outra pessoa revise seu código antes de unir à branch principal.

## Contribuindo com projetos open source

Contribuir com open source parece assustador, mas o fluxo é simples:

1. **Fork** do repositório (cria uma cópia no seu GitHub)
2. **Clone** do fork para sua máquina
3. Criar uma branch para sua contribuição
4. Fazer as alterações e commitar
5. Enviar para o fork e abrir um Pull Request

```bash
# Clonar seu fork
git clone https://github.com/seu-usuario/projeto.git
cd projeto

# Criar branch para sua contribuição
git checkout -b melhoria-no-readme

# ... alterar arquivos ...

git add .
git commit -m "Corrige typo no README"
git push origin melhoria-no-readme
```

O repositório do Grupy São Marcos é aberto e aceita contribuições. Se você encontrou um erro no site, quer escrever um artigo ou melhorar algo, é só seguir esse fluxo.

## Comandos essenciais

Aqui vai uma lista dos comandos que você vai usar no dia a dia:

| Comando | O que faz |
|---------|-----------|
| `git status` | Mostra o estado atual do repositório |
| `git log --oneline` | Lista os commits de forma resumida |
| `git diff` | Mostra o que mudou desde o último commit |
| `git checkout -b nome` | Cria e muda para uma nova branch |
| `git merge branch` | Une uma branch à atual |
| `git stash` | Guarda alterações temporariamente |
| `git pull` | Baixa as atualizações do repositório remoto |

## Dicas para começar

- **Commit frequentemente**: commits pequenos e descritivos são muito mais fáceis de entender do que um único commit gigante.
- **Escreva mensagens claras**: "Corrige bug no login" é melhor que "update".
- **Não tenha medo de errar**: Git permite desfazer quase qualquer coisa. Se você estragar algo, provavelmente tem um comando para resolver.
- **Pratique**: crie um repositório pessoal no GitHub e comece a versionar seus projetos.

O Git tem uma curva de aprendizado no início, mas depois que você pega o jeito, não consegue imaginar programar sem ele. E o GitHub abre portas para colaborar com desenvolvedores do mundo inteiro — inclusive aqui em São Marcos.
