Title: Trabalhando com datas em Python usando datetime
Date: 2026-11-03 09:00
Modified: 2026-11-03 09:00
Category: Blog
Authors: Perceu Bertoletti
Summary: Aprenda a criar, formatar, converter e fazer contas com datas em Python usando o módulo datetime.

Prazo de entrega, data de vencimento, idade de um cliente: datas aparecem em praticamente todo sistema. O Python já traz o módulo `datetime` para lidar com elas.

## Data e hora atuais

```python
from datetime import date, datetime

print(date.today())    # 2026-11-03
print(datetime.now())  # 2026-11-03 09:00:00.123456
```

## Formatando para o padrão brasileiro

O método `strftime` transforma a data em texto:

```python
agora = datetime.now()
print(agora.strftime("%d/%m/%Y %H:%M"))  # 03/11/2026 09:00
```

Os códigos mais usados: `%d` dia, `%m` mês, `%Y` ano, `%H` hora e `%M` minuto.

## Convertendo texto em data

O caminho contrário é o `strptime`, muito usado ao ler dados de planilhas e formulários:

```python
texto = "21/11/2026"
data = datetime.strptime(texto, "%d/%m/%Y").date()
print(data)  # 2026-11-21
```

## Fazendo contas com timedelta

```python
from datetime import timedelta

hoje = date(2026, 11, 3)

print(hoje + timedelta(days=30))  # 2026-12-03

evento = date(2026, 11, 21)
faltam = evento - hoje
print(f"Faltam {faltam.days} dias para o evento")  # Faltam 18 dias para o evento
```

## Calculando a idade

```python
def calcular_idade(nascimento: date, hoje: date) -> int:
    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    return idade


print(calcular_idade(date(1995, 12, 10), date(2026, 11, 3)))  # 30
```

O truque é comparar as tuplas `(mês, dia)`: se o aniversário ainda não chegou neste ano, desconta um.

## Dica final

Guarde datas sempre como objetos `date`/`datetime` e só converta para texto na hora de mostrar. Comparar e ordenar strings como `"03/11/2026"` é receita para bug.

Sugira temas ou contribua no nosso [repositório](https://github.com/grupy-sao-marcos/grupy-sao-marcos.github.io).
