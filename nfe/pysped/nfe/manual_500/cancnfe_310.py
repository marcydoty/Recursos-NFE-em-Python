# -*- coding: utf-8 -*-

import os

from nfe.pysped.nfe.manual_401 import cancnfe_200
from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manual_500 import ESQUEMA_ATUAL


DIRNAME = os.path.dirname(__file__)


class InfCancEnviado(cancnfe_200.InfCancEnviado):
    def __init__(self):
        super(InfCancEnviado, self).__init__()


class CancNFe(cancnfe_200.CancNFe):
    def __init__(self):
        super(CancNFe, self).__init__()
        self.versao    = TagDecimal(nome=u'cancNFe', codigo=u'CP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.infCanc   = InfCancEnviado()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'cancNFe_v3.10.xsd'


class InfCancRecebido(cancnfe_200.InfCancRecebido):
    def __init__(self):
        super(InfCancRecebido, self).__init__()


class RetCancNFe(cancnfe_200.RetCancNFe):
    def __init__(self):
        super(RetCancNFe, self).__init__()
        self.versao = TagDecimal(nome=u'retCancNFe', codigo=u'CR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.infCanc = InfCancRecebido()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retCancNFe_v3.10.xsd'


class ProcCancNFe(cancnfe_200.ProcCancNFe):
    def __init__(self):
        super(ProcCancNFe, self).__init__()
        #
        # Atenção --- a tag procCancNFe tem que começar com letra minúscula, para
        # poder validar no XSD.
        #
        self.versao = TagDecimal(nome=u'procCancNFe', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.cancNFe = CancNFe()
        self.retCancNFe = RetCancNFe()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'procCancNFe_v3.10.xsd'
