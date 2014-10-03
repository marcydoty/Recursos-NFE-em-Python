# -*- coding: utf-8 -*-

import os

from nfe.pysped.nfe.manual_401 import consrecinfe_200
from nfe.pysped.nfe.manual_500 import ESQUEMA_ATUAL
from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manual_401.nfe_200 import NFe
DIRNAME = os.path.dirname(__file__)


class ConsReciNFe(consrecinfe_200.ConsReciNFe):
    def __init__(self):
        super(ConsReciNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'consReciNFe', codigo=u'BP02', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'consReciNFe_v3.10.xsd'


class InfProt(consrecinfe_200.InfProt):
    def __init__(self):
        super(InfProt, self).__init__()


class ProtNFe(consrecinfe_200.ProtNFe):
    def __init__(self):
        super(ProtNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'protNFe', codigo=u'PR02' , propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')


class RetConsReciNFe(consrecinfe_200.RetConsReciNFe):
    def __init__(self):
        super(RetConsReciNFe, self).__init__()
        self.versao   = TagDecimal(nome=u'retConsReciNFe', codigo=u'BR02' , propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retConsReciNFe_v3.10.xsd'


class ProcNFe(consrecinfe_200.ProcNFe):
    def __init__(self):
        super(ProcNFe, self).__init__()
        self.versao  = TagDecimal(nome=u'nfeProc', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.NFe     = NFe()
        self.protNFe = ProtNFe()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'procNFe_v3.10.xsd'
