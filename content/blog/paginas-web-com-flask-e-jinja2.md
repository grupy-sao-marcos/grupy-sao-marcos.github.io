Title: Páginas web com Flask e Jinja2: do JSON ao HTML
Date: 2026-08-20 09:00
Modified: 2026-08-20 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Transforme sua API Flask em um site com páginas HTML usando o motor de templates Jinja2 e herança de layouts.

Até agora nossos exemplos de Flask devolveram **JSON**, o formato ideal para APIs consumidas por outros programas. Mas e quando você quer mostrar os dados para uma pessoa em um navegador, com uma página bonita e formatada?

Para isso o Flask usa o **Jinja2**, um motor de *templates* que já vem embutido. Com ele, você escreve páginas HTML com "espaços" que são preenchidos com dados vindos do Python. Vamos aprender na prática.

## A estrutura de pastas

O Flask espera os templates dentro da pasta `templates`:

```text
meu_app/
├── app.py
└── templates/
    └── index.html
```

## Primeira página com dados

Crie o `app.py`:

```python
from flask import Flask, render_template

app = Flask(__name__)

tarefas = [
    {"id": 1, "titulo": "Escrever artigo", "concluida": True},
    {"id": 2, "titulo": "Estudar Flask", "concluida": False},
    {"id": 3, "titulo": "Revisar código", "concluida": False},
]


@app.route("/")
def index():
    return render_template("index.html", tarefas=tarefas)
```

Agora crie o template `templates/index.html`:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <title>Minhas tarefas</title>
</head>
<body>
    <h1>Minhas tarefas</h1>
    <ul>
        {% for tarefa in tarefas %}
        <li>{{ tarefa.titulo }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

Rode com `python app.py` e acesse `http://localhost:5000/`. A página mostra a lista de tarefas. Repare nos blocos especiais do Jinja2:

- `{% ... %}` executa lógica (laços, condições);
- `{{ ... }}` imprime o valor de uma variável.

## Condicionais

Para marcar as tarefas concluídas, use um `if`:

```html
<ul>
    {% for tarefa in tarefas %}
    <li>
        {{ tarefa.titulo }}
        {% if tarefa.concluida %}
        <strong>(concluída)</strong>
        {% else %}
        <em>(pendente)</em>
        {% endif %}
    </li>
    {% endfor %}
</ul>
```

## Herança de layouts: não repita HTML

Você não quer copiar a estrutura do `<html>` para cada página. O Jinja2 resolve isso com **herança de templates**. Crie o layout base `templates/base.html`:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="utf-8">
    <title>{% block titulo %}Meu site{% endblock %}</title>
</head>
<body>
    <header>
        <nav>
            <a href="{{ url_for('index') }}">Início</a>
            <a href="{{ url_for('sobre') }}">Sobre</a>
        </nav>
    </header>
    <main>
        {% block conteudo %}{% endblock %}
    </main>
</body>
</html>
```

Veja duas novidades:

- `{% block ... %}` define uma área que cada página pode preencher;
- `{{ url_for('index') }}` gera a URL de uma rota a partir do nome da função, evitando URLs "na mão".

Agora a página de tarefas pode ser escrita apenas com o conteúdo:

```html
{% extends "base.html" %}

{% block titulo %}Minhas tarefas{% endblock %}

{% block conteudo %}
<h1>Minhas tarefas</h1>
<ul>
    {% for tarefa in tarefas %}
    <li>{{ tarefa.titulo }}</li>
    {% endfor %}
</ul>
{% endblock %}
```

E uma página "Sobre" reutiliza o mesmo layout:

```html
{% extends "base.html" %}

{% block titulo %}Sobre{% endblock %}

{% block conteudo %}
<h1>Sobre nós</h1>
<p>Somos a comunidade de Python de São Marcos.</p>
{% endblock %}
```

No `app.py`, adicione a rota:

```python
@app.route("/sobre")
def sobre():
    return render_template("sobre.html")
```

Agora as duas páginas compartilham a mesma estrutura e o mesmo menu. Qualquer mudança no layout base reflete em todas as páginas de uma vez.

## Recebendo dados de formulários

O Jinja2 também serve para montar formulários. Crie o template `templates/nova.html`:

```html
{% extends "base.html" %}

{% block conteudo %}
<h1>Nova tarefa</h1>
<form method="POST">
    <label for="titulo">Título:</label>
    <input type="text" name="titulo" id="titulo" required>
    <button type="submit">Salvar</button>
</form>
{% endblock %}
```

E a rota que recebe o formulário. No Flask, formulários usam os métodos **GET** (mostrar o formulário) e **POST** (receber os dados):

```python
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = []


@app.route("/nova", methods=["GET", "POST"])
def nova_tarefa():
    if request.method == "POST":
        titulo = request.form.get("titulo", "")
        tarefas.append({"id": len(tarefas) + 1, "titulo": titulo})
        return redirect(url_for("index"))
    return render_template("nova.html")
```

O `redirect` redireciona o navegador de volta para a lista de tarefas, uma boa prática para evitar que o formulário seja reenviado ao atualizar a página.

## Juntando tudo

Você agora tem os três pilares de uma aplicação web clássica:

- **Python (Flask)** — controla a lógica e as rotas;
- **Jinja2** — gera as páginas HTML dinamicamente;
- **Banco de dados** — guarda os dados de forma permanente (veja nosso [artigo sobre SQLite com Flask]({filename}flask-com-banco-de-dados-sqlite.md)).

## Próximos passos

Com essas bases você pode explorar:

- **CSS e JavaScript** para estilizar e dar interatividade às páginas;
- **Validação de formulários** e mensagens de erro amigáveis;
- **Sessões** para controle de login;
- O **Django**, que traz essa estrutura toda pronta e empacotada.

Transformar dados em páginas é o coração da web, e o Python faz isso de forma surpreendentemente simples.

Tem alguma página que gostaria de construir? Compartilhe nos comentários ou contribua com um artigo no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
