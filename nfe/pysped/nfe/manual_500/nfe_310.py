# -*- coding: utf-8 -*-


import os
from nfe.pysped.xml_sped import *
from nfe.pysped.nfe.manual_401 import nfe_200
from nfe.pysped.nfe.manual_500 import ESQUEMA_ATUAL


DIRNAME = os.path.dirname(__file__)


class Deduc(nfe_200.Deduc):
    def __init__(self):
        super(Deduc, self).__init__()


class ForDia(nfe_200.ForDia):
    def __init__(self):
        super(ForDia, self).__init__()


class Cana(nfe_200.Cana):
    def __init__(self):
        super(Cana, self).__init__()


class ISSQN(nfe_200.ISSQN):
    def __init__(self):
        super(ISSQN, self).__init__()
        #removido na versao 3.10
        self.cSitTrib  = TagCaracter(nome=u'cSitTrib', codigo=u'U07', tamanho=[1,  1], raiz=u'//det/imposto/ISSQN',obrigatorio=False)
        #alterando tipo e tamanho
        self.cListServ = TagCaracter(nome=u'cListServ', codigo=u'U06', tamanho=[1,  5], raiz=u'//det/imposto/ISSQN')

        #adicionando campos 3.10
        self.vDeducao = TagDecimal(nome=u'vDeducao', codigo=u'U07', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz=u'//det/imposto/ISSQN')
        self.vOutro = TagDecimal(nome=u'vOutro', codigo=u'U08', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz=u'//det/imposto/ISSQN')
        self.vDescIncond = TagDecimal(nome=u'vDescIncond', codigo=u'U09', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz=u'//det/imposto/ISSQN')
        self.vDescCond = TagDecimal(nome=u'vDescCond', codigo=u'U10', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz=u'//det/imposto/ISSQN')
        self.vISSRet = TagDecimal(nome=u'vISSRet', codigo=u'U11', tamanho=[1, 15, 1], decimais=[1,  2,  2], raiz=u'//det/imposto/ISSQN')
        self.indISS = TagCaracter(nome=u'indISS', codigo=u'U12', tamanho=[1,  1], raiz=u'//det/imposto/ISSQN')
        self.cServico = TagCaracter(nome=u'cServico', codigo=u'U13', tamanho=[1,  1], raiz=u'//det/imposto/ISSQN')
        self.cMun = TagCaracter(nome=u'cMun', codigo=u'U14', tamanho=[1,  1], raiz=u'//det/imposto/ISSQN')
        self.cPais = TagCaracter(nome=u'cPais', codigo=u'U15', tamanho=[1,  1], raiz=u'//det/imposto/ISSQN')
        self.nProcesso = TagCaracter(nome=u'nProcesso', codigo=u'U16', tamanho=[1,  1], raiz=u'//det/imposto/ISSQN')
        self.indIncentivo = TagCaracter(nome=u'indIncentivo', codigo=u'U17', tamanho=[1,  1], raiz=u'//det/imposto/ISSQN')


    def get_xml(self):

        xml = XMLNFe.get_xml(self)
        xml += u'<ISSQN>'
        xml += self.vBC.xml
        xml += self.vAliq.xml
        xml += self.vISSQN.xml
        xml += self.cMunFG.xml
        xml += self.cListServ.xml
        #novos 3.10
        xml += self.vDeducao.xml
        xml += self.vOutro.xml
        xml += self.vDescIncond.xml
        xml += self.vDescCond.xml
        xml += self.vISSRet.xml
        xml += self.indISS.xml
        xml += self.cServico.xml
        xml += self.cMun.xml
        xml += self.cPais.xml
        xml += self.nProcesso.xml
        xml += self.indIncentivo.xml

        xml += u'</ISSQN>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml       = arquivo
            self.vAliq.xml     = arquivo
            self.vISSQN.xml    = arquivo
            self.cMunFG.xml    = arquivo
            self.cListServ.xml = arquivo
            #novos campos  3.10
            self.vDeducao.xml = arquivo
            self.vOutro.xml = arquivo
            self.vDescIncond.xml = arquivo
            self.vDescCond.xml = arquivo
            self.vISSRet.xml = arquivo
            self.indISS.xml = arquivo
            self.cServico.xml = arquivo
            self.cMun.xml = arquivo
            self.cPais.xml = arquivo
            self.nProcesso.xml = arquivo
            self.indIncentivo.xml = arquivo


    xml = property(get_xml, set_xml)



class COFINSST(nfe_200.COFINSST):
    def __init__(self):
        super(COFINSST, self).__init__()


class TagCSTCOFINS(nfe_200.TagCSTCOFINS):
    def __init__(self, *args, **kwargs):
        super(TagCSTCOFINS, self).__init__(*args, **kwargs)


class COFINS(nfe_200.COFINS):
    def __init__(self):
        super(COFINS, self).__init__()


class PISST(nfe_200.PISST):
    def __init__(self):
        super(PISST, self).__init__()


class TagCSTPIS(nfe_200.TagCSTPIS):
    def __init__(self, *args, **kwargs):
        super(TagCSTPIS, self).__init__(*args, **kwargs)


class PIS(nfe_200.PIS):
    def __init__(self):
        super(PIS, self).__init__()


class II(nfe_200.II):
    def __init__(self):
        super(II, self).__init__()


class TagCSTIPI(nfe_200.TagCSTIPI):
    def __init__(self, *args, **kwargs):
        super(TagCSTIPI, self).__init__(*args, **kwargs)


class IPI(nfe_200.IPI):
    def __init__(self):
        super(IPI, self).__init__()


class TagCSOSN(nfe_200.TagCSOSN):
    def __init__(self, *args, **kwargs):
        super(TagCSOSN, self).__init__(*args, **kwargs)


class TagCSTICMS(nfe_200.TagCSTICMS):
    def __init__(self, *args, **kwargs):
        super(TagCSTICMS, self).__init__(*args, **kwargs)
        self.nome = u'CST'
        self.codigo = u'N12'
        self.tamanho = [2, 2]
        self.raiz = u''
        self.grupo_icms = None

    def set_valor(self, novo_valor):
        super(TagCSTICMS, self).set_valor(novo_valor)

        if not self.grupo_icms:
            return None

        #
        # Definimos todas as tags como não obrigatórias
        #
        self.grupo_icms.modBC.obrigatorio       = False
        self.grupo_icms.vBC.obrigatorio         = False
        self.grupo_icms.pRedBC.obrigatorio      = False
        self.grupo_icms.pICMS.obrigatorio       = False
        self.grupo_icms.vICMS.obrigatorio       = False
        self.grupo_icms.modBCST.obrigatorio     = False
        self.grupo_icms.pMVAST.obrigatorio      = False
        self.grupo_icms.pRedBCST.obrigatorio    = False
        self.grupo_icms.vBCST.obrigatorio       = False
        self.grupo_icms.pICMSST.obrigatorio     = False
        self.grupo_icms.vICMSST.obrigatorio     = False
        self.grupo_icms.motDesICMS.obrigatorio  = False
        self.grupo_icms.vBCSTRet.obrigatorio    = False
        self.grupo_icms.vICMSSTRet.obrigatorio  = False
        self.grupo_icms.vBCSTDest.obrigatorio   = False
        self.grupo_icms.vICMSSTDest.obrigatorio = False
        self.grupo_icms.UFST.obrigatorio        = False
        self.grupo_icms.pBCOp.obrigatorio       = False
        #campos versao 3.10
        self.grupo_icms.vICMSDeson.obrigatorio = False
        self.grupo_icms.motDesICMS.obrigatorio = False

        #
        # Por segurança, zeramos os valores das tags do
        # grupo ICMS ao redefinirmos o código da situação
        # tributária
        #
        self.grupo_icms.modBC.valor       = 3
        self.grupo_icms.vBC.valor         = u'0.00'
        self.grupo_icms.pRedBC.valor      = u'0.00'
        self.grupo_icms.pICMS.valor       = u'0.00'
        self.grupo_icms.vICMS.valor       = u'0.00'
        self.grupo_icms.modBCST.valor     = 4
        self.grupo_icms.pMVAST.valor      = u'0.00'
        self.grupo_icms.pRedBCST.valor    = u'0.00'
        self.grupo_icms.vBCST.valor       = u'0.00'
        self.grupo_icms.pICMSST.valor     = u'0.00'
        self.grupo_icms.vICMSST.valor     = u'0.00'
        self.grupo_icms.motDesICMS.valor  = 0
        self.grupo_icms.vBCSTRet.valor    = u'0.00'
        self.grupo_icms.vICMSSTRet.valor  = u'0.00'
        self.grupo_icms.vBCSTDest.valor   = u'0.00'
        self.grupo_icms.vICMSSTDest.valor = u'0.00'
        self.grupo_icms.UFST.valor        = u''
        self.grupo_icms.pBCOp.valor       = u'0.00'
        #campos versao 3.10
        self.grupo_icms.vICMSDeson.valor = u'0.00'
        self.grupo_icms.motDesICMS.valor = u'0.00'

        #
        # Para cada código de situação tributária,
        # redefinimos a raiz e a obrigatoriedade das
        # tags do grupo de ICMS
        #
        if self.valor == u'00':
            self.grupo_icms.nome_tag = u'ICMS00'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS00'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True

        elif self.valor == u'10':
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True

            if not self.grupo_icms.partilha:
                self.grupo_icms.nome_tag = u'ICMS10'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS10'
            else:
                self.grupo_icms.nome_tag = u'ICMSPart'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSPart'
                self.grupo_icms.pBCOp.obrigatorio    = True
                self.grupo_icms.UFST.obrigatorio     = True

        elif self.valor == u'20':
            self.grupo_icms.nome_tag = u'ICMS20'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS20'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pRedBC.obrigatorio   = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            #novo campos 3.10
            self.grupo_icms.vICMSDeson.obrigatorio = True
            self.grupo_icms.motDesICMS.obrigatorio = True



        elif self.valor == u'30':
            self.grupo_icms.nome_tag = u'ICMS30'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS30'
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True
            #novo campos 3.10
            self.grupo_icms.vICMSDeson.obrigatorio = True
            self.grupo_icms.motDesICMS.obrigatorio = True



        elif self.valor in (u'40', u'41', u'50'):
            if self.grupo_icms.repasse and self.valor == u'41':
                self.grupo_icms.nome_tag = u'ICMSST'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSST'
                self.grupo_icms.vBCSTRet.obrigatorio    = True
                self.grupo_icms.vICMSSTRet.obrigatorio  = True
                self.grupo_icms.vBCSTDest.obrigatorio   = True
                self.grupo_icms.vICMSSTDest.obrigatorio = True
                #novo campos 3.10
                self.grupo_icms.vICMSDeson.obrigatorio = True
                self.grupo_icms.motDesICMS.obrigatorio = True
            else:
                self.grupo_icms.nome_tag = u'ICMS40'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS40'
                #novo campos 3.10
                self.grupo_icms.vICMSDeson.obrigatorio = True
                self.grupo_icms.motDesICMS.obrigatorio = True

        elif self.valor == u'51':
            self.grupo_icms.nome_tag = u'ICMS51'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS51'

        elif self.valor == u'60':
            self.grupo_icms.nome_tag = u'ICMS60'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS60'
            self.grupo_icms.vBCSTRet.obrigatorio   = True
            self.grupo_icms.vICMSSTRet.obrigatorio = True

        elif self.valor == u'70':
            self.grupo_icms.nome_tag = u'ICMS70'
            self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS70'
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pRedBC.obrigatorio   = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True
            #novo campos 3.10
            self.grupo_icms.vICMSDeson.obrigatorio = True
            self.grupo_icms.motDesICMS.obrigatorio = True

        elif self.valor == u'90':
            self.grupo_icms.modBC.obrigatorio    = True
            self.grupo_icms.vBC.obrigatorio      = True
            self.grupo_icms.pICMS.obrigatorio    = True
            self.grupo_icms.vICMS.obrigatorio    = True
            self.grupo_icms.modBCST.obrigatorio  = True
            self.grupo_icms.vBCST.obrigatorio    = True
            self.grupo_icms.pICMSST.obrigatorio  = True
            self.grupo_icms.vICMSST.obrigatorio  = True
            #novo campos 3.10
            self.grupo_icms.vICMSDeson.obrigatorio = True
            self.grupo_icms.motDesICMS.obrigatorio = True

            if not self.grupo_icms.partilha:
                self.grupo_icms.nome_tag = u'ICMS90'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMS90'
            else:
                self.grupo_icms.nome_tag = u'ICMSPart'
                self.grupo_icms.raiz_tag = u'//det/imposto/ICMS/ICMSPart'
                self.grupo_icms.pBCOp.obrigatorio    = True
                self.grupo_icms.UFST.obrigatorio     = True

        #
        # Redefine a raiz para todas as tags do grupo ICMS
        #
        self.grupo_icms.orig.raiz        = self.grupo_icms.raiz_tag
        self.grupo_icms.CST.raiz         = self.grupo_icms.raiz_tag
        self.grupo_icms.modBC.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.vBC.raiz         = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBC.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMS.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMS.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.modBCST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.pMVAST.raiz      = self.grupo_icms.raiz_tag
        self.grupo_icms.pRedBCST.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCST.raiz       = self.grupo_icms.raiz_tag
        self.grupo_icms.pICMSST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSST.raiz     = self.grupo_icms.raiz_tag
        self.grupo_icms.motDesICMS.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCSTRet.raiz    = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSSTRet.raiz  = self.grupo_icms.raiz_tag
        self.grupo_icms.vBCSTDest.raiz   = self.grupo_icms.raiz_tag
        self.grupo_icms.vICMSSTDest.raiz = self.grupo_icms.raiz_tag
        self.grupo_icms.UFST.raiz        = self.grupo_icms.raiz_tag
        self.grupo_icms.pBCOp.raiz       = self.grupo_icms.raiz_tag

    def get_valor(self):
        return self._valor_string

    valor = property(get_valor, set_valor)


class ICMS(nfe_200.ICMS):
    def __init__(self):
        super(ICMS, self).__init__()


class Imposto(nfe_200.Imposto):
    def __init__(self):
        super(Imposto, self).__init__()


class CIDE(nfe_200.CIDE):
    def __init__(self):
        super(CIDE, self).__init__()


class Comb(nfe_200.Comb):
    def __init__(self):
        super(Comb, self).__init__()
        self.pMixGN = TagInteiro(nome=u'pMixGN', codigo=u'L102a', tamanho=[2, 4],raiz=u'//det/prod/comb', obrigatorio=False)
        self.nRECOPI = TagInteiro(nome=u'nRECOPI', codigo=u'L109', tamanho=[20, 20, 20], raiz=u'//det/prod/comb')

    def get_xml(self):
        if not self.cProdANP.valor:
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<comb>'
        xml += self.cProdANP.xml
        xml += self.pMixGN.xml
        xml += self.CODIF.xml
        xml += self.qTemp.xml
        xml += self.UFCons.xml
        xml += self.CIDE.xml
        xml += self.nRECOPI.xml
        xml += u'</comb>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProdANP.xml  = arquivo
            self.pMixGN.xml    = arquivo
            self.CODIF.xml     = arquivo
            self.qTemp.xml     = arquivo
            self.UFCons.xml    = arquivo
            self.CIDE.xml      = arquivo
            self.nRECOPI.xml   = arquivo

    xml = property(get_xml, set_xml)


class Arma(nfe_200.Arma):
    def __init__(self):
        super(Arma, self).__init__()


class Med(nfe_200.Med):
    def __init__(self):
        super(Med, self).__init__()


class VeicProd(nfe_200.VeicProd):
    def __init__(self):
        super(VeicProd, self).__init__()


class Adi(nfe_200.Adi):
    def __init__(self):
        super(Adi, self).__init__()
        self.nDraw = TagInteiro(nome=u'nDraw'     , codigo=u'I29a' , tamanho=[11,  11], raiz=u'//DI')



class DI(nfe_200.DI):
    def __init__(self):
        super(DI, self).__init__()
        self.nDI         = TagCaracter(nome=u'nDI'        , codigo=u'I19', tamanho=[1, 10], raiz=u'//DI')
        self.dDI         = TagData(nome=u'dDI'            , codigo=u'I20',                  raiz=u'//DI')
        self.xLocDesemb  = TagCaracter(nome=u'xLocDesemb' , codigo=u'I21', tamanho=[1, 60], raiz=u'//DI')
        self.UFDesemb    = TagCaracter(nome=u'UFDesemb'   , codigo=u'I22', tamanho=[2,  2], raiz=u'//DI')
        self.dDesemb     = TagData(nome=u'dDesemb'        , codigo=u'I23',                  raiz=u'//DI')
        #implementacao de novos campos para nf-e 3.10
        self.tpViaTransp = TagInteiro(nome=u'tpViaTransp', codigo=u'I23a', tamanho=[2, 2,]),
        self.vAFRMM      = TagInteiro(nome=u'vAFRMM'     , codigo=u'I23b' , tamanho=[13,  13], raiz=u'//DI'),
        self.tpIntermedio = TagInteiro(nome=u'tpIntermedio'     , codigo=u'I23c' , tamanho=[1,  1], raiz=u'//DI'),
        self.CNPJ    = TagCaracter(nome=u'CNPJ'   , codigo=u'I23d' , tamanho=[ 0, 14]   , raiz=u'//DI'),
        self.UFTerceiro    = TagCaracter(nome=u'UFTerceiro'   , codigo=u'I23e' , tamanho=[ 0, 2]   , raiz=u'//DI')
        ###
        self.cExportador = TagCaracter(nome=u'cExportador', codigo=u'I24', tamanho=[1, 60], raiz=u'//DI')
        self.adi         = [Adi()]

    def get_xml(self):
        if not self.nDI:
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<DI>'
        xml += self.nDI.xml
        xml += self.dDI.xml
        xml += self.xLocDesemb.xml
        xml += self.UFDesemb.xml
        xml += self.dDesemb.xml
        xml += self.tpViaTransp.xml
        xml += self.vAFRMM.xml
        xml += self.tpIntermedio.xml
        xml += self.CNPJ.xml
        xml += self.UFTerceiro.xml
        xml += self.cExportador.xml

        for a in self.adi:
            xml += a.xml

        xml += u'</DI>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nDI.xml     = arquivo
            self.dDI.xml     = arquivo
            self.xLocDesemb  = arquivo
            self.UFDesemb    = arquivo
            self.dDesemb     = arquivo
            #novos 3.10
            self.tpViaTransp.xml = arquivo
            self.vAFRMM.xml = arquivo
            self.tpIntermedio.xml = arquivo
            self.CNPJ.xml = arquivo
            self.UFTerceiro.xml = arquivo
            #
            self.cExportador = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            adis = self._le_nohs('//DI/adi')
            self.adi = []
            if adis is not None:
                self.adi = [_Adi() for a in adis]
                for i in range(len(adis)):
                    self.adi[i].xml = adis[i]

    xml = property(get_xml, set_xml)


class exportInd(XMLNFe):
    def __init__(self):
        super(exportInd, self).__init__()
        self.nRE = TagDecimal(nome=u'nRE', codigo=u'I53', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//exportInd')
        self.chNFe = TagDecimal(nome=u'chNFe'  , codigo=u'I54', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//exportInd')
        self.qExport = TagDecimal(nome=u'qExport'  , codigo=u'I55', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//exportInd')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<exportInd>'
        xml += self.nRE.xml
        xml += self.chNFe.xml
        xml += self.qExport.xml
        xml += u'</exportInd>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nRE.xml = arquivo
            self.chNFe.xml = arquivo
            self.qExport.xml = arquivo


    xml = property(get_xml, set_xml)


class detExport(XMLNFe):
    def __init__(self):
        super(detExport, self).__init__()
        self.nDraw = TagDecimal(nome=u'nDraw'  , codigo=u'I51', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//detExport')
        self.exportInd  = exportInd()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<detExport>'
        xml += self.nDraw.xml
        xml += self.exportInd.xml
        xml += u'</detExport>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nDraw.xml = arquivo
            self.exportInd.xml= arquivo


    xml = property(get_xml, set_xml)


class Prod(nfe_200.Prod):
    def __init__(self):
        super(Prod, self).__init__()
        self.NCM      = TagCaracter(nome=u'NCM'     , codigo=u'I05' , tamanho=[2,  8]                        , raiz=u'//det/prod'),
        self.NVE      = TagCaracter(nome=u'NVE'     , codigo=u'I05a' , tamanho=[2,  8]                        , raiz=u'//det/prod',obrigatorio=False),
        self.qCom     = TagDecimal(nome=u'qCom'     , codigo=u'I10' , tamanho=[1, 15, 1], decimais=[0,  4, 4], raiz=u'//det/prod')
        self.vUnCom   = TagDecimal(nome=u'vUnCom'   , codigo=u'I10a', tamanho=[1, 21, 1], decimais=[0, 10, 4], raiz=u'//det/prod')
        self.qTrib    = TagDecimal(nome=u'qTrib'    , codigo=u'I14' , tamanho=[1, 15, 1], decimais=[0,  4, 4], raiz=u'//det/prod')
        self.vUnTrib  = TagDecimal(nome=u'vUnTrib'  , codigo=u'I14a', tamanho=[1, 21, 1], decimais=[0, 10, 4], raiz=u'//det/prod')
        self.vOutro   = TagDecimal(nome=u'vOutro'   , codigo=u'I17a', tamanho=[1, 15, 1], decimais=[0,  2, 2], raiz=u'//det/prod', obrigatorio=False)
        self.indTot   = TagInteiro(nome=u'indTot'   , codigo=u'I17b', tamanho=[1,  1, 1],                      raiz=u'//det/prod', valor=1)
        self.xPed     = TagCaracter(nome=u'xPed'    , codigo=u'I30' , tamanho=[1, 15],                         raiz=u'//det/prod', obrigatorio=False)
        self.nItemPed = TagCaracter(nome=u'nItemPed', codigo=u'I31' , tamanho=[1,  6],                         raiz=u'//det/prod', obrigatorio=False)
        self.nFCI     = TagCaracter(nome=u'nFCI', codigo=u'I70', tamanho=[1,36],                               raiz=u'//det/prod', obrigatorio=False)
        self.veicProd = VeicProd()
        self.comb     = Comb()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<prod>'
        xml += self.cProd.xml
        xml += self.cEAN.xml
        xml += self.xProd.xml
        xml += self.NCM.xml
        xml += self.NVE.xml
        xml += self.EXTIPI.xml
        #xml += self.genero.xml
        xml += self.CFOP.xml
        xml += self.uCom.xml
        xml += self.qCom.xml
        xml += self.vUnCom.xml
        xml += self.vProd.xml
        xml += self.cEANTrib.xml
        xml += self.uTrib.xml
        xml += self.qTrib.xml
        xml += self.vUnTrib.xml
        xml += self.vFrete.xml
        xml += self.vSeg.xml
        xml += self.vDesc.xml
        xml += self.vOutro.xml
        xml += self.indTot.xml

        for d in self.DI:
            xml += d.xml

        xml += self.xPed.xml
        xml += self.nItemPed.xml
        xml += self.nFCI.xml
        xml += self.veicProd.xml

        for m in self.med:
            xml += m.xml

        for a in self.arma:
            xml += a.xml

        xml += self.comb.xml
        xml += u'</prod>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cProd.xml    = arquivo
            self.cEAN.xml     = arquivo
            self.xProd.xml    = arquivo
            self.NCM.xml      = arquivo
            self.NVE.xml      = arquivo
            self.EXTIPI.xml   = arquivo
            self.genero.xml   = arquivo
            self.CFOP.xml     = arquivo
            self.uCom.xml     = arquivo
            self.qCom.xml     = arquivo
            self.vUnCom.xml   = arquivo
            self.vProd.xml    = arquivo
            self.cEANTrib.xml = arquivo
            self.uTrib.xml    = arquivo
            self.qTrib.xml    = arquivo
            self.vUnTrib.xml  = arquivo
            self.vFrete.xml   = arquivo
            self.vSeg.xml     = arquivo
            self.vDesc.xml    = arquivo
            self.vOutro.xml   = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.DI = self.le_grupo('//det/prod/DI', DI)
            self.nFCI.xml = arquivo
            self.veicProd.xml = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.med = self.le_grupo('//det/prod/med', Med)
            self.arma = self.le_grupo('//det/prod/arma', Arma)

            self.comb.xml = arquivo

    xml = property(get_xml, set_xml)

class Det(nfe_200.Det):
    def __init__(self):
        super(Det, self).__init__()


class Compra(nfe_200.Compra):
    def __init__(self):
        super(Compra, self).__init__()


class Exporta(nfe_200.Exporta):
    def __init__(self):
        super(Exporta, self).__init__()


class ProcRef(nfe_200.ProcRef):
    def __init__(self):
        super(ProcRef, self).__init__()


class ObsFisco(nfe_200.ObsFisco):
    def __init__(self):
        super(ObsFisco, self).__init__()


class ObsCont(nfe_200.ObsCont):
    def __init__(self):
        super(ObsCont, self).__init__()


class InfAdic(nfe_200.InfAdic):
    def __init__(self):
        super(InfAdic, self).__init__()


class Dup(nfe_200.Dup):
    def __init__(self):
        super(Dup, self).__init__()


class Fat(nfe_200.Fat):
    def __init__(self):
        super(Fat, self).__init__()


class Cobr(nfe_200.Cobr):
    def __init__(self):
        super(Cobr, self).__init__()

class Card(XMLNFe):
    # Cartoes de credito = NFC-e.
    def __init__(self):
        super(Card, self).__init__()
        self.CNPJ = TagCaracter(nome=u'CNPJ',   codigo=u'YA05', tamanho=[0, 14], raiz=u'//card')
        self.tBand = TagCaracter(nome=u'tBand', codigo=u'YA06', tamanho=[2,2,2], raiz=u'//card')
        self.cAut = TagCaracter(nome=u'cAut',   codigo=u'YA07', tamanho=[1, 20], decimais=[0, 2, 2], raiz=u'//card')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<card>'
        xml += self.CNPJ.xml
        xml += self.tBand.xml
        xml += self.cAut.xml
        xml += u'</card>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml = arquivo
            self.tBand.xml = arquivo
            self.cAut.xml = arquivo


    xml = property(get_xml, set_xml)

class Pag(XMLNFe):

     # Formas de pagamento NFC-e.
    def __init__(self):
        super(Pag, self).__init__()
        self.tPag = TagCaracter(nome=u'tPag', codigo=u'YA02', tamanho=[2,2,2], raiz=u'//ide/pag')
        self.vPag = TagDecimal(nome=u'vPag'  , codigo=u'YA03', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz=u'//ide/pag')
        self.card = Card()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<pag>'
        xml += self.tPag.xml
        xml += self.vPag.xml
        xml += self.card.xml
        xml += u'</pag>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.nRE.xml = arquivo
            self.chNFe.xml = arquivo
            self.card.xml = arquivo


    xml = property(get_xml, set_xml)


class Lacres(nfe_200.Lacres):
    def __init__(self):
        super(Lacres, self).__init__()


class Vol(nfe_200.Vol):
    def __init__(self, xml=None):
        super(Vol, self).__init__()


class Reboque(nfe_200.Reboque):
    def __init__(self):
        super(Reboque, self).__init__()


class VeicTransp(nfe_200.VeicTransp):
    def __init__(self):
        super(VeicTransp, self).__init__()


class RetTransp(nfe_200.RetTransp):
    def __init__(self):
        super(RetTransp, self).__init__()


class Transporta(nfe_200.Transporta):
    def __init__(self):
        super(Transporta, self).__init__()


class Transp(nfe_200.Transp):
    def __init__(self):
        super(Transp, self).__init__()


class RetTrib(nfe_200.RetTrib):
    def __init__(self):
        super(RetTrib, self).__init__()


class ISSQNTot(nfe_200.ISSQNTot):
    def __init__(self):
        super(ISSQNTot, self).__init__()
        self.dCompet = TagDataHora(nome=u'dCompet', codigo=u'W22a', raiz=u'//NFe/infNFe/total/ISSQNtot')
        self.vDeducao = TagDecimal(nome=u'vDeducao', codigo=u'W22b', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vOutro = TagDecimal(nome=u'vOutro', codigo=u'W22c', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vDescIncond = TagDecimal(nome=u'vDescIncond', codigo=u'W22d', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vDescCond = TagDecimal(nome=u'vDescCond', codigo=u'W22e', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.vISSRet = TagDecimal(nome=u'vISSRet', codigo=u'W22f', tamanho=[1, 13, 1], decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)
        self.cRegTrib = TagCaracter(nome=u'cRegTrib', codigo=u'W22g', tamanho=[1, 2],  raiz=u'//NFe/infNFe/total/ISSQNtot', obrigatorio=False)


    def get_xml(self):
        if not (self.vServ.valor or self.vBC.valor or self.vISS.valor or self.vPIS.valor or self.vCOFINS.valor):
            return u''

        xml = XMLNFe.get_xml(self)
        xml += u'<ISSQNtot>'
        xml += self.vServ.xml
        xml += self.vBC.xml
        xml += self.vISS.xml
        xml += self.vPIS.xml
        xml += self.vCOFINS.xml
        #versao 3.10
        xml += self.dCompet.xml
        xml += self.vDeducao.xml
        xml += self.vOutro.xml
        xml += self.vDescIncond.xml
        xml += self.vDescCond.xml
        xml += self.vISSRet.xml
        xml += self.cRegTrib.xml
        xml += u'</ISSQNtot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vServ.xml   = arquivo
            self.vBC.xml     = arquivo
            self.vISS.xml    = arquivo
            self.vPIS.xml    = arquivo
            self.vCOFINS.xml = arquivo
            #versao 3.10
            self.dCompet.xml = arquivo
            self.vDeducao.xml = arquivo
            self.vOutro.xml = arquivo
            self.vDescIncond.xml = arquivo
            self.vDescCond.xml = arquivo
            self.vISSRet.xml = arquivo
            self.cRegTrib.xml = arquivo

    xml = property(get_xml, set_xml)


class ICMSTot(nfe_200.ICMSTot):
    def __init__(self):
        super(ICMSTot, self).__init__()
        self.vICMSDeson  = TagDecimal(nome=u'vICMSDeson'  , codigo=u'W04a', tamanho=[1, 15, 1],
                                      decimais=[0, 2, 2], raiz=u'//NFe/infNFe/total/ICMSTot',valor=u'0.00')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<ICMSTot>'
        xml += self.vBC.xml
        xml += self.vICMS.xml
        xml += self.vICMSDeson.xml
        xml += self.vBCST.xml
        xml += self.vST.xml
        xml += self.vProd.xml
        xml += self.vFrete.xml
        xml += self.vSeg.xml
        xml += self.vDesc.xml
        xml += self.vII.xml
        xml += self.vIPI.xml
        xml += self.vPIS.xml
        xml += self.vCOFINS.xml
        xml += self.vOutro.xml
        xml += self.vNF.xml
        xml += self.vTotTrib.xml
        xml += u'</ICMSTot>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.vBC.xml     = arquivo
            self.vICMS.xml   = arquivo
            self.vICMSDeson.xml   = arquivo
            self.vBCST.xml   = arquivo
            self.vST.xml     = arquivo
            self.vProd.xml   = arquivo
            self.vFrete.xml  = arquivo
            self.vSeg.xml    = arquivo
            self.vDesc.xml   = arquivo
            self.vII.xml     = arquivo
            self.vIPI.xml    = arquivo
            self.vPIS.xml    = arquivo
            self.vCOFINS.xml = arquivo
            self.vOutro.xml  = arquivo
            self.vNF.xml     = arquivo
            self.vTotTrib.xml = arquivo

    xml = property(get_xml, set_xml)


class Total(nfe_200.Total):
    def __init__(self):
        super(Total, self).__init__()
        self.ICMSTot = ICMSTot()
        self.ISSQNTot = ISSQNTot()
        self.retTrib  = RetTrib()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<total>'
        xml += self.ICMSTot.xml
        xml += self.ISSQNTot.xml
        xml += self.retTrib.xml
        xml += u'</total>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.ICMSTot.xml  = arquivo
            self.ISSQNTot.xml = arquivo
            self.retTrib.xml  = arquivo

    xml = property(get_xml, set_xml)

class Entrega(nfe_200.Entrega):
    def __init__(self):
        super(Entrega, self).__init__()


class Retirada(nfe_200.Retirada):
    def __init__(self):
        super(Retirada, self).__init__()



class autXML(XMLNFe):
    def __init__(self):
        super(autXML, self).__init__()
        self.CNPJ      = TagCaracter(nome=u'CNPJ' , codigo=u'G51', tamanho=[0 , 14]   , raiz=u'//NFe/infNFe/autXML', obrigatorio=False)
        self.CPF       = TagCaracter(nome=u'CPF'  , codigo=u'G52', tamanho=[11, 11]   , raiz=u'//NFe/infNFe/autXML', obrigatorio=False)
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<autXML>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml
        xml += u'</autXML>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo

    xml = property(get_xml, set_xml)

class EnderDest(nfe_200.EnderDest):
    def __init__(self):
        super(EnderDest, self).__init__()

        self.xLgr    = TagCaracter(nome=u'xLgr'   , codigo=u'E06', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/dest/enderDest')
        self.nro     = TagCaracter(nome=u'nro'    , codigo=u'E07', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/dest/enderDest')
        self.xCpl    = TagCaracter(nome=u'xCpl'   , codigo=u'E08', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.xBairro = TagCaracter(nome=u'xBairro', codigo=u'E09', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/dest/enderDest')
        self.cMun    = TagInteiro(nome=u'cMun'    , codigo=u'E10', tamanho=[ 7,  7, 7], raiz=u'//NFe/infNFe/dest/enderDest')
        self.xMun    = TagCaracter(nome=u'xMun'   , codigo=u'E11', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/dest/enderDest')
        self.UF      = TagCaracter(nome=u'UF'     , codigo=u'E12', tamanho=[ 2,  2]   , raiz=u'//NFe/infNFe/dest/enderDest')
        self.CEP     = TagCaracter(nome=u'CEP'    , codigo=u'E13', tamanho=[ 8,  8, 8], raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.cPais   = TagInteiro(nome=u'cPais'   , codigo=u'E14', tamanho=[ 4,  4, 4], raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.xPais   = TagCaracter(nome=u'xPais'  , codigo=u'E15', tamanho=[ 1, 60]   , raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)
        self.fone    = TagInteiro(nome=u'fone'    , codigo=u'E16', tamanho=[ 1, 10]   , raiz=u'//NFe/infNFe/dest/enderDest', obrigatorio=False)
        # self.indIEDest    = TagCaracter(nome=u'indIEDest'    , codigo=u'E16a', tamanho=[ 1, 1], raiz=u'//NFe/infNFe/dest/enderDest', valor=u'9')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<enderDest>'
        xml += self.xLgr.xml
        xml += self.nro.xml
        xml += self.xCpl.xml
        xml += self.xBairro.xml
        xml += self.cMun.xml
        xml += self.xMun.xml
        xml += self.UF.xml
        xml += self.CEP.xml
        xml += self.cPais.xml
        xml += self.xPais.xml
        xml += self.fone.xml
        # xml += self.indIEDest.xml
        xml += u'</enderDest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.xLgr.xml    = arquivo
            self.nro.xml     = arquivo
            self.xCpl.xml    = arquivo
            self.xBairro.xml = arquivo
            self.cMun.xml    = arquivo
            self.xMun.xml    = arquivo
            self.UF.xml      = arquivo
            self.CEP.xml     = arquivo
            self.cPais.xml   = arquivo
            self.xPais.xml   = arquivo
            self.fone.xml    = arquivo
            # self.indIEDest.xml = arquivo

    xml = property(get_xml, set_xml)

class Dest(nfe_200.Dest):
    def __init__(self):
        super(Dest, self).__init__()
        self.enderDest = EnderDest()
        self.idEstrangeiro    = TagCaracter(nome=u'idEstrangeiro'    , codigo=u'E03a', tamanho=[ 5, 20]   , raiz=u'//NFe/infNFe/dest',obrigatorio=False)
        self.IE        = TagCaracter(nome=u'IE'   , codigo=u'E17', tamanho=[ 2, 14]   , raiz=u'//NFe/infNFe/dest',obrigatorio=False)
        self.xNome     = TagCaracter(nome=u'xNome', codigo=u'E04', tamanho=[ 2, 60]   , raiz=u'//NFe/infNFe/dest',obrigatorio=False)
        self.indIEDest    = TagCaracter(nome=u'indIEDest'    , codigo=u'E16a', tamanho=[ 1, 1], raiz=u'//NFe/infNFe/dest', valor=u'9')
    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<dest>'

        if self.CPF.valor:
            xml += self.CPF.xml
        else:
            xml += self.CNPJ.xml
        xml += self.idEstrangeiro.xml
        xml += self.xNome.xml
        xml += self.enderDest.xml
        xml += self.indIEDest.xml
        xml += self.IE.xml
        xml += self.ISUF.xml
        xml += self.email.xml
        xml += u'</dest>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.CNPJ.xml      = arquivo
            self.CPF.xml       = arquivo
            self.idEstrangeiro.xml  = arquivo
            self.xNome.xml     = arquivo
            self.enderDest.xml = arquivo
            self.indIEDest.xml = arquivo
            self.IE.xml        = arquivo
            self.ISUF.xml      = arquivo
            self.email.xml     = arquivo

    xml = property(get_xml, set_xml)




class Avulsa(nfe_200.Avulsa):
    def __init__(self):
        super(Avulsa, self).__init__()


class EnderEmit(nfe_200.EnderEmit):
    def __init__(self):
        super(EnderEmit, self).__init__()


class Emit(nfe_200.Emit):
    def __init__(self):
        super(Emit, self).__init__()


class RefECF(nfe_200.RefECF):
    def __init__(self):
        super(RefECF, self).__init__()


class RefNFP(nfe_200.RefNFP):
    def __init__(self):
        super(RefNFP, self).__init__()


class RefNF(nfe_200.RefNF):
    def __init__(self):
        super(RefNF, self).__init__()


class NFRef(nfe_200.NFRef):
    def __init__(self):
        super(NFRef, self).__init__()


class Ide(nfe_200.Ide):
    def __init__(self):
        super(Ide, self).__init__()
        self.mod     = TagInteiro(nome=u'mod'     , codigo=u'B06', tamanho=[ 2,  2, 2], raiz=u'//NFe/infNFe/ide')
        # A tag dEmi nao sera mais utilizada agora sera a dhEmi
        self.dEmi    = TagData(nome=u'dEmi'       , codigo=u'B09',                      raiz=u'//NFe/infNFe/ide',obrigatorio=False)

        self.dhEmi    = TagDataHoraUTC(nome=u'dhEmi'       , codigo=u'B09',                      raiz=u'//NFe/infNFe/ide')
        self.dhSaiEnt  = TagDataHoraUTC(nome=u'dhSaiEnt'       , codigo=u'B10',                      raiz=u'//NFe/infNFe/ide')
        self.hSaiEnt = TagDataHoraUTC(nome=u'hSaiEnt'    , codigo=u'B10a',                     raiz=u'//NFe/infNFe/ide', obrigatorio=False)
        self.idDest   = TagInteiro(nome=u'idDest'      , codigo=u'B11a', tamanho=[ 1,  1, 1], raiz=u'//NFe/infNFe/ide', valor=1)
        self.indFinal = TagCaracter(nome=u'indFinal'   , codigo=u'B25a',                      raiz=u'//NFe/infNFe/ide', valor=u'0')
        self.indPres  = TagCaracter(nome=u'indPres'    , codigo=u'B25b',                      raiz=u'//NFe/infNFe/ide', valor=u'9')
        self.dhCont   = TagDataHoraUTC(nome=u'dhCont', codigo=u'B28',                      raiz=u'//NFe/infNFe/ide', obrigatorio=False)



    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += '<ide>'
        xml += self.cUF.xml
        xml += self.cNF.xml
        xml += self.natOp.xml
        xml += self.indPag.xml
        xml += self.mod.xml
        xml += self.serie.xml
        xml += self.nNF.xml
        xml += self.dhEmi.xml
        xml += self.dhSaiEnt.xml
        xml += self.tpNF.xml
        xml += self.idDest.xml

        xml += self.cMunFG.xml

        for nr in self.NFref:
            xml += nr.xml


        xml += self.tpImp.xml
        xml += self.tpEmis.xml
        xml += self.cDV.xml
        xml += self.tpAmb.xml
        xml += self.finNFe.xml

        xml += self.indFinal.xml
        xml += self.indPres.xml

        xml += self.procEmi.xml
        xml += self.verProc.xml
        xml += self.dhCont.xml
        xml += self.xJust.xml
        xml += '</ide>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.cUF.xml     = arquivo
            self.cNF.xml     = arquivo
            self.natOp.xml   = arquivo
            self.indPag.xml  = arquivo
            self.mod.xml     = arquivo
            self.serie.xml   = arquivo
            self.nNF.xml     = arquivo
            self.dhEmi.xml   = arquivo
            self.dhSaiEnt.xml = arquivo
            self.hSaiEnt.xml = arquivo
            self.tpNF.xml    = arquivo
            self.idDest.xml  = arquivo
            self.cMunFG.xml  = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.NFRef = self.le_grupo('//NFe/infNFe/ide/NFref', NFRef)

            self.tpImp.xml   = arquivo
            self.tpEmis.xml  = arquivo
            self.cDV.xml     = arquivo
            self.tpAmb.xml   = arquivo
            self.finNFe.xml  = arquivo
            self.indFinal.xml = arquivo
            self.indPres.xml = arquivo
            self.procEmi.xml = arquivo
            self.verProc.xml = arquivo
            self.dhCont.xml  = arquivo
            self.xJust.xml   = arquivo

    xml = property(get_xml, set_xml)

class InfNFe(nfe_200.InfNFe):
    def __init__(self):
        super(InfNFe, self).__init__()
        self.versao   = TagDecimal(nome=u'infNFe' , codigo=u'A01', propriedade=u'versao', raiz=u'//NFe', namespace=NAMESPACE_NFE, valor=u'3.10')
        self.ide      = Ide()
        self.emit     = Emit()
        self.avulsa   = Avulsa()
        self.dest     = Dest()
        self.retirada = Retirada()
        self.entrega  = Entrega()
        self.autXML = []
        self.det      = []
        self.total    = Total()
        self.transp   = Transp()
        self.cobr     = Cobr()
        self.infAdic  = InfAdic()
        self.exporta  = Exporta()
        self.compra   = Compra()
        self.cana     = Cana()

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<infNFe versao="' + unicode(self.versao.valor) + u'" Id="' + self.Id.valor + u'">'
        xml += self.ide.xml
        xml += self.emit.xml
        xml += self.avulsa.xml
        xml += self.dest.xml
        xml += self.retirada.xml
        xml += self.entrega.xml

        for aut in self.autXML:
            xml += aut.xml

        for d in self.det:
            xml += d.xml



        xml += self.total.xml
        xml += self.transp.xml
        xml += self.cobr.xml
        xml += self.infAdic.xml
        xml += self.exporta.xml
        xml += self.compra.xml
        xml += self.cana.xml
        xml += u'</infNFe>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.versao.xml   = arquivo
            self.Id.xml       = arquivo
            self.ide.xml      = arquivo
            self.emit.xml     = arquivo
            self.avulsa.xml   = arquivo
            self.dest.xml     = arquivo
            self.retirada.xml = arquivo
            self.entrega.xml  = arquivo

            #
            # Técnica para leitura de tags múltiplas
            # As classes dessas tags, e suas filhas, devem ser
            # "reenraizadas" (propriedade raiz) para poderem ser
            # lidas corretamente
            #
            self.autXML = self.le_grupo('//NFe/infNFe/autXML',autXML)

            self.det = self.le_grupo('//NFe/infNFe/det', Det)

            self.total.xml    = arquivo
            self.transp.xml   = arquivo
            self.cobr.xml     = arquivo
            self.infAdic.xml  = arquivo
            self.exporta.xml  = arquivo
            self.compra.xml   = arquivo
            self.cana.xml     = arquivo

    xml = property(get_xml, set_xml)

class NFe(nfe_200.NFe):
    def __init__(self):
        super(NFe, self).__init__()
        self.infNFe = InfNFe()
        self.Signature = Signature()
        self.caminho_esquema = os.path.join(DIRNAME, u'schema/', ESQUEMA_ATUAL + u'/')
        self.arquivo_esquema = u'nfe_v3.10.xsd'

    # def gera_nova_chave(self):
    #
    #     super(NFe, self).gera_nova_chave()
    #
    #     #
    #     # Ajustar o campo cNF para remover o 1º dígito, que é
    #     # o tipo da emissão
    #     #
    #     self.infNFe.ide.cNF.valor = self.chave[35:43]
    def gera_nova_chave(self):
        chave = unicode(self.infNFe.ide.cUF.valor).zfill(2)
        chave += unicode(self.infNFe.ide.dhEmi.valor.strftime(u'%y%m')).zfill(4)
        chave += unicode(self.infNFe.emit.CNPJ.valor).zfill(14)
        chave += unicode(self.infNFe.ide.mod.valor).zfill(2)
        chave += unicode(self.infNFe.ide.serie.valor).zfill(3)
        chave += unicode(self.infNFe.ide.nNF.valor).zfill(9)

        #
        # A inclusão do tipo de emissão na chave já torna a chave válida também
        # para a versão 2.00 da NF-e
        #
        chave += unicode(self.infNFe.ide.tpEmis.valor).zfill(1)

        #
        # O código numério é um número aleatório
        #
        #chave += unicode(random.randint(0, 99999999)).strip().rjust(8, u'0')

        #
        # Mas, por segurança, é preferível que esse número não seja aleatório de todo
        #
        if not self.infNFe.ide.cNF.valor:
            soma = 0
            for c in chave:
                soma += int(c) ** 3 ** 2

            codigo = unicode(soma)
            if len(codigo) > 8:
                codigo = codigo[-8:]
            else:
                codigo = codigo.rjust(8, u'0')

            chave += codigo
            #
            # Define na estrutura do XML o campo cNF
            #
            self.infNFe.ide.cNF.valor = (unicode(self.infNFe.ide.tpEmis.valor).zfill(1) + codigo)
        else:
            chave += self.infNFe.ide.cNF.valor

        # self.infNFe.ide.cNF.valor = self.chave[35:43]
        #
        # Gera o dígito verificador
        #
        digito = self._calcula_dv(chave)

        #
        # Define na estrutura do XML o campo cDV
        #
        self.infNFe.ide.cDV.valor = digito

        chave += unicode(digito)
        self.chave = chave

        #
        # Define o Id
        #
        self.infNFe.Id.valor = u'NFe' + chave
        self.infNFe.ide.cNF.valor = self.chave[35:43]


    def monta_chave(self):
        self.gera_nova_chave()
        chave = unicode(self.infNFe.ide.cUF.valor).strip().rjust(2, u'0')
        chave += unicode(self.infNFe.ide.dhEmi.valor.strftime(u'%y%m')).strip().rjust(4, u'0')
        chave += unicode(self.infNFe.emit.CNPJ.valor).strip().rjust(14, u'0')
        chave += u'55'
        chave += unicode(self.infNFe.ide.serie.valor).strip().rjust(3, u'0')
        chave += unicode(self.infNFe.ide.nNF.valor).strip().rjust(9, u'0')

        #
        # Inclui agora o tipo da emissão
        #
        chave += unicode(self.infNFe.ide.tpEmis.valor).strip().rjust(1, u'0')

        chave += unicode(self.infNFe.ide.cNF.valor).strip().rjust(8, u'0')
        chave += unicode(self.infNFe.ide.cDV.valor).strip().rjust(1, u'0')

        self.chave = chave

    def monta_dados_contingencia_fsda(self):
        dados = unicode(self.infNFe.ide.cUF.valor).zfill(2)
        dados += unicode(self.infNFe.ide.tpEmis.valor).zfill(1)
        dados += unicode(self.infNFe.emit.CNPJ.valor).zfill(14)
        dados += unicode(int(self.infNFe.total.ICMSTot.vNF.valor * 100)).zfill(14)

        #
        # Há ICMS próprio?
        #
        if self.infNFe.total.ICMSTot.vICMS.valor:
            dados += u'1'
        else:
            dados += u'2'

        #
        # Há ICMS ST?
        #
        if self.infNFe.total.ICMSTot.vST.valor:
            dados += u'1'
        else:
            dados += u'2'

        dados += self.infNFe.ide.dhEmi.valor.strftime(u'%d').zfill(2)

        digito = self._calcula_dv(dados)
        dados += unicode(digito)
        self.dados_contingencia_fsda = dados
