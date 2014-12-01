# -*- coding: utf-8 -*-

import os

from nfe.pysped.nfe.manual_401 import envinfe_200
from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manual_500 import ESQUEMA_ATUAL
from nfe_310 import NFe
DIRNAME = os.path.dirname(__file__)


class EnviNFe(envinfe_200.EnviNFe):
    def __init__(self):
        super(EnviNFe, self).__init__()

        self.versao  = TagDecimal(nome=u'enviNFe', codigo=u'AP02', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.indSinc  = TagInteiro(nome=u'indSinc' , codigo=u'AP03a', tamanho=[1, 1, 1], raiz=u'//enviNFe',valor=0)

        self.arquivo_esquema = u'enviNFe_v3.10.xsd'
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml
        xml += self.indSinc.xml

        for n in self.NFe:
            xml += tira_abertura(n.xml)

        xml += u'</enviNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.idLote.xml = arquivo
            self.indSinc.xml = arquivo
            self.NFe = self.le_grupo('//enviLote/NFe', NFe)

        return self.xml

    xml = property(get_xml, set_xml)

class InfRec(envinfe_200.InfRec):
    def __init__(self):
        super(InfRec, self).__init__()


class RetEnviNFe(envinfe_200.RetEnviNFe):
    def __init__(self):
        super(RetEnviNFe, self).__init__()
        self.versao   = TagDecimal(nome=u'retEnviNFe', codigo=u'AR02' , propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.dhRecbto = TagDataHoraUTC(nome=u'dhRecbto' , codigo=u'AR06b'                        , raiz=u'//retEnviNFe')
        self.infRec   = InfRec()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retEnviNFe_v3.10.xsd'
