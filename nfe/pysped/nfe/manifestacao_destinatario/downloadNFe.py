# -*- coding: utf-8 -*-
__author__ = 'marcilene.ribeiro'


from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manifestacao_destinatario import ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)



class DownloadNFe(XMLNFe):
    def __init__(self):
        super(DownloadNFe, self).__init__()
        self.versao    = TagDecimal(nome=u'downloadNFe', codigo=u'JP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.00', raiz=u'/')
        self.tpAmb = TagInteiro(nome=u'tpAmb'   , codigo=u'JP03', tamanho=[ 1,  1, 1] , raiz=u'//downloadNFe')
        self.xServ =  TagCaracter(nome=u'xServ', codigo=u'JP04' , tamanho=[12, 12, 12]     , raiz=u'//downloadNFe',valor=u'DOWNLOAD NFE')
        self.CNPJ = TagCaracter(nome=u'CNPJ'   , codigo=u'JP05' , tamanho=[ 0, 14]   , raiz=u'//downloadNFe')
        self.chNFe = TagCaracter(nome=u'chNFe'   , codigo=u'JP06', tamanho=[44, 44, 44], raiz=u'//downloadNFe')
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'downloadNFe_v1.00.xsd'


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.CNPJ.xml
        xml += self.chNFe.xml
        xml += u'</downloadNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml = arquivo
            self.CNPJ.xml = arquivo
            self.chNFe.xml = arquivo


    xml = property(get_xml, set_xml)


class ProcNFeGrupoZip(XMLNFe):
    def __init__(self):
        super(ProcNFeGrupoZip, self).__init__()
        self.procNFeZip    = TagCaracter(nome=u'ProcNFeGrupoZip', codigo=u'JR12', tamanho=[15, 1000]    , raiz=u'//retNFe/ProcNFeGrupoZip', propriedade=u'procNFeZip', obrigatorio= False)
        self.NFeZip = TagCaracter(nome=u'NFeZip'   , codigo=u'JR14', tamanho=[44, 44, 44], raiz=u'//retNFe/ProcNFeGrupoZip', obrigatorio= False)
        self.protNFeZip = TagCaracter(nome=u'protNFeZip', codigo=u'JR15' ,  tamanho=[ 0, 30],raiz=u'//retNFe/ProcNFeGrupoZip', obrigatorio= False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += self.procNFeZip.xml
        xml += self.NFeZip.xml
        xml += self.protNFeZip.xml
        if  self.protNFeZip.xml:
            xml += u'</ProcNFeGrupoZip>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.procNFeZip.xml = arquivo
            self.NFeZip.xml = arquivo
            self.protNFeZip.xml = arquivo

    xml = property(get_xml, set_xml)


#<retDownloadNFe versao="1.00" xmlns="http://www.portalfiscal.inf.br/nfe"><tpAmb>1</tpAmb><verAplic>RS20111129150959</verAplic><cStat>139</cStat><xMotivo>Pedido de download Processado</xMotivo><dhResp>2012-12-17T17:25:53</dhResp>
#<retNFe>
#<chNFe>43121203211158000142550010000125531144040128</chNFe><cStat>140</cStat><xMotivo>Download disponibilizado</xMotivo>
#<procNFeGrupoZip>
#<NFeZip>H4sIAAAAAAAEAO29B2AcS...</NFeZip>
#<protNFeZip>H4sIAAAAAAAEAO29B2AcS...</protNFeZip>
#</procNFeGrupoZip>
#</retNFe></retDownloadNFe>





class RetNFe(XMLNFe):
    def __init__(self):
        super(RetNFe, self).__init__()
        self.chNFe    = TagCaracter(nome=u'chNFe', codigo=u'JR08',  tamanho=[44, 44, 44], raiz=u'//retDownloadNFe/retNFe')
        self.cStat    = TagCaracter(nome=u'cStat'    , codigo=u'JR10' , tamanho=[3, 3, 3]   , raiz=u'//retDownloadNFe/retNFe')
        self.xMotivo  = TagCaracter(nome=u'xMotivo' , codigo=u'JR11' , tamanho=[1, 255]    , raiz=u'//retDownloadNFe/retNFe')
        self.procNFeGrupoZip = ProcNFeGrupoZip()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<retNFe>'
        xml += self.chNFe.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        if self.procNFeGrupoZip.xml:
            xml += self.procNFeGrupoZip.xml
        xml += u'</retNFe>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chNFe.xml = arquivo
            self.cStat.xml = arquivo
            self.xMotivo.xml = arquivo
            if self.procNFeGrupoZip.xml:
                self.procNFeGrupoZip.xml = arquivo

    xml = property(get_xml, set_xml)

class RetDownloadNFe(XMLNFe):
    def __init__(self):
        super(RetDownloadNFe, self).__init__()
        self.versao    = TagDecimal(nome=u'retDownloadNFe',propriedade=u'versao', codigo=u'JR01',  namespace=NAMESPACE_NFE, valor=u'1.00', raiz=u'/')
        self.tpAmb = TagInteiro(nome=u'tpAmb'   , codigo=u'JR03', tamanho=[ 1,  1, 1] , raiz=u'//retDownloadNFe', valor=2)
        self.verAplic = TagCaracter(nome=u'verAplic', codigo=u'JR04' , tamanho=[1, 20]     , raiz=u'//retDownloadNFe')
        self.cStat    = TagCaracter(nome=u'cStat'    , codigo=u'JR05' , tamanho=[3, 3, 3]   , raiz=u'//retDownloadNFe')
        self.xMotivo  = TagCaracter(nome=u'xMotivo' , codigo=u'JR06' , tamanho=[1, 255]    , raiz=u'//retDownloadNFe')
        self.dhResp = TagCaracter(nome=u'dhResp', codigo=u'JR07' ,  tamanho=[ 0, 30],raiz=u'//retDownloadNFe')
        self.retNFe = RetNFe()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retDownloadNFe_v1.00.xsd'

    def get_xml(self):


        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.dhResp.xml
        xml += self.retNFe.xml
        xml += u'</retDownloadNFe>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml = arquivo
            self.verAplic.xml = arquivo
            self.cStat.xml = arquivo
            self.xMotivo.xml = arquivo
            self.dhResp.xml = arquivo
            self.retNFe.xml = arquivo

    xml = property(get_xml, set_xml)

