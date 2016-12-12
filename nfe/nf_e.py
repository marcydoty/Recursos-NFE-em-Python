# -*- coding: utf-8 -*-

from nfe.pysped.nfe import ProcessadorNFe, DANFE
from nfe.pysped.nfe.manual_401 import *
from nfe.pysped.nfe.manual_500 import *
from os.path import abspath, dirname
from OpenSSL import crypto
from StringIO import StringIO
from xml.dom import minidom
from nfe.pysped.nfe.danfe.danferetrato import *
from nfe.pysped.xml_sped.certificado import Certificado
from nfe.pysped.nfe.webservices_2 import ESTADO_WS, SVAN, SVRS, UFRS, NFE_AMBIENTE_PRODUCAO
FILE_DIR = abspath(dirname(__file__))

class nf_e(object):
    """
    Especialização da biblioteca pysped.
    @author: Marcilene Ribeiro
    """

    def extrair_certificado_a1(self, arquivo, senha):
        '''
        Extrai o conteúdo do certificado A1
        @param arquivo:arquivo binário do certificado
        @param senha: senha do certificado.
        @return: dicionário com a string do certificado, chave privada, emissor, proprietario, data_inicio_validade e
        data_final_validade.
        '''

        conteudo_pkcs12 = crypto.load_pkcs12(arquivo, senha)
        key_str = crypto.dump_privatekey(crypto.FILETYPE_PEM, conteudo_pkcs12.get_privatekey())

        cert_str = crypto.dump_certificate(crypto.FILETYPE_PEM, conteudo_pkcs12.get_certificate())
        certificado = Certificado()
        certificado.prepara_certificado_txt(cert_str)

        vals = {'cert': cert_str,
                'key': key_str,
                'emissor': certificado.emissor.get('OU'),
                'proprietario': certificado.proprietario.get('CN'),
                'data_inicio_validade': certificado.data_inicio_validade,
                'data_final_validade': certificado.data_fim_validade,
        }
        return vals

    def consultar_servidor(self, cert, key, versao=u'2.00', ambiente=2, estado=u'MG',
                           tipo_contingencia=False):
        """
        Este método verifica se o servidor está em operação
        @param cert: string do certificado digital A1,
        @param key: chave privada do certificado digital,
        @param versao: versão da nfe,
        @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
        @param estado: estado em que realizará a consulta do servidor,
        @param tipo_contingencia : habilita a contigência.
        @return: Dicionário com o status,envio,resposta e reason.
        """

        p = ProcessadorNFe()
        p.ambiente = ambiente
        p.estado = estado
        p.versao = versao
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.salvar_arquivos = False
        p.tipo_contingencia = tipo_contingencia
        p.caminho = u''
        processo, novos_arquivos = p.consultar_servico()
        status = processo.resposta.cStat.valor
        processo.envio.xml
        processo.resposta.xml
        processo.resposta.reason

        return{'status': status, 'envio': processo.envio.xml, 'resposta': processo.resposta.xml,
               'reason': processo.resposta.reason}


    def processar_nfe(self, xml_nfe, cert, key, versao=u'2.00', ambiente=2, estado=u'MG',
                      tipo_contingencia=False):
        """
        Este método realiza o processamento de validação, assinatura e transmissão da nfe.
        @param xml_nfe:xml da nfe (string)
        @param cert: string do certificado digital A1,
        @param key: chave privada do certificado digital,
        @param versao: versão da nfe,
        @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
        @param estado: estado em que realizará o processamento,
        @param tipo_contingencia: habilita a contigência .
        @return: Dicionário com a chave_nfe, protocolo, envio, numero_lote, resposta, status_resposta,status_motivo e reason.
        """

        p = ProcessadorNFe()
        p.ambiente = ambiente
        p.estado = estado
        p.versao = versao
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.salvar_arquivos = True
        p.tipo_contingencia = tipo_contingencia
        p.caminho = u''
        if versao == '3.10':
            n = NFe_310()
        else:
            n = NFe_200()
        n.infNFe.xml = xml_nfe
        for processo in p.processar_notas([n]):
            processo.envio.xml
            processo.resposta.xml
            processo.resposta.reason
        vals = {'envio': processo.envio.xml,
                'resposta': processo.resposta.xml,
                'chave_nfe': n.chave,
                'xml_pre_validado': n.xml,
                'status_resposta': processo.resposta.cStat.valor,
                'status_motivo': processo.resposta.xMotivo.valor,
                'reason': processo.resposta.reason
        }
        try:
            if processo.resposta.infProt.nProt.valor == '':
                vals['protocolo'] = processo.resposta.protNFe.infProt.nProt.valor
        except:
            pass

        for nome, proc in p.processos.iteritems():
            for arquivo in proc[1]:
                if arquivo[0] == 'numero_lote':
                    vals['numero_lote'] = arquivo[1]
                if arquivo[0] == 'numero_protocolo':
                    vals['protocolo'] = arquivo[1]
                    vals['resposta'] = proc[1][1][1]
                if arquivo[0] == 'status_resp':
                    vals['status_resposta'] = arquivo[1][0]
                    vals['status_motivo'] = arquivo[1][1]
        return vals


    def processar_lote(self, lista_xml_nfe, cert, key, versao=u'2.00', ambiente=2, estado=u'MG',
                       tipo_contingencia=False):
        """
        Este método realiza o processamento de validação, assinatura e transmissão da nfe.
        @param lista_xml_nfe:lista nfe
        @param cert: string do certificado digital A1,
        @param key: chave privada do certificado digital,
        @param versao: versão da nfe,
        @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
        @param estado: estado em que realizará o processamento,
        @param tipo_contingencia: habilita a contigência .
        @return: Dicionário com o envio,resposta e reason.
        """

        p = ProcessadorNFe()
        p.ambiente = ambiente
        p.estado = estado
        p.versao=versao
        p.tipo_contingencia = tipo_contingencia
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.salvar_arquivos = False
        p.caminho = u''
        if versao == '3.10':
            n = NFe_310()
        else:
            n = NFe_200()
        lista = []
        if lista_xml_nfe:
            for x in lista_xml_nfe:
                n.infNFe.xml = x
                lista.append(n)
        for processo in p.processar_notas(lista):
            processo.envio.xml
            processo.resposta.xml
            processo.resposta.reason

        return {'envio': processo.envio.xml, 'resposta': processo.resposta.xml,
                'reason': processo.resposta.reason}


    def cancelar_nota(self, cnpj, chave, protocolo, justificativa, cert, key, versao=u'2.00',
                      ambiente=2, estado=u'MG', tipo_contingencia=False):
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
        @param tipo_contingencia: habilita a contigência .
        @return: Dicionário com o envio,resposta e reason.
        """
        p = ProcessadorNFe()
        p.versao = versao
        p.estado = estado
        p.ambiente = ambiente
        p.tipo_contingencia = tipo_contingencia
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.salvar_arquivos = False
        processo = p.cancelar_nota(cnpj, chave_nfe=chave, numero_protocolo=protocolo,
                                   justificativa=justificativa)
        processo.resposta.reason
        vals = {'envio': processo.envio.xml,
                'resposta': processo.processo_cancelamento_nfe.xml,
                'status_resposta': processo.resposta.infEvento.cStat.valor,
                'status_motivo': processo.resposta.infEvento.xMotivo.valor,
                'reason': processo.resposta.reason}
        if processo.resposta.infEvento.cStat.valor == '135':
            vals['protocolo'] = processo.resposta.infEvento.nProt.valor

        return vals


    def inutilizar_nota(self, cnpj, serie, numero, justificativa, cert, key, versao=u'2.00',
                        ambiente=2, estado=u'MG', tipo_contingencia=False):
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
        @param tipo_contingencia: habilita a contigência .
        @return: Dicionário com o envio,resposta e reason.
        """
        p = ProcessadorNFe()
        p.versao = versao
        p.estado = estado
        p.ambiente = ambiente
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.salvar_arquivos = False
        p.tipo_contingencia = tipo_contingencia
        p.caminho = u''
        processo = p.inutilizar_nota(cnpj=cnpj, serie=serie, numero_inicial=numero,
                                     justificativa=justificativa)
        processo.envio.xml
        processo.resposta.xml
        processo.resposta.reason
        vals = {'envio': processo.envio.xml,
                'resposta': processo.resposta.xml,
                'status_resposta': processo.resposta.infInut.cStat.valor,
                'status_motivo': processo.resposta.infInut.xMotivo.valor,
                'reason': processo.resposta.reason}
        return vals

    def inutilizar_faixa_numeracao(self, cnpj, serie, numero_inicial, numero_final, justificativa,
                                   cert, key, versao=u'2.00', ambiente=2, estado=u'MG',
                                   tipo_contingencia=False):
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
        @param tipo_contingencia: habilita a contigência .
        @return: Dicionário com o envio,resposta e reason.
        """

        p = ProcessadorNFe()
        p.versao = versao
        p.estado = estado
        p.ambiente = ambiente
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.salvar_arquivos = False
        p.tipo_contingencia = tipo_contingencia
        p.caminho = u''
        processo = p.inutilizar_nota(cnpj=cnpj, serie=serie, numero_inicial=numero_inicial,
                                     numero_final=numero_final, justificativa=justificativa)
        processo.envio.xml
        processo.resposta.xml
        processo.resposta.reason
        vals = {'envio': processo.envio.xml,
                'resposta': processo.resposta.xml,
                'status_resposta': processo.resposta.infInut.cStat.valor,
                'status_motivo': processo.resposta.infInut.xMotivo.valor,
                'reason': processo.resposta.reason}
        if processo.resposta.infInut.cStat.valor == '102':
            vals['protocolo'] = processo.resposta.infInut.nProt.valor

        return vals

    def gerar_danfe(self, nfe, retcan_nfe=None, site_emitente=u'', logo=u'',
                    nome_sistema=u'SigERP - www.sigsolucoes.net.br', leiaute_logo_vertical=False,
                    versao='2.00'):
        """
        Geração do DANFE
        @param nfe:string do xml da NF-e
        @param site_emitente: Endereço do site do emitente
        @param logo:O caminho para a imagem ou  Instância da imagem.
        @param leiaute_logo_vertical: possibilita que a logomarca tenha a orientação vertical
        @return: String
        """

        d = DANFE()
        if versao == '3.10':
            nota = NFe_310()
            protNFe = ProtNFe_310()
            proc = ProcNFe_310()
        else:
            nota = NFe_200()
            protNFe = ProtNFe_200()
            proc = ProcNFe_200()
        nota.xml = nfe
        resp = minidom.parseString(nfe.encode('utf-8'))
        resp = resp.getElementsByTagName("protNFe")[0]
        resposta = resp.toxml()
        protNFe.xml = resposta
        proc.protNFe = protNFe

        d.NFe = nota
        d.protNFe = protNFe
        d.versao = versao
        d.salvar_arquivo = False
        d.obs_impressao = u'DANFE gerado em %(now:%d/%m/%Y, %H:%M:%S)s'
        d.nome_sistema = nome_sistema
        d.site = site_emitente
        d.logo = logo
        d.leiaute_logo_vertical = leiaute_logo_vertical
        d.gerar_danfe()
        danfe_pdf = StringIO()
        d.danfe.generate_by(PDFGenerator, filename=danfe_pdf)
        d.danfe = danfe_pdf.getvalue()
        danfe_pdf.close()

        return d.danfe

    def validar_chave_nfe(self, chave, uf, data_emissao, cnpj, modelo, serie, numero_nf):
        """
        Verifica consistência da chave de NF-e informada
        @param chave:Chave da NF-e
        @param uf:
        @param data_emissao:
        @param cnpj
        @param modelo
        @param serie
        @param numero_nf
        @return: Dicionário
        """
        msg = ''
        res = {'valida': True, msg: ''}
        if len(chave) == 44:
            if chave[:2] != uf:
                msg += '* Estado informado inválido.\n'
            data_emissao = data_emissao[2:4] + data_emissao[5:7]
            if chave[2:6] != data_emissao:
                msg += '* Data de emissão inválida. \n'
            cnpj = cnpj.replace('.', '').replace('-', '').replace('/', '')
            if chave[6:20] != cnpj:
                msg += '* CNPJ do emitente inválido. \n'
            if chave[20:22] != modelo:
                msg += '* Modelo da Nota Fiscal inválido.\n'
            if chave[22:25] != ('%003d' % int(serie)):
                msg += '* Série da Nota Fiscal inválida.\n'
            if chave[25:34] != '%009d' % int(numero_nf):
                msg += '* Número da Nota Fiscal inválido. \n'
            nf = NFe_200()
            digito_verificador = nf._calcula_dv(chave[:43])
            if digito_verificador != int(chave[43:]):
                msg += '* Dígito verificador inválido. \n'
            if msg:
                res['msg'] = 'Chave de acesso inválida: \n' + msg
                res['valida'] = False
        else:
            res['msg'] = 'Chave inválida.'
            res['valida'] = False
        return res

    def consultar_nfe(self,chave, cert, key, versao=u'2.00', ambiente=2, estado=u'MG',
                      tipo_contingencia=False):
        """
            @param chave:chave da nfe
            @param cert: string do certificado digital A1,
            @param key: chave privada do certificado digital,
            @param versao: versão da nfe,
            @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
            @param estado: estado em que realizará o processamento,
            @param tipo_contingencia: habilita a contigência .
            @return: Dicionário com o envio,resposta e reason.
        """
        p = ProcessadorNFe()
        p.versao = versao
        p.estado = estado
        p.ambiente = ambiente
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.tipo_contingencia=tipo_contingencia
        p.salvar_arquivos = False
        processo, arquivos = p.consultar_nota(chave_nfe=chave)
        vals = {'envio': processo.envio.xml,
                'resposta': processo.resposta.xml,
                'status_resposta': processo.resposta.cStat.valor,
                'status_motivo': processo.resposta.xMotivo.valor,
                'reason': processo.resposta.reason,
                'arquivos':arquivos}
        return vals


    def consultar_cadastro(self, cpf_cnpj, inscricao_estadual, uf, cert, key, versao=u'2.00',
                           ambiente=2, estado=u'MG', tipo_contingencia=False):
        """
            @param chave:chave da nfe
            @param cert: string do certificado digital A1,
            @param key: chave privada do certificado digital,
            @param versao: versão da nfe,
            @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
            @param estado: estado em que realizará o processamento,
            @param tipo_contingencia: habilita a contigência .
            @return: Dicionário com o envio,resposta e reason.
             """
        p = ProcessadorNFe()
        p.versao = versao
        p.estado = estado
        if uf in ('AC', 'AL', 'AP', 'DF', 'ES', 'PB', 'RJ', 'RN', 'RO', 'RR', 'SC',
                  'SE', 'TO'):
            #SVRS[NFE_AMBIENTE_PRODUCAO][u'servidor'] = u'svp-ws.sefazvirtual.rs.gov.br'
            SVRS[NFE_AMBIENTE_PRODUCAO][u'servidor'] = u'cad.svrs.rs.gov.br'
        if uf == 'RS':
            #UFRS[NFE_AMBIENTE_PRODUCAO][u'servidor'] = u'sef.sefaz.rs.gov.br'
            UFRS[NFE_AMBIENTE_PRODUCAO][u'servidor'] = u'cad.sefazrs.rs.gov.br'
        p.ambiente = ambiente
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.tipo_contingencia = tipo_contingencia
        p.salvar_arquivos = False
        processo = p.consultar_cadastro_contribuinte(cpf_cnpj=cpf_cnpj,
                                                     inscricao_estadual=inscricao_estadual, uf=uf,
                                                     ambiente=ambiente)
        vals = {'envio': processo.envio.xml,
                'resposta': processo.resposta.xml,
                'status_resposta': processo.resposta.infCons.cStat.valor,
                'status_motivo': processo.resposta.infCons.xMotivo.valor,
                'reason': processo.resposta.reason}
        return vals

    #MANIFESTAÇÃO DO DESTINATÁRIO

    def efetuar_manifesto(self, cnpj, tipo_evento, chave,  cert, key, versao=u'2.00', ambiente=2,
                          estado=u'MG', tipo_contingencia=False):
        """
            Realiza o manifesto do destinatário
            @param chave:chave da nfe
            @param cert: string do certificado digital A1,
            @param key: chave privada do certificado digital,
            @param versao: versão da nfe,
            @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
            @param estado: estado em que realizará o processamento,
            @param tipo_contingencia: habilita a contigência .
            @return: Dicionário com o envio,resposta e reason.
            """
        p = ProcessadorNFe()
        p.versao = versao
        p.estado = estado
        #Provisoriamente apontado para um estado que usa o webservice de ambiente nacional,
        # pois em MG ainda não existe suporte ao Manifesto do Destinatário
        ESTADO_WS[estado] = SVAN
        p.ambiente = ambiente
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.tipo_contingencia = tipo_contingencia
        p.salvar_arquivos = False
        processo = p.consultar_manifesto_destinatario(cnpj, tipo_evento=tipo_evento, chave_nfe=chave)

        vals = {'envio': processo.envio.xml,
                'resposta': processo.processo_evento_nfe.xml,
                'status_resposta': processo.resposta.infEvento.cStat.valor,
                'status_motivo': processo.resposta.infEvento.xMotivo.valor,
                'reason': processo.resposta.reason}
        if processo.resposta.infEvento.cStat.valor == '135':
            vals['protocolo'] = processo.resposta.infEvento.nProt.valor

        return vals


    def consultar_nfe_destinatario(self, cnpj, indnfe, indemi, cert, key, nsu='0', versao=u'2.00',
                                   ambiente=2, estado=u'MG', tipo_contingencia=False):
        """
            Realiza  a consulta do manifesto do destinatário
            @param cert: string do certificado digital A1,
            @param key: chave privada do certificado digital,
            @param versao: versão da nfe,
            @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
            @param estado: estado em que realizará o processamento,
            @param tipo_contingencia: habilita a contigência .
            @return: Dicionário com o envio,resposta e reason.
            """
        p = ProcessadorNFe()
        p.versao = versao
        p.estado = estado
        #Provisoriamente apontado para um estado que usa o webservice de ambiente nacional, pois em MG ainda
        # não existe suporte ao Manifesto do Destinatário
        ESTADO_WS[estado] = SVAN
        p.ambiente = ambiente
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.tipo_contingencia = tipo_contingencia
        p.salvar_arquivos = False
        processo = p.consultar_notas_destinatario(cnpj=cnpj, indnfe=indnfe, indemi=indemi, nsu=nsu)
        resp = processo.resposta
        lista_notas = []
        if resp.cStat.valor == '138':#Documento localizado para o destinatário
            for resp in resp.ret:
                if resp.resNFe.xml:
                    dict_resnfe = {
                        'NSU': resp.resNFe.NSU.valor,
                        'chNFe': resp.resNFe.chNFe.valor,
                        'CNPJ': resp.resNFe.CNPJ.valor,
                        'CPF': resp.resNFe.CPF.valor,
                        'xNome': resp.resNFe.xNome.valor,
                        'IE': resp.resNFe.IE.valor,
                        'dEmi': resp.resNFe.dEmi.valor,
                        'tpNF': resp.resNFe.tpNF.valor,
                        'vNF': resp.resNFe.vNF.valor,
                        'digVal': resp.resNFe.digVal.valor,
                        'dhRecbto': resp.resNFe.dhRecbto.valor,
                        'cSitNFe': resp.resNFe.cSitNFe.valor,
                        'cSitConf': resp.resNFe.cSitConf.valor
                    }
                    lista_notas.append({'resNFe': dict_resnfe})
                if resp.resCanc.xml:
                    dict_rescanc = {
                        'NSU': resp.resCanc.NSU.valor,
                        'chNFe': resp.resCanc.chNFe.valor,
                        'CNPJ': resp.resCanc.CNPJ.valor,
                        'CPF': resp.resCanc.CPF.valor,
                        'xNome': resp.resCanc.xNome.valor,
                        'IE': resp.resCanc.IE.valor,
                        'dEmi': resp.resCanc.dEmi.valor,
                        'tpNF': resp.resCanc.tpNF.valor,
                        'vNF': resp.resCanc.vNF.valor,
                        'digVal': resp.resCanc.digVal.valor,
                        'dhRecbto': resp.resCanc.dhRecbto.valor,
                        'cSitNFe': resp.resCanc.cSitNFe.valor,
                        'cSitConf': resp.resCanc.cSitConf.valor
                    }
                    lista_notas.append({'resCanc': dict_rescanc})
                if resp.resCCe.xml:
                    dict_rescce = {
                        'NSU': resp.resCCe.NSU.valor,
                        'chNFe': resp.resCCe.chNFe.valor,
                        'dhEvento': resp.resCCe.dhEvento.valor,
                        'tpEvento': resp.resCCe.tpEvento.valor,
                        'nSeqEvento': resp.resCCe.nSeqEvento.valor,
                        'descEvento': resp.resCCe.descEvento.valor,
                        'xCorrecao': resp.resCCe.xCorrecao.valor,
                        'tpNF': resp.resCCe.tpNF.valor,
                        'dhRecbto': resp.resCCe.dhRecbto.valor
                    }
                    lista_notas.append({'resCCe': dict_rescce})


        vals = {'envio':processo.envio.xml,
                'resposta': processo.resposta.xml,
                'status_resposta': processo.resposta.cStat.valor,
                'status_motivo': processo.resposta.xMotivo.valor,
                'lista_notas': lista_notas,
                'reason': processo.resposta.reason}

        return vals

    def download_xml(self, cnpj, lista_chaves,  cert, key, ambiente_nacional=True, versao=u'2.00', ambiente=2, estado=u'MG',
                     tipo_contingencia=False):
        """
            Realiza  a consulta do manifesto do destinatário
            @param lista_chaves: lista de até 10 chaves
            @param cert: string do certificado digital A1,
            @param key: chave privada do certificado digital,
            @param versao: versão da nfe,
            @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
            @param estado: estado em que realizará o processamento,
            @param tipo_contingencia: habilita a contigência .
            @return: Dicionário com o envio,resposta e reason.
            """
        if len(lista_chaves)>10:
            raise ValueError(u'Maximo de 10 Chaves de Acesso por lote.')
            
        p = ProcessadorNFe()
        p.versao = versao
        p.estado = estado
        if ambiente_nacional:
            ESTADO_WS[estado] = SVAN
        p.ambiente = ambiente
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.tipo_contingencia = tipo_contingencia
        p.salvar_arquivos = False
        processo = p.download_nfe_xml(cnpj, ambiente, lista_chaves=lista_chaves)

        vals = {'envio': processo.envio.xml,
                'resposta': processo.resposta.xml,
                'proc_xml':processo.resposta.original,
                #'status_resposta': processo.resposta.retNFe.cStat.valor,
                #'status_motivo': processo.resposta.retNFe.xMotivo.valor,
                'reason': processo.resposta.reason}
        for i,ret in enumerate(processo.resposta.retNFe):
            vals['status_resp_nota_' + str(i)] = ret.cStat.valor
            vals['status_motivo_nota_' + str(i)] = ret.xMotivo.valor

        return vals

    #CARTA DE CORRECAO

    def emitir_carta_correcao(self, chave, cnpj, texto_correcao, cert, key, sequencia=None,
                              versao=u'2.00', ambiente=2, estado=u'MG',
                              tipo_contingencia=False):
        """
            @param chave:chave da nfe
            @param cert: string do certificado digital A1,
            @param key: chave privada do certificado digital,
            @param versao: versão da nfe,
            @param ambiente: ambiente da consulta, pode ser 1 para o ambiente de produção e 2 para homologação,
            @param estado: estado em que realizará o processamento,
            @param tipo_contingencia: habilita a contigência .
            @return: Dicionário com o envio,resposta e reason.
            """
        p = ProcessadorNFe()
        p.versao = versao
        p.estado = estado
        p.ambiente = ambiente
        p.certificado.cert_str = cert
        p.certificado.key_str = key
        p.salvar_arquivos = False
        p.tipo_contingencia = tipo_contingencia
        processo = p.corrigir_nota(chave_nfe=chave, cnpj=cnpj, texto_correcao=texto_correcao,
                                   ambiente=ambiente,sequencia=sequencia)
        processo.resposta.reason
        vals = {'envio': processo.envio.xml,
                'resposta': processo.processo_correcao_nfe.xml,
                'status_resposta': processo.resposta.infEvento.cStat.valor,
                'status_motivo': processo.resposta.infEvento.xMotivo.valor,
                'reason': processo.resposta.reason}
        if processo.resposta.infEvento.cStat.valor == '135':
            vals['protocolo'] = processo.resposta.infEvento.nProt.valor

        return vals







