# -*- coding: utf-8 -*-

from nfe.pysped.nfe import ProcessadorNFe
from nfe.pysped.nfe.webservices_flags import *
from nfe.pysped.nfe.manual_401 import *
from os.path import abspath, dirname
from OpenSSL import crypto
from StringIO import StringIO


FILE_DIR = abspath(dirname(__file__))



class nf_e(object):

    """
    Especialização da biblioteca pysped.
    @author: Marcilene Ribeiro
    """

    def extrair_certificado_a1(self,arquivo,senha):
        '''
        Extrai o conteúdo do certificado A1
        @param arquivo:caminho para o arquivo .pfx
        @param senha: senha do certificado.
        @return: dicionário com a string do certificado e da chave privada. 
        '''
        
        conteudo_pkcs12 = crypto.load_pkcs12(file(arquivo, 'rb').read(), senha)
      
        key = crypto.dump_privatekey(crypto.FILETYPE_PEM, conteudo_pkcs12.get_privatekey())

        cert = crypto.dump_certificate(crypto.FILETYPE_PEM, conteudo_pkcs12.get_certificate())

        return{'cert':cert,'key':key}

    def consultar_servidor(self,cert,key,versao=u'2.00',ambiente=2,estado=u'MG',scan=False):
        """
        Este método verifica se o servidor está em operação
        @param cert: string do certificado digital A1,
        @param key: chave privada do certificado digital,
        @param versao: versão da nfe,
        @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
        @param estado: estado em que realizará a consulta do servidor,
        @param scan: habilita a contigência SCAN. 
        @return: Dicionário com o status,envio,resposta e reason.
        """

        p = ProcessadorNFe()
        p.ambiente=ambiente
        p.estado=estado
        p.versao=versao
        p.certificado.cert_str=cert
        p.certificado.key_str=key
        p.salvar_arquivos=False
        p.contingencia_SCAN=scan
        p.caminho = u''
        processo = p.consultar_servico()
        status=processo.resposta.cStat.valor
        processo.envio.xml
        processo.resposta.xml
        processo.resposta.reason
        
        return{'status':status,'envio':processo.envio.xml,'resposta':processo.resposta.xml,'reason':processo.resposta.reason}


    def processar_nfe(self,xml_nfe,cert,key,versao=u'2.00',ambiente=2,estado=u'MG',scan=False):
       
        """
        Este método realiza o processamento de validação, assinatura e transmissão da nfe.
        @param xml_nfe:xml da nfe (string)
        @param cert: string do certificado digital A1,
        @param key: chave privada do certificado digital,
        @param versao: versão da nfe,
        @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
        @param estado: estado em que realizará o processamento,
        @param scan: habilita a contigência SCAN. 
        @return: Dicionário com a chave_nfe, protocolo, envio,resposta e reason.
        """
        
        p = ProcessadorNFe()
        p.ambiente=ambiente
        p.estado=estado
        p.certificado.cert_str=cert
        p.certificado.key_str=key
        p.salvar_arquivos=False
        p.contingencia_SCAN=scan
        p.caminho = u''
        n = NFe_200()
        n.infNFe.xml=xml_nfe 
        for processo in p.processar_notas([n]): 
            processo.envio.xml
            processo.resposta.xml
            processo.resposta.reason
            
        print dir(processo)
        print dir(processo.envio)
        print dir(processo.envio.validar)
        print processo.envio.xml
        print processo.resposta.xml
#        print processo.resposta.chNFe.valor
#        print processo.resposta.protNFe
#        print dir(processo.resposta.protNFe)
        print
        print 'nfe',n.xml
        print n.infNFe.ide.tpAmb.valor
        print dir(n)
        print n.chave
        print dir(processo.resposta)
#        print processo.resposta.protNFe
        print '***', dir(n.infNFe)
        print '***2', dir(n.infNFe.ide)
#        processo.resposta.protNFe.infProt.nProt.valor #quando a nota tiver sido processada, desta forma se consegue acessar o protocolo,
        print '++++++++',dir(processo.resposta.infProt.nProt)
        print 'prot',processo.resposta.infProt.nProt.valor
        
        print 'prot2',processo.resposta.protNFe.infProt.nProt.valor
#        print '-------',n.nfeProc.prot
#        print n.nfeProc.protNFe.infProt.nProt.valor
        print 
        return {'envio':processo.envio.xml,
                'resposta':processo.resposta.xml,
                'chave_nfe':n.chave,
                'protocolo':processo.resposta.protNFe.infProt.nProt.valor,
#                'protocolo':'12345678910',
                'reason':processo.resposta.reason
                }
    
    
    def processar_lote(self,lista_xml_nfe,cert,key,versao=u'2.00',ambiente=2,estado=u'MG',scan=False):
        
        """
        Este método realiza o processamento de validação, assinatura e transmissão da nfe.
        @param lista_xml_nfe:lista nfe
        @param cert: string do certificado digital A1,
        @param key: chave privada do certificado digital,
        @param versao: versão da nfe,
        @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
        @param estado: estado em que realizará o processamento,
        @param scan: habilita a contigência SCAN. 
        @return: Dicionário com o envio,resposta e reason.
        """

        p = ProcessadorNFe()
        p.ambiente=ambiente
        p.estado=estado

        p.certificado.cert_str=cert
        p.certificado.key_str=key
        p.salvar_arquivos=False
        p.contingencia_SCAN=scan
        p.caminho = u''
        n = NFe_200()
        lista=[]
        if lista_xml_nfe:
            for x in lista_xml_nfe:
                n.infNFe.xml=x
                lista.append(n)
        for processo in p.processar_notas(lista):        
            processo.envio.xml
            processo.resposta.xml
            processo.resposta.reason
            
        return {'envio':processo.envio.xml,'resposta':processo.resposta.xml,'reason':processo.resposta.reason}


    def cancelar_nota(self,chave,protocolo,justificativa,cert,key,versao=u'2.00',ambiente=2,estado=u'MG',scan=False):
        
        """
        Realiza o cancelamento da nfe.
        @param chave:chave da nfe
        @param protocolo: protocolo do processamento da nfe
        @param justificativa: justificativa do cancelamento 
        @param cert: string do certificado digital A1,
        @param key: chave privada do certificado digital,
        @param versao: versão da nfe,
        @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
        @param estado: estado em que realizará o processamento,
        @param scan: habilita a contigência SCAN. 
        @return: Dicionário com o envio,resposta e reason.
        """
        p = ProcessadorNFe()
        p.versao=versao
        p.estado=estado 
        p.ambiente=ambiente
        p.certificado.cert_str=cert
        p.certificado.key_str=key
        processo = p.cancelar_nota(chave_nfe=chave,numero_protocolo=protocolo,justificativa=justificativa)
        p.salvar_arquivos=False
        p.contingencia_SCAN=scan
    
        processo.envio.xml
        processo.resposta.xml
        processo.resposta.reason
        
        return {'envio':processo.envio.xml,'resposta':processo.resposta.xml,'reason':processo.resposta.reason}
    
    
    def inutilizar_nota(self,cnpj,serie,numero,justificativa,cert,key,versao=u'2.00',ambiente=2,estado=u'MG',scan=False):
        
        """
        Realiza a inutilização do número de uma nota fiscal
        @param cnpj:cnpj do emitente
        @param serie: serie da nfe
        @param numero: número da nota que deseja inutilizar
        @param justificativa: justificativa da inutilização 
        @param cert: string do certificado digital A1,
        @param key: chave privada do certificado digital,
        @param versao: versão da nfe,
        @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
        @param estado: estado em que realizará o processamento,
        @param scan: habilita a contigência SCAN. 
        @return: Dicionário com o envio,resposta e reason.
        """
        p = ProcessadorNFe()
        p.versao= u'2.00'
        p.estado= u'MG'
        p.ambiente= 2
        p.certificado.cert_str=cert
        p.certificado.key_str=key
        p.salvar_arquivos=False
        p.contingencia_SCAN=scan
        p.caminho = u''
        processo = p.inutilizar_nota(cnpj=cnpj,serie=serie,numero_inicial=numero,justificativa=justificativa)
        processo.envio.xml
        processo.resposta.xml
        processo.resposta.reason
        
        return {'envio':processo.envio.xml,'resposta':processo.resposta.xml,'reason':processo.resposta.reason}
    
    def inutilizar_faixa_numeracao(self,cnpj,serie,numero_inicial,numero_final,justificativa,cert,key,versao=u'2.00',ambiente=2,estado=u'MG',scan=False):
        
        """
        Realiza a inutilização de faixa de numeração de nota fiscal
        @param cnpj:cnpj do emitente
        @param serie: série da nfe
        @param numero_inicial: faixa inicial da nota que deseja inutilizar
        @param numero_final: faixa final da nota que deseja inutilizar
        @param justificativa: justificativa da inutilização 
        @param cert: string do certificado digital A1,
        @param key: chave privada do certificado digital,
        @param versao: versão da nfe,
        @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
        @param estado: estado em que realizará o processamento,
        @param scan: habilita a contigência SCAN. 
        @return: Dicionário com o envio,resposta e reason.
        """
        
        p = ProcessadorNFe()
        p.versao= u'2.00'
        p.estado= u'MG'
        p.ambiente= 2
        p.certificado.cert_str=cert
        p.certificado.key_str=key
        p.salvar_arquivos=False
        p.contingencia_SCAN=scan
        p.caminho = u''
        processo = p.inutilizar_nota(cnpj=cnpj,serie=serie,numero_inicial=numero_inicial,numero_final=numero_final,justificativa=justificativa)
        processo.envio.xml
        processo.resposta.xml
        processo.resposta.reason
        
        return {'envio':processo.envio.xml,'resposta':processo.resposta.xml,'reason':processo.resposta.reason}
    
    


