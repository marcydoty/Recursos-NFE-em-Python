# -*- coding: utf-8 -*-


import os


DIRNAME = os.path.dirname(__file__)
from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manual_401 import conscad_200
from nfe.pysped.nfe.manual_500 import ESQUEMA_ATUAL

class _InfConsEnviado(XMLNFe):
    def __init__(self):
        self.xServ = TagCaracter(nome=u'xServ', codigo=u'GP04', tamanho=[8, 8], raiz=u'//ConsCad', valor=u'CONS-CAD')
        self.UF = TagCaracter(nome=u'UF', codigo=u'GP05', tamanho=[2, 2], raiz=u'//ConsCad')
        self.IE = TagCaracter(nome=u'IE', codigo=u'GP06', tamanho=[2, 14], raiz=u'//ConsCad', obrigatorio=False)
        self.CNPJ = TagCaracter(nome=u'CNPJ', codigo=u'GP07', tamanho=[3, 14], raiz=u'//ConsCad', obrigatorio=False)
        self.CPF = TagCaracter(nome=u'CPF', codigo=u'GP08', tamanho=[3, 11], raiz=u'//ConsCad', obrigatorio=False)

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infCons>'
        xml += self.xServ.xml
        xml += self.UF.xml
        xml += self.IE.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += u'</infCons>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xServ.xml = arquivo
            self.UF.xml = arquivo
            self.IE.xml = arquivo
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo

    xml = property(get_xml, set_xml)


class ConsCad(conscad_200.ConsCad):
    def __init__(self):
        super(ConsCad, self).__init__()


class Ender(conscad_200.Ender):
    def __init__(self):
        super(Ender, self).__init__()


class _InfCadRecebido(XMLNFe):
    def __init__(self):
        self.IE = TagCaracter(nome=u'IE', codigo=u'GR08', tamanho=[2, 14], raiz=u'//infCad')
        self.CNPJ = TagCaracter(nome=u'CNPJ', codigo=u'GR09', tamanho=[3, 14], raiz=u'//infCad')
        self.CPF = TagCaracter(nome=u'CPF', codigo=u'GR10', tamanho=[3, 11], raiz=u'//infCad')
        self.UF = TagCaracter(nome=u'UF', codigo=u'GR11', tamanho=[2, 2], raiz=u'//infCad')
        self.cSit = TagInteiro(nome=u'cSit', codigo=u'GR12', tamanho=[1, 1], raiz=u'//infCad')
        self.indCredNFe = TagCaracter(nome=u'indCredNFe', codigo=u'GR12a', tamanho=[1, 1], raiz=u'//infCad')
        self.indCredCTe = TagCaracter(nome=u'indCredCTe', codigo=u'GR12b', tamanho=[1, 1], raiz=u'//infCad')
        self.xNome = TagCaracter(nome=u'xNome', codigo=u'GR13', tamanho=[1, 60], raiz=u'//infCad', obrigatorio=False)
        self.xFant = TagCaracter(nome=u'xFant', codigo=u'GR13a', tamanho=[1, 60], raiz=u'//infCad', obrigatorio=False)
        self.xRegApur = TagCaracter(nome=u'xRegApur', codigo=u'GR14', tamanho=[1, 60], raiz=u'//infCad',
                                    obrigatorio=False)
        self.CNAE = TagInteiro(nome=u'CNAE', codigo=u'GR15', tamanho=[6, 7], raiz=u'//infCad', obrigatorio=False)
        self.dIniAtiv = TagData(nome=u'dIniAtiv', codigo=u'GR16', raiz=u'//infCad', obrigatorio=False)
        self.dUltSit = TagData(nome=u'dUltSit', codigo=u'GR17', raiz=u'//infCad', obrigatorio=False)
        self.dBaixa = TagData(nome=u'dBaixa', codigo=u'GR18', raiz=u'//infCad', obrigatorio=False)
        self.IEUnica = TagCaracter(nome=u'IEUnica', codigo=u'GR20', tamanho=[2, 14], raiz=u'//infCad',
                                   obrigatorio=False)
        self.IEAtual = TagCaracter(nome=u'IEAtual', codigo=u'GR21', tamanho=[2, 14], raiz=u'//infCad',
                                   obrigatorio=False)
        self.ender = Ender()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infCad>'
        xml += self.IE.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.UF.xml
        xml += self.cSit.xml
        xml += self.indCredNFe.xml
        xml += self.indCredCTe.xml
        xml += self.xNome.xml
        xml += self.xFant.xml
        xml += self.xRegApur.xml
        xml += self.CNAE.xml
        xml += self.dIniAtiv.xml
        xml += self.dUltSit.xml
        xml += self.dBaixa.xml
        xml += self.IEUnica.xml
        xml += self.IEAtual.xml
        xml += self.ender.xml
        xml += u'</infCad>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.IE.xml = arquivo
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo
            self.UF.xml = arquivo
            self.cSit.xml = arquivo
            self.indCredNFe.xml = arquivo
            self.indCredCTe.xml = arquivo
            self.xNome.xml = arquivo
            self.xFant.xml = arquivo
            self.xRegApur.xml = arquivo
            self.CNAE.xml = arquivo
            self.dIniAtiv.xml = arquivo
            self.dUltSit.xml = arquivo
            self.dBaixa.xml = arquivo
            self.IEUnica.xml = arquivo
            self.IEAtual.xml = arquivo
            self.ender.xml = arquivo

    xml = property(get_xml, set_xml)


class InfCad(conscad_200.InfCad):
    def __init__(self):
        super(InfCad, self).__init__()


class _InfConsRecebido(XMLNFe):
    def __init__(self):
        self.verAplic = TagCaracter(nome=u'verAplic', codigo=u'GR04', tamanho=[1, 20], raiz=u'//retConsCad/infCons')
        self.cStat = TagCaracter(nome=u'cStat', codigo=u'GR05', tamanho=[3, 3, 3], raiz=u'//retConsCad/infCons')
        self.xMotivo = TagCaracter(nome=u'xMotivo', codigo=u'GR06', tamanho=[1, 255], raiz=u'//retConsCad/infCons')
        self.UF = TagCaracter(nome=u'UF', codigo=u'GR06a', tamanho=[2, 2], raiz=u'//retConsCad/infCons')
        self.IE = TagCaracter(nome=u'IE', codigo=u'GR06b', tamanho=[2, 14], raiz=u'//retConsCad/infCons',
                              obrigatorio=False)
        self.CNPJ = TagCaracter(nome=u'CNPJ', codigo=u'GR06c', tamanho=[3, 14], raiz=u'//retConsCad/infCons',
                                obrigatorio=False)
        self.CPF = TagCaracter(nome=u'CPF', codigo=u'GR06d', tamanho=[3, 11], raiz=u'//retConsCad/infCons',
                               obrigatorio=False)
        self.dhCons = TagDataHora(nome=u'dhCons', codigo=u'GR06e', raiz=u'//retConsCad/infCons')
        self.cUF = TagInteiro(nome=u'cUF', codigo=u'GR06f', tamanho=[2, 2, 2], raiz=u'//retConsCad/infCons')
        self.infCad = []

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infCons>'
        xml += self.verAplic.xml
        xml += self.cStat.xml
        xml += self.xMotivo.xml
        xml += self.UF.xml
        xml += self.IE.xml
        xml += self.CNPJ.xml
        xml += self.CPF.xml
        xml += self.dhCons.xml
        xml += self.cUF.xml

        for ic in self.infCad:
            xml += ic.xml

        xml += u'</infCons>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.verAplic.xml = arquivo
            self.cStat.xml = arquivo
            self.xMotivo.xml = arquivo
            self.UF.xml = arquivo
            self.IE.xml = arquivo
            self.CNPJ.xml = arquivo
            self.CPF.xml = arquivo
            self.dhCons.xml = arquivo
            self.cUF.xml = arquivo

            self.infCad = self.le_grupo('//retConsCad/infCons/infCad', _InfCadRecebido)

    xml = property(get_xml, set_xml)


class RetConsCad(conscad_200.RetConsCad):
    def __init__(self):
        super(RetConsCad, self).__init__()
        self.versao = TagDecimal(nome=u'retConsCad', codigo=u'GR01', propriedade=u'versao', namespace=NAMESPACE_NFE, valor=u'3.10', raiz=u'/')
        self.infCons = _InfConsRecebido()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'retConsCad_v2.00.xsd'

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA
        xml += self.versao.xml
        xml += self.infCons.xml
        xml += u'</retConsCad>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml  = arquivo
            self.infCons.xml = arquivo

    xml = property(get_xml, set_xml)
