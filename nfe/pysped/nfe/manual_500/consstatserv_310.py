# -*- coding: utf-8 -*-

import os

from nfe.pysped.nfe.manual_401 import consstatserv_200
from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manual_500 import ESQUEMA_ATUAL


DIRNAME = os.path.dirname(__file__)


class ConsStatServ(consstatserv_200.ConsStatServ):
    def __init__(self):
        super(ConsStatServ, self).__init__()
        self.versao = TagDecimal(nome=u'consStatServ', codigo=u'FP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'consStatServ_v3.10.xsd'


class RetConsStatServ(consstatserv_200.RetConsStatServ):
    def __init__(self):
        super(RetConsStatServ, self).__init__()
        self.versao    = TagDecimal(nome=u'retConsStatServ', codigo=u'FR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retConsStatServ_v3.10.xsd'
