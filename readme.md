# BthTools

`BthTools` é uma biblioteca que oferece recursos para integração de sistemas da suíte Betha Cloud com aplicações desenvolvidas em python.

* Leitura de fontes de dados
* Verificação e validação de tokens
* Interação com service layer

### Instalação
```
pip3 install bthtools
```

### Atualização
Obtém a versão mais atual da biblioteca.
```
pip3 install --upgrade bthtools
```

## Utilização

O primeiro passo para utilização da biblioteca é realizar a importação no arquivo do projeto. Para isso, basta inserir a seguinte linha de código no início do projeto:

``` python
from bthtools import *
```

Feito isso, já é possível instanciar as classes da biblioteca e começar a utiliza-las.

## Operações com Token

Para utilizar qualquer uma das classes de consulta, é necessário apontar para a classe o token de serviço que dará autorização para utilizar os serviços Betha.
A utilização desses método não é obrigatória, mas uma vez feito não é necessário informar o token em toda chamada subsequente.

### Setando um token padrão
 ``` python
bth.setToken('034453a8-xxxx-xxxx-xxxx-8403518f7199')
```

### Verificando o token configurado
 ``` python
bth.getToken()
```

### Verificando informações vinculadas ao token
 ``` python
bth.getDadosToken()
```

### Verifica informações de entidade vinculada ao token
 ``` python
bth.getDadosEntidade()
```

## Consultas em fontes de dados

Para se realizar consultas em fontes de dados, deve-se utilizar o método 'busca' da classe 'BthFontesDados'. Esse método recebe como entrada os parâmetros de forma semelhante a busca através do BFC (mais detalhes [aqui](http://test.betha.com.br/documentacao/bfc-script/2.16.X/index.html)).
Segue exemplo de utilização:

### Busca

 ``` python
from bthtools import *

bth = BthFontesDados()
dadosBusca = bth.busca({'token': '034453a8-xxxx-xxxx-xxxx-8403518f7199',
                        'sistema': 'contabilidade',
                        'fonte': 'empenhos',
                        'campos': 'numeroCadastro.numero, exercicio.ano',
                        'criterio': 'exercicio.ano = 2020'
                        })
for i in dadosBusca:
    print(f'{i.numeroCadastro.numero}/{i.exercicio.ano}')
```

### Consulta endereço de fonte de dados
 ``` python
from bthtools import *
bth = BthFontesDados()
printf(bth.getUrlFonteBetha({'sistema': 'contabilidade', 'fonte': 'empenhos' }))
```

## Demais configurações

### Timeout
Configura o timeout padrão das requisições realizadas pela classe nas API's da Betha.
 ``` python
bth.setTimeout(5000) # O valor padrão é 2000
```

### Limit
Configura a quantidade de informações obtidas por requisição, inflanciando na quantidade de paginações da fonte.
 ``` python
bth.setLimit(1000) # O valor padrão é 50
```

### DotMap
Especifica se a busca irá retornar um objeto DotMap ou Dict.
 ``` python
bth.setDotmap(False) # O valor padrão é True

# Exemplo de utilização de dados com o DotMap desligado, utilizando o retorno da busca como dicionário:
for i in dadosBusca:
    print(f'{i["numeroCadastro"]["numero"]}/{i["exercicio"]["ano"]}')
```

