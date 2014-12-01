# -*- coding: utf-8 -*-


import os

from nfe.pysped.nfe.manual_401 import soap_200
from nfe.pysped.xml_sped import *

DIRNAME = os.path.dirname(__file__)


class NFeCabecMsg(soap_200.NFeCabecMsg):
    def __init__(self):
        super(NFeCabecMsg, self).__init__()
        self.versaoDados = TagDecimal(nome=u'versaoDados', codigo=u'', raiz=u'//cabecMsg', tamanho=[1, 4], valor=u'3.10')


class NFeDadosMsg(soap_200.NFeDadosMsg):
    def __init__(self):
        super(NFeDadosMsg, self).__init__()


class SOAPEnvio(soap_200.SOAPEnvio):
    def __init__(self):
        super(SOAPEnvio, self).__init__()


class SOAPRetorno(soap_200.SOAPRetorno):
    def __init__(self):
        super(SOAPRetorno, self).__init__()

