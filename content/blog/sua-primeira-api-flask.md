Title: Sua primeira API com Flask: do zero ao primeiro endpoint
Date: 2026-08-16 09:00
Modified: 2026-08-16 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Crie sua primeira API REST usando Flask, aprenda o que são rotas, métodos HTTP e JSON, e teste seus endpoints no navegador.

Se você já conhece o básico de Python e quer dar os primeiros passos no mundo web, o [Flask](https://flask.palletsprojects.com/) é uma ótima porta de entrada. Ele é leve, simples e você consegue criar sua primeira API em poucos minutos.

Neste artigo vamos construir uma API de tarefas (a clássica *todo list*) usando JSON.

## Preparando o ambiente

Antes de começar, crie um ambiente virtual (se tiver dúvidas, veja nosso [artigo sobre ambientes virtuais]({filename}virtual-env.md)) e instale o Flask:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install flask
```

## Criando a aplicação

Crie um arquivo chamado `app.py` com o seguinte conteúdo:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = []
proximo_id = 1

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

if __name__ == "__main__":
    app.run(debug=True)
```

Para rodar, execute:

```bash
python app.py
```

Acesse `http://localhost:5000/tarefas` no navegador. Você verá uma lista vazia `[]`. Pronto, sua primeira API está no ar!

## O que acabamos de fazer?

Vamos entender as peças desse código:

- `@app.route("/tarefas", methods=["GET"])` registra uma **rota**: quando alguém acessar `/tarefas`, a função abaixo será executada.
- `methods=["GET"]` define o **método HTTP** aceito. O `GET` é usado para consultar informações.
- `jsonify` transforma um objeto Python (como uma lista) em JSON, o formato usado para trocar dados entre aplicações.

## Adicionando novas tarefas

Uma API não serve apenas para consultar, ela também deve permitir **criar**, **atualizar** e **deletar** informações. Para isso usamos os métodos HTTP:

| Método | Ação                          | URL          |
|--------|-------------------------------|--------------|
| GET    | listar tarefas                | /tarefas     |
| POST   | criar uma nova tarefa         | /tarefas     |
| GET    | ver uma tarefa específica     | /tarefas/1   |
| PUT    | atualizar uma tarefa          | /tarefas/1   |
| DELETE | remover uma tarefa            | /tarefas/1   |

Vamos adicionar a rota de criação:

```python
@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    global proximo_id
    dados = request.get_json()

    nova_tarefa = {
        "id": proximo_id,
        "titulo": dados.get("titulo", ""),
        "concluida": False,
    }
    tarefas.append(nova_tarefa)
    proximo_id += 1

    return jsonify(nova_tarefa), 201
```

O `201` no `return` é o código HTTP de **Created**, indicando que o recurso foi criado com sucesso.

## Testando com curl

Para enviar uma requisição `POST` com dados, usamos o `curl` no terminal:

```bash
curl -X POST http://localhost:5000/tarefas \
  -H "Content-Type: application/json" \
  -d '{"titulo": "Escrever artigo do blog"}'
```

Você deve receber como resposta:

```json
{
  "id": 1,
  "titulo": "Escrever artigo do blog",
  "concluida": false
}
```

## Consultando e atualizando uma tarefa

Agora vamos implementar as rotas para uma tarefa específica:

```python
def encontrar_tarefa(tarefa_id):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            return tarefa
    return None

@app.route("/tarefas/<int:tarefa_id>", methods=["GET"])
def ver_tarefa(tarefa_id):
    tarefa = encontrar_tarefa(tarefa_id)
    if tarefa is None:
        return jsonify({"erro": "Tarefa nao encontrada"}), 404
    return jsonify(tarefa)

@app.route("/tarefas/<int:tarefa_id>", methods=["PUT"])
def atualizar_tarefa(tarefa_id):
    tarefa = encontrar_tarefa(tarefa_id)
    if tarefa is None:
        return jsonify({"erro": "Tarefa nao encontrada"}), 404

    dados = request.get_json()
    tarefa["titulo"] = dados.get("titulo", tarefa["titulo"])
    tarefa["concluida"] = dados.get("concluida", tarefa["concluida"])
    return jsonify(tarefa)
```

Note o uso de `<int:tarefa_id>` na rota: o Flask converte o trecho da URL em um inteiro e o passa como argumento para a função.

Para deletar, criamos a última rota:

```python
@app.route("/tarefas/<int:tarefa_id>", methods=["DELETE"])
def deletar_tarefa(tarefa_id):
    global tarefas
    tarefas = [t for t in tarefas if t["id"] != tarefa_id]
    return "", 204
```

O código `204` significa **No Content**: a operação funcionou, mas não há nada para retornar.

## Teste completo da sua API

```bash
# criar duas tarefas
curl -X POST http://localhost:5000/tarefas -H "Content-Type: application/json" -d '{"titulo": "Estudar Flask"}'
curl -X POST http://localhost:5000/tarefas -H "Content-Type: application/json" -d '{"titulo": "Estudar Docker"}'

# listar todas
curl http://localhost:5000/tarefas

# atualizar a tarefa 1
curl -X PUT http://localhost:5000/tarefas/1 -H "Content-Type: application/json" -d '{"concluida": true}'

# deletar a tarefa 2
curl -X DELETE http://localhost:5000/tarefas/2
```

## Próximos passos

A partir daqui o caminho é longo e divertido:

- **Conectar a um banco de dados** para os dados não se perderem ao reiniciar o servidor;
- **Organizar o código** em módulos e usar *blueprints*;
- **Adicionar validação** nos dados recebidos;
- Conhecer outros frameworks como o **FastAPI** e o **Django**.

O Flask é perfeito para começar, pois ele não impõe estrutura e deixa você aprender cada conceito aos poucos. Em breve traremos um artigo mostrando como integrar sua API a um banco de dados.

Gostou? Compartilhe com a comunidade e envie sua versão da API no nosso [repositorio](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
