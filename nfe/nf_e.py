# -*- coding: utf-8 -*-

from nfe.pysped.nfe import ProcessadorNFe, DANFE
from nfe.pysped.nfe.webservices_flags import *
from nfe.pysped.nfe.manual_401 import *
from os.path import abspath, dirname
from OpenSSL import crypto
from StringIO import StringIO
from xml.dom import minidom
from nfe.pysped.nfe.danfe.danferetrato import *
from nfe.pysped.xml_sped.certificado import Certificado

FILE_DIR = abspath(dirname(__file__))

class nf_e(object):

    """
    Especialização da biblioteca pysped.
    @author: Marcilene Ribeiro
    """

    def extrair_certificado_a1(self,arquivo,senha):
        '''
        Extrai o conteúdo do certificado A1
        @param arquivo:arquivo binário do certificado .pfx
        @param senha: senha do certificado.
        @return: dicionário com a string do certificado, chave privada, emissor, proprietario, data_inicio_validade e data_final_validade.
        '''

        conteudo_pkcs12 = crypto.load_pkcs12(arquivo, senha)
        key_str = crypto.dump_privatekey(crypto.FILETYPE_PEM, conteudo_pkcs12.get_privatekey())

        cert_str = crypto.dump_certificate(crypto.FILETYPE_PEM, conteudo_pkcs12.get_certificate())
        certificado= Certificado()
        certificado.prepara_certificado_txt(cert_str)

        vals = {'cert':cert_str,
                'key':key_str,
                'emissor':certificado.emissor.get('OU'),
                'proprietario':certificado.proprietario.get('CN'),
                'data_inicio_validade':certificado.data_inicio_validade,
                'data_final_validade':certificado.data_fim_validade,
                }
        return vals
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
        @return: Dicionário com a chave_nfe, protocolo, envio, numero_lote, resposta, status_resposta,status_motivo e reason.
        """
        
        p = ProcessadorNFe()
        p.ambiente=ambiente
        p.estado=estado
        p.certificado.cert_str=cert
        p.certificado.key_str=key
        p.salvar_arquivos=True
        p.contingencia_SCAN=scan
        p.caminho = u''
        n = NFe_200()
        n.infNFe.xml=xml_nfe
        for processo in p.processar_notas([n]): 
            processo.envio.xml
            processo.resposta.xml
            processo.resposta.reason
        vals={'envio':processo.envio.xml,
                'resposta':processo.resposta.xml,
                'chave_nfe':n.chave,
                'status_resposta':processo.resposta.cStat.valor,
                'status_motivo':processo.resposta.xMotivo.valor,
                'reason':processo.resposta.reason
            }
        try:
            if processo.resposta.infProt.nProt.valor=='':
                vals['protocolo']=processo.resposta.protNFe.infProt.nProt.valor
        except:
            pass

        for nome, proc in p.processos.iteritems():
            for arquivo in proc[1]:
                if arquivo[0]=='numero_lote':
                    vals['numero_lote']=arquivo[1]
                if arquivo[0]=='numero_protocolo':
                    vals['protocolo']=arquivo[1]
                    vals['resposta']=proc[1][1][1]
                if arquivo[0]=='status_resp':
                    vals['status_resposta']=arquivo[1][0]
                    vals['status_motivo']=arquivo[1][1]
        return vals
    
    
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
        p.contingencia_SCAN=scan
        p.salvar_arquivos=False
        processo = p.cancelar_nota(chave_nfe=chave,numero_protocolo=protocolo,justificativa=justificativa)
        processo.envio.xml
        processo.resposta.xml
        processo.resposta.reason
        
        vals={'envio':processo.envio.xml,
              'resposta':processo.resposta.xml,
              'status_resposta':processo.resposta.infCanc.cStat.valor,
              'status_motivo':processo.resposta.infCanc.xMotivo.valor,
              'reason':processo.resposta.reason}
        if processo.resposta.infCanc.cStat.valor =='101':
            vals['protocolo']=processo.resposta.infCanc.nProt.valor
            
        return vals
    
    
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
        vals={'envio':processo.envio.xml,
              'resposta':processo.resposta.xml,
              'status_resposta':processo.resposta.infInut.cStat.valor,
              'status_motivo':processo.resposta.infInut.xMotivo.valor,
              'reason':processo.resposta.reason}
        return vals
    
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
        vals={'envio':processo.envio.xml,
              'resposta':processo.resposta.xml,
              'status_resposta':processo.resposta.infInut.cStat.valor,
              'status_motivo':processo.resposta.infInut.xMotivo.valor,
              'reason':processo.resposta.reason}
        if processo.resposta.infInut.cStat.valor =='102':
            vals['protocolo'] = processo.resposta.infInut.nProt.valor
        
        return vals

    def gerar_danfe(self,nfe,retcan_nfe=None,site_emitente=u'',logo=u'',nome_sistema=u'SigERP - www.sigsolucoes.net.br',leiaute_logo_vertical=False):

            """
            Geração do DANFE
            @param nfe:string do xml da NF-e
            @param site_emitente: Endereço do site do emitente
            @param logo:O caminho para a imagem ou  Instância da imagem.
            @param leiaute_logo_vertical: possibilita que a logomarca tenha a orientação vertical
            @return: String
            """

            d = DANFE()
            nota = NFe_200()
            nota.xml = nfe
            protNFe = ProtNFe_200()
            resp = minidom.parseString(nfe.encode('utf-8'))
            resp = resp.getElementsByTagName("protNFe")[0]
            resposta = resp.toxml()
            protNFe.xml= resposta
            proc = ProcNFe_200()
            proc.protNFe = protNFe

            d.NFe = nota
            d.protNFe = protNFe
            d.salvar_arquivo = False
            d.obs_impressao    = u'DANFE gerado em %(now:%d/%m/%Y, %H:%M:%S)s'
            d.nome_sistema     = nome_sistema
            d.site             = site_emitente
            d.logo             = logo
            d.leiaute_logo_vertical = leiaute_logo_vertical
            d.gerar_danfe()
            danfe_pdf = StringIO()
            d.danfe.generate_by(PDFGenerator, filename=danfe_pdf)
            d.danfe = danfe_pdf.getvalue()
            danfe_pdf.close()

            return d.danfe


    


