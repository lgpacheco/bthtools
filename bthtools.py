import json
import requests
import re
from dotmap import DotMap


class BthFontesDados:
    # Constructor (Seta valores iniciais de parâmetros da classe)
    def __init__(self):
        self.p_token = ''
        self.p_timeout = 2000
        self.p_limit = 100
        self.dadosToken = {}
        self.dadosEntidade = {}
        self.useDotmap = True

    # Retorna o valor do token em uso
    def getToken(self):
        return self.p_token

    # Retorna o valor do token em uso
    def getDadosToken(self):
        if self.dadosToken == {} and self.p_token != '':
            self.gerarDadosToken(self.p_token)
        return self.dadosToken

    # Seta o valor para token genérico da classe
    def setToken(self, n):
        self.p_token = n
        self.dadosToken = self.gerarDadosToken(n)

    # Seta valor de timeout das requisições
    def setTimeout(self, n):
        self.p_timeout = n

    # Seta valor de limite de dados (paginação) das requisições
    def setLimit(self, n):
        self.p_limit = n

    # Define se os resultados das requisições serão retornados com uso do DotMap
    def setDotmap(self, n):
        self.useDotmap = n

    # Retorna o valor dos dados da entidade
    def getDadosEntidade(self):
        if self.dadosEntidade == {}:
            self.gerarDadosEntidade()
        return self.dadosEntidade

    # Busca endereço da fonte desejado no JSON local de ativos
    def getUrlFonteBetha(self, args):
        r = {'status': 0, 'url': ''}
        try:
            with open('bthDS.json') as json_file:
                data = json.load(json_file)
                for i in data:
                    if i['identificador'] == args['sistema']:
                        for j in i['ativos']:
                            if j['tema'] == args['fonte'] and j['tipoOperacao']['value'] == 'L':
                                if 'hostExterno' in i and 'endereco' in j:
                                    r = {'status': 1, 'url': (i['hostExterno'] + j['endereco'])}
                                break
        except:
            print('Falha ao executar função "getUrlFonteBetha"')
        return r

    # Consulta dados do token ativo
    def gerarDadosToken(self, token):
        r = {'status': 0}
        try:
            url = "https://oauth.cloud.betha.com.br/auth/oauth2/tokeninfo"
            params = {'access_token': self.p_token}
            r = requests.get(url=url, params=params)
            data = r.json()
            r = {
                 'status': 1,
                 'expired': re.search("(?<=expired\'\: )(False|True)", str(data)).group(),
                 'database': re.search("(?<=databaseId\" \: \")(\d+)(?!=\")", str(data)).group(),
                 'entity': re.search("(?<=entityId\" \: \")(\d+)(?!=\")", str(data)).group()
                 }
        except:
            print(f'Falha ao consultar dados para o token {self.p_token}')
        return r

    # Busca informações da entidade vinculado ao token
    def gerarDadosEntidade(self):
        url = f'https://contabilidade-fontes-dados.cloud.betha.com.br/contabilidade/fontes-dados/contabil/entidades-ctb?fields=id, nome, cnpj, descricaoNatureza&filter=id={self.dadosToken["entity"]}'
        headers = {'authorization': f'bearer {self.p_token}'}
        r = requests.get(url=url, headers=headers, timeout=self.p_timeout)
        data = r.json()['content']
        self.dadosEntidade = {
            'id': data[0]['id'],
            'nome': data[0]['nome'],
            'cnpj': data[0]['cnpj'],
            'natureza': data[0]['descricaoNatureza']
        }

    # Busca os dados na fonte conforme parâmetros de entrada
    def busca(self, args):
        retBusca = []
        hasNext = True
        url = self.getUrlFonteBetha({'sistema': args['sistema'], 'fonte': args['fonte']})['url']
        params = {'offset': 0, 'limit': self.p_limit}
        if 'token' in args:
            headers = {'authorization': f'bearer {args["token"]}'}
        else:
            if self.p_token == '':
                print('Não foi especificado um token .')
                return {}
            else:
                headers = {'authorization': f'bearer {self.p_token}'}
        if 'campos' in args:
            params['fields'] = args['campos']
        if 'criterio' in args:
            params['filter'] = args['criterio']
        if 'ordenacao' in args:
            params['sort'] = args['ordenacao']
        if 'parametros' in args:
            for p in args['parametros']:
                url = url.replace("{" + p + "}", str(args['parametros'][p]))
        while hasNext:
            r = requests.get(url=url, params=params, headers=headers, timeout=self.p_timeout)
            data = r.json()
            if 'content' in data:
                for i in data['content']:
                    if self.useDotmap:
                        retBusca.append(DotMap(i))
                    else:
                        retBusca.append(i)
            params['offset'] += self.p_limit
            hasNext = str(data['hasNext']) == 'True'
        return retBusca
