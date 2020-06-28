# BthTools

[![Build Status](https://github.com/scoiak/bthtools](https://github.com/scoiak/bthtools)

# Instalação
```
pip3 install bthtools
```

## Atualização
Obtém a versão mais atual da biblioteca.
```
pip3 install --upgrade bthtools
```

# Recursos
`BthTools` é uma biblioteca que oferece recursos para integração de sistemas da suíte Betha Cloud com aplicações
desenvolvidas em python.

* Leitura de Fontes de Dados
* Verificação e validação de Tokens
* Interação com Service Layer

# Utilização

O primeiro passo para utilização da biblioteca é realizar a importação no arquivo do projeto. Para isso, basta inserir
a seguinte linha de código no início do projeto:

``` python
from bthtools import *
```

Feito isso, já é possível instanciar as classes da biblioteca e começar a utiliza-las.

# Token

Para utilizar qualquer uma das classes de consulta, é necessário apontar para a classe o token de serviço que dará
autorização para utilizar os serviços Betha. Segue exemplo abaixo de como setar o valor do token na classe:

 ``` python
 # Importando bliblioteca 'bthtools'
from bthtools import *

 # Criando instância da classe 'BthFontesDados'
bth = BthFontesDados()

# Setando o token de serviço na classe para utilização dos métodos de consulta
bth.setToken('034453a8-xxxx-xxxx-xxxx-8403518f7199')
```
