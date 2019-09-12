# Exercício de Lógica
Fique avontade para fazer na linguagem que quiser.
Se tiver teste automatizado melhor inda. Tem um problema manda um pr.

Tem alguns arquivos com dados em massa

## 1 - Ordenação
Dada uma lista de candidatos/profissional. Queremos ordernar por:
- idade
- salário
- anos de experiência
- ordem alfabetica
- hierarquico (se anos de experiência for igual para todos então ordernar por idade)

A orderm padrão é ascendente porém deve ser possivel ordernar descendente para qualquer
filtro anterior

Um Cantidato tem os seguintes atributods
- id
- nome
- idade
- experiência
- salário


## 2 - Agrupamento
Dada uma matrix de itens, deixe items do mesmo grupo em um único item. A lista de entrada não deve ser alterada.
A ordem dos itens deve ser respeitada. Deixe apenas as proprieades group_id e itens na saída.
Mostre a matrix de entrada e saida.

Por exemplo:
Entrada
```js
[
    {
        "group_id": "x8jfu",
        "itens": [
            'xjfoeij',
            '145365',
            '8i3dcr2',
        ],
        'line': 1
    },
    {
        "group_id": "x8jfu",
        "itens": [
            'mki1d0'
            'duf36d'
        ],
        'line': 2
    },
    {
        "group_id": "uty28",
        "itens": [
            '8jfoejhf'
            '1449j387f',
            '839jkfu1',
        ],
        "line": 3
    }
]
```

Saída
```js
[
    {
        "group_id": "x8jfu",
        "itens": [
            "xjfoeij",
            "145365",
            "8i3dcr2",
            "mki1d0",
            "duf36d"
        ]
    },
    {
        "group_id": "uty28",
        "itens": [
            "8jfoejhf"
            "1449j387f",
            "839jkfu1"
        ]
    }
]
```


## 3 - Bulk insert
Você notou que fazer um insert por um no baco de dados demora muito
por isso você vai montar um insert de muitos por vez. (Bulk Insert)
Data uma lista de Pessoas (id, nome, idade) retornar uma lista de string
com o sql de insert equivalente (100 por vez - cada insert vai ter 100 Pessoas).
Lembrando que o último item não pode ter virgula.

A tabela é person, e as colunas são: id, name, age

Exemplo (2 por vez)
Entrada
```js
[
    {
        "id": "2",
        "name": "Nome test 1",
        "idade": 35,
    },
    {
        "id": "3",
        "name": "Nome test 3",
        "idade": 45,
    },
    {
        "id": "233",
        "name": "Nome test 4",
        "idade": 20,
    }
]
```

Saida
```js
[
    `
    INSERT INTO person (id, name, age) VALUES
    ('2', 'Nome test 1', 35),
    ('3', 'Nome test 3', 45)
    `,

    `
    INSERT INTO person (id, name, age) VALUES
    ('233', 'Nome test 4', 20)
    `
]
```


## 4 - Sincronizar arquivo no s3 com arquivo local
Dada uma bucket no s3 e uma key (path do arquivo no s3)
Sincronizar o arquivo do s3 com o arquivo localhost.
Se o arquivo no s3 é mais novo deve que baixar, caso contrario faz nada.
Use a propriedade LastModified tanto do s3 quanto do arquivo local.
E timezone UTC.
