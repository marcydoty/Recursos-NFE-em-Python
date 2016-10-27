# -*- coding: utf-8 -*-

import os, sys
from datetime import datetime
sys.path.insert(0, os.path.abspath(".."))

from nfe.nf_e import nf_e

from nfe.pysped.nfe.manual_500.nfe_310 import NFe as NFe_310
from nfe.pysped.nfe.manual_500.nfe_310 import Det as Det_310
from nfe.pysped.nfe.webservices_flags import UF_CODIGO

if __name__ == '__main__':
    nova_nfe = nf_e()
    #Associacao.pfx nao e valido, utilize um certificado valido
    caminho_certificado = "certificado/Associacao.pfx"
    with open(caminho_certificado, 'rb') as f:
        arquivo = f.read()
    
    info_certificado = nova_nfe.extrair_certificado_a1(arquivo, "associacao")
    
    ##Montar nota fiscal
    
    nfe = NFe_310()
    
    #Identificação da nota
    nfe.infNFe.ide.cUF.valor        = UF_CODIGO['MG']
    nfe.infNFe.ide.natOp.valor      = u'Venda de produto'
    nfe.infNFe.ide.tpAmb.valor      = 2
    nfe.infNFe.ide.indPag.valor     = 2  
    nfe.infNFe.ide.serie.valor      = 101    
    nfe.infNFe.ide.nNF.valor        = 27    
    nfe.infNFe.ide.dhEmi.valor       = datetime(2016, 10, 14)  
    nfe.infNFe.ide.dhSaiEnt.valor    = datetime(2016, 10, 14)
    nfe.infNFe.ide.tpImp.valor      = 1            
    nfe.infNFe.ide.tpEmis.valor     = 1            
    nfe.infNFe.ide.finNFe.valor     = 1            
    nfe.infNFe.ide.procEmi.valor    = 0            
    nfe.infNFe.ide.verProc.valor    = u'PySPED NF-e'
    nfe.infNFe.ide.mod.valor        = u'55'
    nfe.infNFe.ide.cMunFG.valor     = u'3106200'
    
    #Identificação do emitente
    nfe.infNFe.emit.CNPJ.valor              = u'11111111111111'
    nfe.infNFe.emit.xNome.valor             = u'RAZAO SOCIAL'        
    nfe.infNFe.emit.xFant.valor             = u'Nome Fantasia'       #nao obrigatorio
    nfe.infNFe.emit.CRT.valor               = u'1'                   #SIMPLES NACIONAL
    nfe.infNFe.emit.IE.valor                = u'ISENTO'
    #Endereco emitente
    nfe.infNFe.emit.enderEmit.xLgr.valor    = u'LOGRADOURO (RUA, PRACA, AVENIDA)'
    nfe.infNFe.emit.enderEmit.nro.valor     = u'140'
    nfe.infNFe.emit.enderEmit.xCpl.valor    = u''                        
    nfe.infNFe.emit.enderEmit.xBairro.valor = u'PILAR'
    nfe.infNFe.emit.enderEmit.cMun.valor    = u'3106200'
    nfe.infNFe.emit.enderEmit.xMun.valor    = u'BELO HORIONTE'
    nfe.infNFe.emit.enderEmit.UF.valor      = u'MG'
    nfe.infNFe.emit.enderEmit.CEP.valor     = u'30390350'
    nfe.infNFe.emit.enderEmit.fone.valor    = u'3133333333'
    nfe.infNFe.emit.enderEmit.cPais.valor     = 1058 
    nfe.infNFe.emit.enderEmit.xPais.valor     = u'BRASIL'
    
    
    #Identificação do destinatario
    nfe.infNFe.dest.CNPJ.valor  = u'99999999000191'                                                 #Para homologacao
    nfe.infNFe.dest.xNome.valor = u'NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL'     #Para homologacao
    #Endereco destinatario
    nfe.infNFe.dest.enderDest.xLgr.valor    = u'RUA DOIS'
    nfe.infNFe.dest.enderDest.nro.valor     = u'140'
    nfe.infNFe.dest.enderDest.xCpl.valor    = u''
    nfe.infNFe.dest.enderDest.xBairro.valor = u'BARRO PRETO'
    nfe.infNFe.dest.enderDest.cMun.valor    = u'3106200'
    nfe.infNFe.dest.enderDest.xMun.valor    = u'BELO HORIZONTE'
    nfe.infNFe.dest.enderDest.UF.valor      = u'MG'
    nfe.infNFe.dest.enderDest.CEP.valor     = u'30190110'
    nfe.infNFe.dest.enderDest.cPais.valor   = u'1058'
    nfe.infNFe.dest.enderDest.xPais.valor   = u'Brasil'
    
    nfe.infNFe.dest.enderDest.fone.valor    = u'3122222222'
    #nfe.infNFe.dest.IE.valor = u'111111111111'
    nfe.infNFe.dest.IE.valor = u''
    nfe.infNFe.dest.indIEDest.valor = u'2'
    
    #Detalhamento dos produtos e servicos
    det = Det_310()
    
    det.nItem.valor = 1
    det.prod.cProd.valor    = u'CODIGO DO PRODUTO'
    det.prod.cEAN.valor     = u''
    det.prod.xProd.valor    = u'DESCRIÇÃO DO PRODUTO USADO PARA EMISSÃO'
    det.prod.NCM.valor      = u'01012100'
    det.prod.EXTIPI.valor   = u''
    det.prod.genero.valor   = u''
    det.prod.CFOP.valor     = u'5101'
    det.prod.uCom.valor     = u'UN'
    det.prod.qCom.valor     = u'100.00'
    det.prod.vUnCom.valor   = u'10.0000'
    det.prod.vProd.valor    = u'1000.00'
    det.prod.cEANTrib.valor = u''
    det.prod.uTrib.valor    = det.prod.uCom.valor
    det.prod.qTrib.valor    = det.prod.qCom.valor
    det.prod.vUnTrib.valor  = det.prod.vUnCom.valor
    det.prod.vFrete.valor   = u'0.00'
    det.prod.vSeg.valor     = u'0.00'
    det.prod.vDesc.valor    = u'0.00'
    
    #Impostos
    det.imposto.ICMS.regime_tributario = 1      #REGIME TRIBUTARIO: SIMPLES NACIONAL
    det.imposto.ICMS.CSOSN.valor    = u'400'     #CODIGO DE REGIME APENAS PARA O SIMPLES NACIONAL
    det.imposto.IPI.CST.valor       = u'99'
    det.imposto.PIS.CST.valor       = u'99'
    det.imposto.COFINS.CST.valor    = u'99'
    
    # Os primeiros 188 caracteres desta string
    # são todos os caracteres válidos em tags da NF-e
    #Informacoes adicionais
    det.infAdProd.valor = u'!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ·¸¹º»¼½¾¿À'
    
    #Incluir detalhes na nfe
    nfe.infNFe.det.append(det)
    
    #Totais
    nfe.infNFe.total.ICMSTot.vBC.valor     = u'0.00'
    nfe.infNFe.total.ICMSTot.vICMS.valor   = u'0.00'
    nfe.infNFe.total.ICMSTot.vBCST.valor   = u'0.00'
    nfe.infNFe.total.ICMSTot.vST.valor     = u'0.00'
    nfe.infNFe.total.ICMSTot.vProd.valor   = u'1000.00'
    nfe.infNFe.total.ICMSTot.vFrete.valor  = u'0.00'
    nfe.infNFe.total.ICMSTot.vSeg.valor    = u'0.00'
    nfe.infNFe.total.ICMSTot.vDesc.valor   = u'0.00'
    nfe.infNFe.total.ICMSTot.vII.valor     = u'0.00'
    nfe.infNFe.total.ICMSTot.vIPI.valor    = u'0.00'
    nfe.infNFe.total.ICMSTot.vPIS.valor    = u'0.00'
    nfe.infNFe.total.ICMSTot.vCOFINS.valor = u'0.00'
    nfe.infNFe.total.ICMSTot.vOutro.valor  = u'0.00'
    nfe.infNFe.total.ICMSTot.vNF.valor     = u'1000.00'
    nfe.infNFe.total.ICMSTot.vICMSDeson.valor = u'0.00'
    
    nfe.gera_nova_chave()
    
    #Gera e emite nota fiscal
    resultados = nova_nfe.processar_nfe(xml_nfe=nfe.xml, cert=info_certificado['cert'], key=info_certificado['key'], versao=u'3.10', ambiente=2, estado=u'MG', tipo_contingencia=False)
    print("\nResultado:\n")
    '''Retorna um dicionario'''
    for key, value in resultados.items():
        print(str(key)+" : "+str(value))