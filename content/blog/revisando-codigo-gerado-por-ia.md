Title: Programando com IA: um checklist para revisar o código gerado
Date: 2026-11-09 09:00
Modified: 2026-11-09 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Assistentes de IA aceleram muito o desenvolvimento, mas o código gerado ainda é sua responsabilidade. Veja um checklist simples para revisá-lo.

No 11° encontro, a palestra **Desenvolvimento 100% IA, riscos e facilidades** rendeu uma ótima conversa: a IA escreve código rápido, mas quem coloca em produção (e quem responde pelos bugs) é você. Aqui vai um checklist curto para revisar o que a IA entrega.

## 1. Você entende o que o código faz?

Se você não consegue explicar o código para um colega, não faça commit dele. Peça para a IA explicar, leia a documentação, rode por partes.

## 2. As bibliotecas existem mesmo?

A IA às vezes sugere pacotes ou funções que não existem, ou que têm nome parecido com um pacote verdadeiro. Antes de um `pip install`, confira o pacote no [PyPI](https://pypi.org) e veja se ele é mantido.

## 3. Tem testes?

Peça os testes junto com o código, ou escreva você mesmo. Um teste simples com `pytest` já pega muita coisa:

```python
from minha_app import calcular_desconto


def test_desconto_nao_fica_negativo():
    assert calcular_desconto(valor=10, percentual=150) >= 0
```

Teste principalmente os **casos de borda**: lista vazia, valor zero, texto com acento, arquivo que não existe.

## 4. Segurança

Fique atento a:

- Senhas e chaves escritas direto no código;
- SQL montado com f-string (use parâmetros, como `cursor.execute("... WHERE id = ?", (id,))`);
- Dados do usuário usados sem validação.

## 5. Combina com o resto do projeto?

O código gerado segue o padrão do projeto, usa as mesmas bibliotecas e o mesmo estilo? Rode o linter e o formatador:

```bash
pip install ruff
ruff check .
ruff format .
```

## Dica final

Trate a IA como um colega muito rápido, mas que acabou de chegar no projeto: ela ajuda bastante, mas tudo que ela entrega precisa de revisão.

Tem dicas próprias? Compartilhe com a comunidade no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
