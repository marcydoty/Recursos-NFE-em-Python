# -*- coding: utf-8 -*-

import os
from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manual_401 import inutnfe_200
from nfe.pysped.nfe.manual_500 import ESQUEMA_ATUAL


DIRNAME = os.path.dirname(__file__)


class InfInutEnviado(inutnfe_200.InfInutEnviado):
    def __init__(self):
        super(InfInutEnviado, self).__init__()
        self.Id     = TagCaracter(nome=u'infInut', codigo=u'DP03', tamanho=[43, 43] , raiz=u'//inutNFe', propriedade=u'Id')


class InutNFe(inutnfe_200.InutNFe):
    def __init__(self):
        super(InutNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'inutNFe', codigo=u'DP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.infInut = InfInutEnviado()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'inutNFe_v3.10.xsd'

class InfInutRecebido(inutnfe_200.InfInutRecebido):
    def __init__(self):
        super(InfInutRecebido, self).__init__()
        self.dhRecbto = TagDataHoraUTC(nome=u'dhRecbto' , codigo=u'DR16', raiz=u'//retInutNFe/infInut',obrigatorio=False)



class RetInutNFe(inutnfe_200.RetInutNFe):
    def __init__(self):
        super(RetInutNFe, self).__init__()
        self.versao = TagDecimal(nome=u'retInutNFe', codigo=u'DR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.infInut = InfInutRecebido()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retInutNFe_v3.10.xsd'



class ProcInutNFe(inutnfe_200.ProcInutNFe):
    def __init__(self):
        super(ProcInutNFe, self).__init__()
        #
        # Atenção --- a tag ProcInutNFe tem que começar com letra maiúscula, para
        # poder validar no XSD. Os outros arquivos proc, procCancNFe, e procNFe
        # começam com minúscula mesmo
        #
        self.versao = TagDecimal(nome=u'ProcInutNFe', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.inutNFe = InutNFe()
        self.retInutNFe = RetInutNFe()

        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'procInutNFe_v3.10.xsd'

