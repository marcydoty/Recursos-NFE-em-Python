# -*- coding: utf-8 -*-
__author__ = 'marcilene.ribeiro'


from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manifestacao_destinatario import ESQUEMA_ATUAL
import os

DIRNAME = os.path.dirname(__file__)

class TagChNFe(TagCaracter):
    def __init__(self, *args, **kwargs):
        super(TagChNFe, self).__init__(*args, **kwargs)
        self.nome = 'chNFe'
        self.codigo = 'JP06',
        self.tamanho = [44, 44]
        self.raiz = '//downloadNFe'
        
class DownloadNFe(XMLNFe):
    def __init__(self):
        super(DownloadNFe, self).__init__()
        self.versao    = TagDecimal(nome=u'downloadNFe', codigo=u'JP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.00', raiz=u'/')
        self.tpAmb = TagInteiro(nome=u'tpAmb'   , codigo=u'JP03', tamanho=[ 1,  1, 1] , raiz=u'//downloadNFe')
        self.xServ =  TagCaracter(nome=u'xServ', codigo=u'JP04' , tamanho=[12, 12, 12]     , raiz=u'//downloadNFe',valor=u'DOWNLOAD NFE')
        self.CNPJ = TagCaracter(nome=u'CNPJ'   , codigo=u'JP05' , tamanho=[ 0, 14]   , raiz=u'//downloadNFe')
        #self.chNFe = TagCaracter(nome=u'chNFe'   , codigo=u'JP06', tamanho=[44, 44, 44], raiz=u'//downloadNFe')
        self.chNFe = []
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'downloadNFe_v1.00.xsd'


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.tpAmb.xml
        xml += self.xServ.xml
        xml += self.CNPJ.xml
        #xml += self.chNFe.xml
        for chave in self.chNFe:
            xml += chave.xml
        
        xml += u'</downloadNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.tpAmb.xml  = arquivo
            self.xServ.xml = arquivo
            self.CNPJ.xml = arquivo
            #self.chNFe.xml = arquivo
            self.chNFe = self.le_grupo('//downloadNFe/chNFe', TagChNFe)


    xml = property(get_xml, set_xml)


class ProcNFeGrupoZip(XMLNFe):
    def __init__(self):
        super(ProcNFeGrupoZip, self).__init__()
        self.NFeZip = TagCaracter(nome='NFeZip', codigo='JR13', raiz='//retNFe/procNFeGrupoZip')
        self.protNFeZip = TagCaracter(nome='protNFeZip', codigo='JR14', raiz='//retNFe/procNFeGrupoZip')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.NFeZip.valor and self.protNFeZip.valor:
            xml += '<procNFeGrupoZip>'
            xml += self.NFeZip.xml
            xml += self.protNFeZip.xml
            xml += '</procNFeGrupoZip>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.NFeZip.xml     = arquivo
            self.protNFeZip.xml = arquivo

    xml = property(get_xml, set_xml)


class RetNFe(XMLNFe):
    def __init__(self):
        super(RetNFe, self).__init__()
        self.chNFe    = TagCaracter(nome=u'chNFe', codigo=u'JR08',  tamanho=[44, 44, 44], raiz=u'//retDownloadNFe/retNFe')
        self.cStat    = TagCaracter(nome=u'cStat'    , codigo=u'JR10' , tamanho=[3, 3, 3]   , raiz=u'//retDownloadNFe/retNFe')
        self.xMotivo  = TagCaracter(nome=u'xMotivo' , codigo=u'JR11' , tamanho=[1, 255]    , raiz=u'//retDownloadNFe/retNFe')
        self.procNFeZip = TagCaracter(nome='procNFeZip', codigo='JR13', raiz='//retNFe', obrigatorio=False)
        self.schema  = TagCaracter(nome='procNFe', propriedade='schema', raiz='//retNFe', obrigatorio=False)
        self.procNFe  = TagCaracter(nome='procNFe', codigo='JR12', raiz='//retNFe', obrigatorio=False)
        self.procNFeGrupoZip = ProcNFeGrupoZip()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<retNFe>'
        xml += self.chNFe.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        
        if self.procNFe.valor:
            xml += self.schema.xml
            xml += self.procNFe.valor
            xml += '</procNFe>'
        
        xml += self.procNFeZip.xml
        xml += self.procNFeGrupoZip.xml
        
        xml += u'</retNFe>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.chNFe.xml = arquivo
            self.cStat.xml = arquivo
            self.xMotivo.xml = arquivo
            self.schema.xml  = arquivo
            
            procNFe = self._le_noh('//retNFe/procNFe')
            if procNFe is not None and len(procNFe):
                procNFe = etree.tostring(procNFe, encoding='unicode')
                procNFe = procNFe.split('<')
                procNFe = '<' + '<'.join(procNFe[2:-1])
                self.procNFe.valor = procNFe
            else:
                self.procNFe.valor = ''

            self.procNFeZip.xml = arquivo
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
        #self.retNFe = RetNFe()
        self.retNFe = []
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
        #xml += self.retNFe.xml
        for r in self.retNFe:
            xml += r.xml
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
            #self.retNFe.xml = arquivo
            self.retNFe = self.le_grupo('//retDownloadNFe/retNFe', RetNFe)

    xml = property(get_xml, set_xml)


