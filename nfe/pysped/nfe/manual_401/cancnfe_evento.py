# -*- coding: utf-8 -*-

from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manual_401 import ESQUEMA_ATUAL
import os


DIRNAME = os.path.dirname(__file__)


class InfEventoEnviado(XMLNFe):
    def __init__(self):
        super(InfEventoEnviado, self).__init__()
        self.Id    = TagCaracter(nome=u'infEvento', codigo=u'HP06', tamanho=[54, 54]    , raiz=u'//envEvento', propriedade=u'Id')
        self.cOrgao  = TagInteiro(nome=u'cOrgao'      , codigo=u'HP08', tamanho=[2, 2,2]   , raiz=u'//envEvento/infEvento', valor=91)
        self.tpAmb = TagInteiro(nome=u'tpAmb'   , codigo=u'HP09', tamanho=[ 1,  1, 1] , raiz=u'//envEvento/infEvento', valor=2)
        self.CNPJ    = TagCaracter(nome=u'CNPJ'   , codigo=u'HP10' , tamanho=[ 0, 14]   , raiz=u'//envEvento/infEvento')
        self.CPF     = TagCaracter(nome=u'CPF'    , codigo=u'HP11', tamanho=[11, 11]   , raiz=u'//envEvento/infEvento')
        self.chNFe = TagCaracter(nome=u'chNFe'   , codigo=u'HP12', tamanho=[44, 44, 44], raiz=u'//envEvento/infEvento')
#        self.dhEvento = TagDataHora(nome=u'dhRecbto', codigo=u'HP13' ,  raiz=u'//envEvento/infEvento')
        self.dhEvento = TagCaracter(nome=u'dhEvento', codigo=u'HP13' , tamanho=[ 0, 30], raiz=u'//envEvento/infEvento')
        self.tpEvento = TagCaracter(nome=u'tpEvento'   , codigo=u'HP14', tamanho=[6, 6, 6], raiz=u'//envEvento/infEvento',valor=u'110111')
        self.nSeqEvento = TagInteiro(nome=u'nSeqEvento'   , codigo=u'HP15', tamanho=[1,2], raiz=u'//envEvento/infEvento', valor=1)
        self.verEvento = TagDecimal(nome=u'verEvento'   , codigo=u'HP16', raiz=u'//envEvento/infEvento', valor=u'1.00')
        self.versao= TagDecimal(nome=u'detEvento'   , codigo=u'HP17',  raiz=u'//envEvento/infEvento', propriedade=u'versao', valor=u'1.00')
        self.descEvento  = TagCaracter(nome=u'descEvento'   , codigo=u'HP19' , tamanho=[ 5, 60]   , raiz=u'//envEvento/infEvento/detEvento', valor=u'Cancelamento')
        self.nProt    = TagCaracter(nome=u'nProt'    , codigo=u'HP20' , tamanho=[15, 15, 15], raiz=u'//envEvento/infEvento/detEvento')
        self.xJust = TagCaracter(nome=u'xJust'  , codigo=u'HP21', tamanho=[15, 255]   , raiz=u'//envEvento/infEvento/detEvento')

    def get_xml(self):

        xml = XMLNFe.get_xml(self)

        self.Id.valor = u'ID' + self.tpEvento.valor + self.chNFe.valor +  ("%02d" % self.nSeqEvento.valor)

        xml += self.Id.xml
        xml += self.cOrgao.xml
        xml += self.tpAmb.xml
        xml += self.CNPJ.xml
        if self.CPF.valor:
            xml += self.CPF.xml
        xml += self.chNFe.xml
        xml += self.dhEvento.xml
        xml += self.tpEvento.xml
        xml += self.nSeqEvento.xml
        xml += self.verEvento.xml
        xml += self.versao.xml
        xml += self.descEvento.xml
        xml += self.nProt.xml
        xml += self.xJust.xml
        xml += u'</detEvento>'
        xml += u'</infEvento>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.cOrgao.xml = arquivo
            self.tpAmb.xml = arquivo
            self.CNPJ.xml = arquivo
            if self.CPF.valor:
                self.CPF.xml = arquivo
            self.chNFe.xml = arquivo
            self.dhEvento.xml = arquivo
            self.tpEvento.xml = arquivo
            self.nSeqEvento.xml = arquivo
            self.verEvento.xml = arquivo
            self.versao.xml = arquivo
            self.descEvento.xml = arquivo
            self.nProt.xml = arquivo
            self.xJust.xml = arquivo

    xml = property(get_xml, set_xml)


class EnvEvento(XMLNFe):
    def __init__(self):
        super(EnvEvento, self).__init__()
        self.versao    = TagDecimal(nome=u'envEvento', codigo=u'HP01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.00', raiz=u'/')
        self.idLote    = TagInteiro(nome=u'idLote', codigo=u'HP03', tamanho=[1, 15]    , raiz=u'//envEvento', valor=1)
        self.evento_versao = TagDecimal(nome=u'evento'   , codigo=u'HP04', namespace=NAMESPACE_NFE, raiz=u'//envEvento', valor=u'1.00', propriedade=u'versao')
        self.infEvento   = InfEventoEnviado()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'envEventoCancNFe_v1.00.xsd'


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml
        xml += self.evento_versao.xml
        xml += self.infEvento.xml

        #
        # Define a URI a ser assinada
        #
        self.Signature.URI = u'#' + self.infEvento.Id.valor

        xml += self.Signature.xml
        xml += u'</evento>'
        xml += u'</envEvento>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.infEvento.xml = arquivo
            self.Signature.xml = self._le_noh('//envEvento/sig:Signature')
    xml = property(get_xml, set_xml)


class InfEventoRecebido(XMLNFe):
    def __init__(self):
        super(InfEventoRecebido, self).__init__()
        self.Id    = TagCaracter(nome=u'infEvento', codigo=u'HR11', tamanho=[17, 17]    , raiz=u'//retEnvEvento/retEvento', propriedade=u'Id',obrigatorio=False)
        self.tpAmb = TagInteiro(nome=u'tpAmb'   , codigo=u'HR13', tamanho=[ 1,  1, 1] , raiz=u'//retEnvEvento/retEvento/infEvento')
        self.verAplic = TagCaracter(nome=u'verAplic', codigo=u'HR14' , tamanho=[1, 20]     , raiz=u'//retEnvEvento/retEvento/infEvento')
        self.cOrgao  = TagInteiro(nome=u'cOrgao'      , codigo=u'HR15', tamanho=[2, 2,2]   , raiz=u'//retEnvEvento/retEvento/infEvento' )
        self.cStat    = TagCaracter(nome=u'cStat'    , codigo=u'HR16' , tamanho=[3, 3, 3]   , raiz=u'//retEnvEvento/retEvento/infEvento')
        self.xMotivo  = TagCaracter(nome=u'xMotivo' , codigo=u'HR17' , tamanho=[1, 255]    , raiz=u'//retEnvEvento/retEvento/infEvento')
        self.chNFe = TagCaracter(nome=u'chNFe'   , codigo=u'HR18', tamanho=[44, 44, 44], raiz=u'//retEnvEvento/retEvento/infEvento',obrigatorio=False)
        self.tpEvento = TagCaracter(nome=u'tpEvento'   , codigo=u'HR19', tamanho=[6, 6, 6], raiz=u'//retEnvEvento/retEvento/infEvento',valor=u'110111',obrigatorio=False)
        self.xEvento  = TagCaracter(nome=u'xEvento'   , codigo=u'HR20' , tamanho=[ 5, 60]   , raiz=u'//retEnvEvento/retEvento/infEvento', obrigatorio=False,valor='CANCELAMENTO HOMOLOGADO')#, valor=u'Cancelamento homologado')
        self.nSeqEvento = TagInteiro(nome=u'nSeqEvento'   , codigo=u'HR21', tamanho=[2,2], raiz=u'//retEnvEvento/retEvento/infEvento',obrigatorio=False, valor=1)#,valor=1)
        self.CNPJDest  = TagCaracter(nome=u'CNPJDest'   , codigo=u'HR22' , tamanho=[ 0, 14]   , raiz=u'//retEnvEvento/retEvento/infEvento',obrigatorio=False)
        self.CPFDest  = TagCaracter(nome=u'CPFDest'    , codigo=u'HR23', tamanho=[11, 11]   , raiz=u'//retEnvEvento/retEvento/infEvento',obrigatorio=False)
        self.emailDest = TagCaracter(nome=u'emailDest'   , codigo=u'HR24' , tamanho=[ 1, 60]   , raiz=u'//retEnvEvento/retEvento/infEvento',obrigatorio=False)
#        self.dhRegEvento = TagDataHora(nome=u'dhRegEvento', codigo=u'HR25' ,  raiz=u'//retEnvEvento/retEvento/infEvento')
        self.dhRegEvento = TagCaracter(nome=u'dhRegEvento', codigo=u'HR25' ,  tamanho=[ 0, 30],raiz=u'//retEnvEvento/retEvento/infEvento')
        self.nProt    = TagCaracter(nome=u'nProt'    , codigo=u'HR26' , tamanho=[15, 15, 15], raiz=u'//retEnvEvento/infEvento',obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)

        if self.Id.xml:
            xml += self.Id.xml
        else:
            xml += u'<infEvento>'
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cOrgao.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.chNFe.xml
        xml += self.tpEvento.xml
        xml += self.xEvento.xml
        xml += self.nSeqEvento.xml
        xml += self.CNPJDest.xml
        if self.CPFDest.xml:
            xml += self.CPFDest.xml
        xml += self.emailDest.xml
        xml += self.dhRegEvento.xml
        xml += self.nProt.xml
        xml += u'</infEvento>'
        xml += u'</retEvento>'
        return xml


    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.Id.xml = arquivo
            self.tpAmb.xml = arquivo
            self.verAplic.xml = arquivo
            self.cOrgao.xml = arquivo
            self.cStat.xml = arquivo
            self.xMotivo.xml = arquivo
            self.chNFe.xml = arquivo
            self.tpEvento.xml = arquivo
            self.xEvento.xml = arquivo
            self.nSeqEvento.xml = arquivo
            self.CNPJDest.xml = arquivo
            if self.CPFDest.xml:
                self.CPFDest.xml = arquivo
            self.emailDest.xml = arquivo
            self.dhRegEvento.xml = arquivo
            self.nProt.xml = arquivo

    xml = property(get_xml, set_xml)


class RetEnvEvento(XMLNFe):
    def __init__(self):
        super(RetEnvEvento, self).__init__()
        self.versao    = TagDecimal(nome=u'retEnvEvento',propriedade=u'versao', codigo=u'HR01',  namespace=NAMESPACE_NFE, valor=u'1.00', raiz=u'/')
        self.idLote    = TagInteiro(nome=u'idLote', codigo=u'HR03', tamanho=[1, 15]    , raiz=u'//retEnvEvento', valor=1)
        self.tpAmb = TagInteiro(nome=u'tpAmb'   , codigo=u'HR04', tamanho=[ 1,  1, 1] , raiz=u'//retEnvEvento', valor=2)
        self.verAplic = TagCaracter(nome=u'verAplic', codigo=u'HR05' , tamanho=[1, 20]     , raiz=u'//retEnvEvento')
        self.cOrgao  = TagInteiro(nome=u'cOrgao'      , codigo=u'HR06', tamanho=[2, 2, 2]   , raiz=u'//retEnvEvento' )
        self.cStat    = TagCaracter(nome=u'cStat'    , codigo=u'HR07' , tamanho=[3, 3, 3]   , raiz=u'//retEnvEvento')
        self.xMotivo  = TagCaracter(nome=u'xMotivo' , codigo=u'HR08' , tamanho=[1, 255]    , raiz=u'//retEnvEvento')
        self.ret_evento_versao = TagDecimal(nome=u'retEvento', codigo=u'HR09', raiz=u'//retEnvEvento', valor=u'1.00',  propriedade=u'versao')
        self.infEvento   = InfEventoRecebido()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retEnvEventoCancNFe_v1.00.xsd'

    def get_xml(self):


        xml = XMLNFe.get_xml(self)

        xml += ABERTURA
        xml += self.versao.xml
        xml += self.idLote.xml
        xml += self.tpAmb.xml
        xml += self.verAplic.xml
        xml += self.cOrgao.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.ret_evento_versao.xml
        xml += self.infEvento.xml
#        print 'xml evento recebido',xml

        # Define a URI a ser assinada
        #
        if len(self.Signature.URI) and (self.Signature.URI.strip() != u'#'):
            xml += self.Signature.xml

        xml += u'</retEnvEvento>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml = arquivo
            self.idLote.xml = arquivo
            self.tpAmb.xml = arquivo
            self.verAplic.xml = arquivo
            self.cOrgao.xml = arquivo
            self.cStat.xml = arquivo
            self.xMotivo.xml = arquivo
            self.ret_evento_versao.xml = arquivo
            self.infEvento.xml = arquivo
            self.Signature.xml = self._le_noh('//retEnvEvento/sig:Signature')

    xml = property(get_xml, set_xml)

class ProcEventoNFe(XMLNFe):
    def __init__(self):
        super(ProcEventoNFe, self).__init__()
        #
        # Atenção --- a tag procEventoNFe tem que começar com letra minúscula, para
        # poder validar no XSD.
        #
        self.versao = TagDecimal(nome=u'procEventoNFe', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'1.00', raiz=u'/')
        self.envEvento = EnvEvento()
        self.retEnvEvento = RetEnvEvento()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'procEventoCancNFe_v1.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.envEvento.evento_versao.xml.replace(ABERTURA, u'')
        xml += self.envEvento.infEvento.xml
        xml += self.envEvento.Signature.xml
        xml += u'</evento>'

        xml += self.retEnvEvento.ret_evento_versao.xml.replace(ABERTURA, u'')
        xml += self.retEnvEvento.infEvento.xml
        xml += u'</procEventoNFe>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.envEvento.evento_versao.xml = arquivo
            self.envEvento.infEvento.xml = arquivo
            self.retEnvEvento.ret_evento_versao.xml = arquivo
            self.retEnvEvento.infEvento.xml = arquivo
            self.envEvento.Signature.xml = arquivo
            self.Signature.xml = self._le_noh('//procEventoNFe/sig:Signature')

    xml = property(get_xml, set_xml)
