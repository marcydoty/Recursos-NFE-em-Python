# -*- coding: utf-8 -*-
__author__ = 'marcilene.ribeiro'


from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manifestacao_destinatario import ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)



class ConsNFeDest(XMLNFe):
    def __init__(self):
        super(ConsNFeDest, self).__init__()
        self.versao    = TagDecimal(nome=u'consNFeDest', codigo=u'IP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.01', raiz=u'/')
        self.tpAmb = TagInteiro(nome=u'tpAmb'   , codigo=u'IP03', tamanho=[ 1,  1, 1] , raiz=u'//consNFeDest')
        self.xServ =  TagCaracter(nome=u'xServ', codigo=u'IP04' , tamanho=[18, 18]     , raiz=u'//consNFeDest', valor=u'CONSULTAR NFE DEST')
        self.CNPJ = TagCaracter(nome=u'CNPJ'   , codigo=u'IP05' , tamanho=[ 0, 14]   , raiz=u'//consNFeDest')
        self.indNFe = TagInteiro(nome=u'indNFe', codigo=u'IP06' , tamanho=[1, 1, 1]     , raiz=u'//consNFeDest')
        self.indEmi = TagInteiro(nome=u'indEmi', codigo=u'IP07' , tamanho=[1, 1, 1]     , raiz=u'//consNFeDest')
        self.ultNSU = TagCaracter(nome=u'ultNSU', codigo=u'IP08' , tamanho=[1, 15]     , raiz=u'//consNFeDest')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'consNFeDest_v1.01.xsd'


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.CNPJ.xml
        xml += self.indNFe.xml
        xml += self.indEmi.xml
        xml += self.ultNSU.xml

        xml += u'</consNFeDest>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml = arquivo
            self.CNPJ.xml = arquivo
            self.indNFe.xml = arquivo
            self.indEmi.xml = arquivo
            self.ultNSU.xml = arquivo


    xml = property(get_xml, set_xml)


class ResCCe(XMLNFe):
    def __init__(self):
        super(ResCCe, self).__init__()
        self.NSU    = TagInteiro(nome=u'resCCe', codigo=u'IR39', tamanho=[1, 15]    , raiz=u'//ret', propriedade=u'NSU',obrigatorio=False)
        self.chNFe = TagCaracter(nome=u'chNFe'   , codigo=u'IR41', tamanho=[44, 44, 44], raiz=u'//ret/resCCe',obrigatorio=False)
        self.dhEvento = TagCaracter(nome=u'dhEvento', codigo=u'IR42' ,  tamanho=[ 0, 30],raiz=u'//ret/resCCe',obrigatorio=False)
        self.tpEvento = TagCaracter(nome=u'tpEvento'   , codigo=u'IR43', tamanho=[6, 6, 6], raiz=u'//ret/resCCe',obrigatorio=False)
        self.nSeqEvento = TagInteiro(nome=u'nSeqEvento'   , codigo=u'IR44', tamanho=[2,2], raiz=u'//ret/resCCe',obrigatorio=False)
        self.descEvento = TagCaracter(nome=u'descEvento'   , codigo=u'IR45' , tamanho=[ 5, 60]   , raiz=u'//ret/resCCe',obrigatorio=False)
        self.xCorrecao = TagCaracter(nome=u'descEvento'   , codigo=u'IR46' , tamanho=[ 15, 1000]   , raiz=u'//ret/resCCe', obrigatorio=False)
        self.tpNF = TagInteiro(nome=u'tpNF', codigo=u'IR47' , tamanho=[1, 1, 1]     , raiz=u'//ret/resCCe',obrigatorio=False)
        self.dhRecbto = TagCaracter(nome=u'dhRecbto', codigo=u'IR48' ,  tamanho=[ 0, 30],raiz=u'//ret/resCCe',obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        if self.NSU.xml:
            xml += u'<ret>'
        xml += self.NSU.xml
        xml += self.chNFe.xml
        xml += self.dhEvento.xml
        xml += self.tpEvento.xml
        xml += self.nSeqEvento.xml
        xml += self.descEvento.xml
        xml += self.xCorrecao.xml
        xml += self.tpNF.xml
        xml += self.dhRecbto.xml
        if self.NSU.xml:
            xml += u'</resCCe>'
#            xml += u'</ret>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NSU.xml = arquivo
            self.chNFe.xml = arquivo
            self.dhEvento.xml = arquivo
            self.tpEvento.xml = arquivo
            self.nSeqEvento.xml = arquivo
            self.descEvento.xml = arquivo
            self.xCorrecao.xml = arquivo
            self.tpNF.xml = arquivo
            self.dhRecbto.xml = arquivo

    xml = property(get_xml, set_xml)


class ResCanc(XMLNFe):
    def __init__(self):
        super(ResCanc, self).__init__()
        self.NSU    = TagInteiro(nome=u'resCanc', codigo=u'IR25', tamanho=[1, 15]    , raiz=u'//ret', propriedade=u'NSU', obrigatorio=False)
        self.chNFe = TagCaracter(nome=u'chNFe'   , codigo=u'IR27', tamanho=[44, 44, 44], raiz=u'//ret/resCanc',obrigatorio=False)
        self.CNPJ = TagCaracter(nome=u'CNPJ'   , codigo=u'IR28' , tamanho=[ 0, 14]   , raiz=u'//ret/resCanc',obrigatorio=False)
        self.CPF  = TagCaracter(nome=u'CPF'    , codigo=u'IR29', tamanho=[11, 11]   , raiz=u'//ret/resCanc',obrigatorio=False)
        self.xNome  = TagCaracter(nome=u'xNome'   , codigo=u'IR30' , tamanho=[ 3, 60]   , raiz=u'//ret/resCanc' ,obrigatorio=False)
        self.IE    = TagCaracter(nome=u'IE'  , codigo=u'IR31', tamanho=[ 1, 14]   , raiz=u'//ret/resCanc',obrigatorio=False)
        self.dEmi = TagCaracter(nome=u'dEmi', codigo=u'IR32' ,  tamanho=[ 0, 30],raiz=u'//ret/resCanc',obrigatorio=False)
        self.tpNF = TagInteiro(nome=u'tpNF', codigo=u'IR33' , tamanho=[1, 1, 1]     , raiz=u'//ret/resCanc',obrigatorio=False)
        self.vNF     = TagDecimal(nome=u'vNF'    , codigo=u'IR34', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//ret/resCanc',obrigatorio=False)
        self.digVal    = TagCaracter(nome=u'digVal'  , codigo=u'IR35', tamanho=[28, 28]   , raiz=u'//ret/resCanc',obrigatorio=False)
        self.dhRecbto = TagCaracter(nome=u'dhRecbto', codigo=u'IR36' ,  tamanho=[ 0, 30],raiz=u'//ret/resCanc',obrigatorio=False)
        self.cSitNFe = TagInteiro(nome=u'cSitNFe', codigo=u'IR37' , tamanho=[1, 1, 1]     , raiz=u'//ret/resCanc',obrigatorio=False)
        self.cSitConf = TagInteiro(nome=u'cSitConf', codigo=u'IR38' , tamanho=[1, 1, 1]     , raiz=u'//ret/resCanc',obrigatorio=False)


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        if self.NSU.xml:
            xml += u'<ret>'
        xml += self.NSU.xml
        xml += self.chNFe.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.xNome.xml
        xml += self.IE.xml
        xml += self.dEmi.xml
        xml += self.tpNF.xml
        xml += self.vNF.xml
        xml += self.digVal.xml
        xml += self.dhRecbto.xml
        xml += self.cSitNFe.xml
        xml += self.cSitConf.xml
        if self.NSU.xml:
            xml += u'</resCanc>'
#            xml += u'</ret>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NSU.xml = arquivo
            self.chNFe.xml = arquivo
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo
            self.xNome.xml = arquivo
            self.IE.xml = arquivo
            self.dEmi.xml = arquivo
            self.tpNF.xml = arquivo
            self.vNF.xml = arquivo
            self.digVal.xml = arquivo
            self.dhRecbto.xml = arquivo
            self.cSitNFe.xml = arquivo
            self.cSitConf.xml = arquivo
    xml = property(get_xml, set_xml)

class ResNFe(XMLNFe):
    def __init__(self):
        super(ResNFe, self).__init__()
        self.NSU    = TagInteiro(nome=u'resNFe', codigo=u'IR11', tamanho=[1, 15]    , raiz=u'//ret', propriedade=u'NSU',obrigatorio=False)
        self.chNFe = TagCaracter(nome=u'chNFe'   , codigo=u'IR13', tamanho=[44, 44, 44], raiz=u'//ret/resNFe',obrigatorio=False)
        self.CNPJ = TagCaracter(nome=u'CNPJ'   , codigo=u'IR14' , tamanho=[ 0, 14]   , raiz=u'//ret/resNFe',obrigatorio=False)
        self.CPF  = TagCaracter(nome=u'CPF'    , codigo=u'IR15', tamanho=[11, 11]   , raiz=u'//ret/resNFe',obrigatorio=False)
        self.xNome  = TagCaracter(nome=u'xNome'   , codigo=u'IR16' , tamanho=[ 3, 60]   , raiz=u'//ret/resNFe' ,obrigatorio=False)
        self.IE    = TagCaracter(nome=u'IE'  , codigo=u'IR17', tamanho=[ 1, 14]   , raiz=u'//ret/resNFe',obrigatorio=False)
        self.dEmi = TagData(nome=u'dEmi', codigo=u'IR18' , raiz=u'//ret/resNFe',obrigatorio=False)
        self.tpNF = TagInteiro(nome=u'tpNF', codigo=u'IR19' , tamanho=[1, 1, 1]     , raiz=u'//ret/resNFe',obrigatorio=False)
        self.vNF     = TagDecimal(nome=u'vNF'    , codigo=u'IR20', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//ret/resNFe',obrigatorio=False)
        self.digVal    = TagCaracter(nome=u'digVal'  , codigo=u'IR21', tamanho=[28, 28]   , raiz=u'//ret/resNFe',obrigatorio=False)
        self.dhRecbto = TagDataHora(nome=u'dhRecbto', codigo=u'IR22' , raiz=u'//ret/resNFe',obrigatorio=False)
        self.cSitNFe = TagInteiro(nome=u'cSitNFe', codigo=u'IR23' , tamanho=[1, 1, 1]     , raiz=u'//ret/resNFe',obrigatorio=False)
        self.cSitConf = TagInteiro(nome=u'cSitConf', codigo=u'IR24' , tamanho=[1, 1, 1]     , raiz=u'//ret/resNFe',obrigatorio=False)


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        if self.NSU.xml:
            xml += u'<ret>'
        xml += self.NSU.xml
        xml += self.chNFe.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.xNome.xml
        xml += self.IE.xml
        xml += self.dEmi.xml
        xml += self.tpNF.xml
        xml += self.vNF.xml
        xml += self.digVal.xml
        xml += self.dhRecbto.xml
        xml += self.cSitNFe.xml
        xml += self.cSitConf.xml
        if self.NSU.xml:
            xml += u'</resNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NSU.xml = arquivo
            self.chNFe.xml = arquivo
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo
            self.xNome.xml = arquivo
            self.IE.xml = arquivo
            self.dEmi.xml = arquivo
            self.tpNF.xml = arquivo
            self.vNF.xml = arquivo
            self.digVal.xml = arquivo
            self.dhRecbto.xml = arquivo
            self.cSitNFe.xml = arquivo
            self.cSitConf.xml = arquivo

    xml = property(get_xml, set_xml)



class Ret(XMLNFe):
    def __init__(self):
        super(Ret, self).__init__()
        self.ret   = TagCaracter(nome=u'ret' , codigo=u'IR10',  raiz=u'/')
        self.resNFe = ResNFe()
        self.resCanc = ResCanc()
        self.resCCe = ResCCe()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.resNFe.xml
        xml += self.resCanc.xml
        xml += self.resCCe.xml
        xml += u'</ret>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ret.xml = arquivo
            self.resNFe.xml = arquivo
            self.resCanc.xml = arquivo
            self.resCCe.xml = arquivo

    xml = property(get_xml, set_xml)



class RetConsNFeDest(XMLNFe):
    def __init__(self):
        super(RetConsNFeDest, self).__init__()
        self.versao    = TagDecimal(nome=u'retConsNFeDest',propriedade=u'versao', codigo=u'IR01',  namespace=NAMESPACE_NFE, valor=u'1.01', raiz=u'/')
        self.tpAmb = TagInteiro(nome=u'tpAmb'   , codigo=u'IR03', tamanho=[ 1,  1, 1] , raiz=u'//retConsNFeDest', valor=2)
        self.verAplic = TagCaracter(nome=u'verAplic', codigo=u'IR04' , tamanho=[1, 20]     , raiz=u'//retConsNFeDest')
        self.cStat    = TagCaracter(nome=u'cStat'    , codigo=u'IR05' , tamanho=[3, 3, 3]   , raiz=u'//retConsNFeDest')
        self.xMotivo  = TagCaracter(nome=u'xMotivo' , codigo=u'IR06' , tamanho=[1, 255]    , raiz=u'//retConsNFeDest')
        self.dhResp = TagCaracter(nome=u'dhResp', codigo=u'IR07' ,  tamanho=[ 0, 30],raiz=u'//retConsNFeDest')
        self.indCont = TagInteiro(nome=u'indCont', codigo=u'IR08' , tamanho=[1, 1, 1]     , raiz=u'//retConsNFeDest', obrigatorio=False)
        self.ultNSU = TagInteiro(nome=u'ultNSU', codigo=u'IR09' , tamanho=[1, 15]     , raiz=u'//retConsNFeDest',obrigatorio=False)
        self.ret = []
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retconsNFeDest_v1.01.xsd'

    def get_xml(self):


        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.dhResp.xml
        xml += self.indCont.xml
        xml += self.ultNSU.xml
        for d in self.ret:
            xml += d.xml

        xml += u'</retConsNFeDest>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml = arquivo
            self.verAplic.xml = arquivo
            self.cStat.xml = arquivo
            self.xMotivo.xml = arquivo
            self.dhResp.xml = arquivo
            self.indCont.xml = arquivo
            self.ultNSU.xml = arquivo
            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.ret = self.le_grupo('//retConsNFeDest/ret', Ret)


    xml = property(get_xml, set_xml)

