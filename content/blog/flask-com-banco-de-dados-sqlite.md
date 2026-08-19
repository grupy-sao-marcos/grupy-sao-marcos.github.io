Title: Flask com banco de dados: sua API com SQLite na prática
Date: 2026-08-19 09:00
Modified: 2026-08-19 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Evolua sua API Flask guardando os dados em um banco SQLite, usando SQL puro, sem dependências extras.

No [artigo anterior]({filename}sua-primeira-api-flask.md) criamos uma API de tarefas onde os dados eram guardados em uma lista em memória. Isso funciona enquanto o servidor está no ar, mas basta reiniciar o programa e **tudo se perde**.

A solução é usar um banco de dados. Neste artigo vamos usar o **SQLite**, que já vem embutido no Python — sem precisar instalar nada além do Flask.

## Por que SQLite?

O SQLite é um banco de dados em arquivo único, leve e que não precisa de servidor rodando. É perfeito para aprender, para aplicações pequenas e até para protótipos. Depois, quando a aplicação crescer, a troca para um banco como o PostgreSQL é tranquila.

## Criando a estrutura

Vamos manter a mesma API de tarefas do artigo anterior, mas agora com uma tabela no banco. Crie o arquivo `app.py`:

```python
import sqlite3

from flask import Flask, g, jsonify, request

app = Flask(__name__)
DB_PATH = "tarefas.db"


def conectar_banco():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def fechar_conexao(erro):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def criar_tabela():
    with app.app_context():
        db = conectar_banco()
        db.execute("""
            CREATE TABLE IF NOT EXISTS tarefas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                concluida INTEGER NOT NULL DEFAULT 0
            )
        """)
        db.commit()


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    db = conectar_banco()
    linhas = db.execute("SELECT * FROM tarefas").fetchall()
    return jsonify([dict(linha) for linha in linhas])
```

Antes de explicar o código, vamos olhar para dois detalhes importantes:

- `g` é um objeto do Flask que guarda dados durante a requisição. Usamos ele para abrir **uma** conexão por requisição;
- `@app.teardown_appcontext` garante que a conexão seja fechada ao final de cada requisição, evitando vazamento de recursos.

Agora vamos criar as demais rotas. Primeiro o `POST`, para criar tarefas:

```python
@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = request.get_json()
    db = conectar_banco()

    cursor = db.execute(
        "INSERT INTO tarefas (titulo) VALUES (?)",
        (dados.get("titulo", ""),),
    )
    db.commit()

    tarefa = db.execute(
        "SELECT * FROM tarefas WHERE id = ?", (cursor.lastrowid,)
    ).fetchone()
    return jsonify(dict(tarefa)), 201
```

Perceba o `?` no comando SQL: é um **placeholder** de parâmetro. Nunca monte consultas com concatenação de strings, pois isso abre brecha para **SQL injection**:

```python
# ERRADO e perigoso:
db.execute(f"SELECT * FROM tarefas WHERE titulo = '{dados['titulo']}'")
```

Sempre use os placeholders. Essa simples prática evita uma das vulnerabilidades mais comuns em aplicações web.

## Atualizando e deletando

Para atualizar e remover tarefas, a lógica é parecida:

```python
@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefa(tarefa_id):
    dados = request.get_json()
    db = conectar_banco()

    db.execute(
        "UPDATE tarefas SET titulo = ?, concluida = ? WHERE id = ?",
        (
            dados.get("titulo", ""),
            int(dados.get("concluida", False)),
            tarefa_id,
        ),
    )
    db.commit()

    tarefa = db.execute(
        "SELECT * FROM tarefas WHERE id = ?", (tarefa_id,)
    ).fetchone()
    if tarefa is None:
        return jsonify({"erro": "Tarefa não encontrada"}), 404
    return jsonify(dict(tarefa))


@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def deletar_tarefa(tarefa_id):
    db = conectar_banco()
    db.execute("DELETE FROM tarefas WHERE id = ?", (tarefa_id,))
    db.commit()
    return "", 204
```

## Rodando a aplicação

No final do arquivo, adicione a criação da tabela e o start do servidor:

```python
if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)
```

Rode com:

```bash
python app.py
```

## Testando a persistência

Vamos criar uma tarefa e reiniciar o servidor para provar que os dados sobrevivem:

```bash
curl -X POST http://localhost:5000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Estudar banco de dados"}'
```

Agora **pare o servidor** (Ctrl+C) e rode `python app.py` novamente:

```bash
curl http://localhost:5000/tarefas
```

A tarefa ainda está lá. O arquivo `tarefas.db` foi criado na pasta do projeto e é ele quem guarda os dados.

## Dica: visualize o banco

Você pode inspecionar o conteúdo do banco direto no terminal:

```bash
sqlite3 tarefas.db "SELECT * FROM tarefas;"
```

## Próximos passos

Você já tem uma API funcional com dados persistidos usando apenas a biblioteca padrão! A partir daqui pode evoluir para:

- **Validação** dos dados recebidos nas requisições;
- Um **ORM** como o SQLAlchemy, que escreve o SQL por você;
- **Migrações** de banco de dados;
- Migrar para **PostgreSQL** em produção.

No próximo artigo vamos dar um passo atrás e aprender a gerar **páginas HTML** com Flask e o motor de templates **Jinja2**, transformando sua API em um site de verdade.

Gostou do conteúdo? Deixe seu comentário ou contribua com um artigo no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
