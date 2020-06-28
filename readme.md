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

## Token

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

## Consultas em fontes de dados

Para se realizar consultas em fontes de dados, deve-se utilizar o método 'busca' da classe 'BthFontesDados'. Esse método recebe como entrada os parâmetros de forma semelhante a busca através do BFC (mais detalhes [aqui](http://test.betha.com.br/documentacao/bfc-script/2.16.X/index.html)).
Segue exemplo de utilização:

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

