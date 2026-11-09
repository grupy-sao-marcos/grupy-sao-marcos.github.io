Title: Troque o print pelo logging: o primeiro passo para monitorar sua aplicação
Date: 2026-11-04 09:00
Modified: 2026-11-04 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda a usar o módulo logging do Python para registrar o que sua aplicação faz e descobrir problemas antes dos seus usuários.

No 11° encontro a palestra **Monitorar nunca foi o problema** mostrou que o difícil não é coletar informação, e sim coletar a informação **certa**. E tudo começa por algo simples: parar de usar `print` para depurar.

## Por que não o print?

O `print` não diz **quando** algo aconteceu, nem **onde**, nem **quão grave** foi. E na hora de colocar em produção, você precisa sair caçando e apagando cada um deles.

## O básico do logging

O módulo `logging` já vem com o Python:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)

logger = logging.getLogger(__name__)

logger.info("Aplicação iniciada")
logger.warning("Estoque baixo para o produto %s", "café")
```

Saída:

```
2026-11-04 09:00:00,123 [INFO] __main__: Aplicação iniciada
2026-11-04 09:00:00,124 [WARNING] __main__: Estoque baixo para o produto café
```

## Os níveis de log

Do menos ao mais grave:

- `DEBUG`: detalhes para quem está desenvolvendo;
- `INFO`: o que é esperado acontecer;
- `WARNING`: algo estranho, mas o programa segue;
- `ERROR`: algo falhou;
- `CRITICAL`: a aplicação pode parar.

Basta mudar o `level` para controlar o que aparece, sem apagar nenhuma linha do código.

## Registrando exceções

Dentro de um `except`, use `logger.exception`, que guarda a mensagem **e** o traceback completo:

```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    logger.exception("Falha ao calcular o resultado")
```

## Salvando em arquivo

```python
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
```

## Dica final

Logue **eventos que importam** (um pedido criado, um pagamento recusado, uma integração que caiu) com informações que ajudem a investigar. Log demais vira ruído; log de menos vira mistério.

Quer se aprofundar no tema? Fique de olho nos nossos [eventos](/) e contribua no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
