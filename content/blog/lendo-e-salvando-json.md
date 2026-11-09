Title: Lendo e salvando JSON em Python
Date: 2026-11-07 09:00
Modified: 2026-11-07 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Entenda como converter dados Python para JSON e vice-versa, e como ler e salvar arquivos JSON com o módulo nativo json.

O **JSON** é o formato mais usado para trocar dados entre sistemas: APIs, arquivos de configuração, integrações. E o Python já vem com o módulo `json` para trabalhar com ele.

## Do Python para JSON

O `json.dumps` transforma dicionários e listas em texto JSON:

```python
import json

usuario = {"nome": "João", "idade": 28, "ativo": True, "cursos": ["Python", "Git"]}

texto = json.dumps(usuario, ensure_ascii=False, indent=2)
print(texto)
```

```json
{
  "nome": "João",
  "idade": 28,
  "ativo": true,
  "cursos": [
    "Python",
    "Git"
  ]
}
```

Repare que o `True` do Python virou `true` no JSON. O `ensure_ascii=False` mantém os acentos legíveis, e o `indent=2` deixa tudo formatado.

## Do JSON para Python

O caminho contrário é o `json.loads`:

```python
texto = '{"nome": "Maria", "idade": 31}'
dados = json.loads(texto)

print(dados["nome"])  # Maria
print(type(dados))    # <class 'dict'>
```

## Salvando em arquivo

Para arquivos, use `json.dump` e `json.load` (sem o "s"):

```python
with open("usuario.json", "w", encoding="utf-8") as arquivo:
    json.dump(usuario, arquivo, ensure_ascii=False, indent=2)

with open("usuario.json", encoding="utf-8") as arquivo:
    carregado = json.load(arquivo)

print(carregado["cursos"])  # ['Python', 'Git']
```

Uma forma de lembrar: o "s" de `dumps` e `loads` vem de **string**.

## Tratando JSON inválido

Dados que vêm de fora podem estar quebrados. Proteja seu código:

```python
texto = '{"nome": "Maria",}'  # vírgula sobrando

try:
    dados = json.loads(texto)
except json.JSONDecodeError as erro:
    print(f"JSON inválido: {erro}")
```

## Cuidado com tipos que o JSON não conhece

Datas, por exemplo, não existem em JSON. Converta para texto antes:

```python
from datetime import date

evento = {"nome": "Grupy", "data": date(2026, 11, 21).isoformat()}
print(json.dumps(evento))  # {"nome": "Grupy", "data": "2026-11-21"}
```

## Dica final

Use sempre `encoding="utf-8"` ao abrir arquivos e `ensure_ascii=False` ao salvar: assim seus acentos ficam corretos em qualquer sistema.

Contribua com novos artigos no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
