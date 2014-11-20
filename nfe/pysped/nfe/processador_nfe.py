# -*- coding: utf-8 -*-

from httplib import HTTPSConnection, HTTPResponse
from OpenSSL import crypto
import socket
import ssl
from datetime import datetime
import time
import os
from uuid import uuid4

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict

from webservices_flags import *
import webservices_2
import webservices_3

from nfe.pysped.xml_sped.certificado import Certificado



#
# Manual do Contribuinte versão 4.01
# NF-e leiaute 2.00
#
from manual_401 import SOAPEnvio_200, SOAPRetorno_200
from manual_401 import EnviNFe_200, RetEnviNFe_200
from manual_401 import ConsReciNFe_200, RetConsReciNFe_200, ProtNFe_200, ProcNFe_200
from manual_401 import CancNFe_200, RetCancNFe_200, ProcCancNFe_200, EnvEvento_200, RetEnvEvento_200, ProcEventoNFe_200
from manual_401 import InutNFe_200, RetInutNFe_200, ProcInutNFe_200
from manual_401 import ConsSitNFe_200, RetConsSitNFe_200, ConsCad_200, RetConsCad_200
from manual_401 import ConsStatServ_200, RetConsStatServ_200
from manual_401 import  EnvEventoCCe_200, RetEnvEventoCCe_200, ProcEventoNFeCCe_200

#
# Manual do Contribuinte versão 5.00
# NF-e leiaute 3.10
#
from manual_500 import SOAPEnvio_310, SOAPRetorno_310
from manual_500 import EnviNFe_310, RetEnviNFe_310
from manual_500 import ConsReciNFe_310, RetConsReciNFe_310, ProtNFe_310, ProcNFe_310
from manual_500 import CancNFe_310, RetCancNFe_310, ProcCancNFe_310, EnvEvento_310, RetEnvEvento_310, ProcEventoNFe_310
from manual_500 import InutNFe_310, RetInutNFe_310, ProcInutNFe_310
from manual_500 import ConsSitNFe_310, RetConsSitNFe_310, ConsCad_310, RetConsCad_310
from manual_500 import ConsStatServ_310, RetConsStatServ_310
from manual_500 import  EnvEventoCCe_310, RetEnvEventoCCe_310, ProcEventoNFeCCe_310


from manifestacao_destinatario import EnvConfRecebto_200, RetEnvConfRecebto_200
from manifestacao_destinatario import ConsNFeDest_200, RetConsNFeDest_200, ProcEventoNFeRecebto_200
from manifestacao_destinatario import DownloadNFe_200, RetDownloadNFe_200
from nfse import nfse_sete_lagoas
from nfse import codservico
#
# DANFE
#
from danfe.danferetrato import *

from StringIO import StringIO
import pytz
import tempfile


class ProcessoNFe(object):
    def __init__(self, webservice=0, envio=u'', resposta=u''):
        self.webservice = webservice
        self.envio = envio
        self.resposta = resposta


class ConexaoHTTPS(HTTPSConnection):
    def connect(self):
        "Connect to a host on a given (SSL) port."

        sock = socket.create_connection((self.host, self.port),
                                        self.timeout, self.source_address)
        if self._tunnel_host:
            self.sock = sock
            self._tunnel()
        self.sock = ssl.wrap_socket(sock, self.key_file, self.cert_file,
                                    ssl_version=ssl.PROTOCOL_SSLv3)


class ProcessadorNFe(object):
    def __init__(self):
        self.ambiente = 2
        self.estado = u'MG'
        self.versao = u'2.00'
        self.certificado = Certificado()
        self.caminho = u''
        self.salvar_arquivos = True
        self.tipo_contingencia = False
        self.danfe = DANFE()
        self.caminho_temporario = u''
        self.processos = []

        self._servidor     = u''
        self._url          = u''
        self._soap_envio   = None
        self._soap_retorno = None

    def _conectar_servico(self, servico, envio, resposta, ambiente=None):
        print 'nfe versao...', self.versao
        print 'conectando ao servico SEFAZ.........'
        if ambiente is None:
            ambiente = self.ambiente

        if self.versao == u'2.00':
            self._soap_envio   = SOAPEnvio_200()
            self._soap_envio.webservice = webservices_2.METODO_WS[servico]['webservice']
            self._soap_envio.metodo     = webservices_2.METODO_WS[servico]['metodo']
            self._soap_envio.cUF        = UF_CODIGO[self.estado]
            self._soap_envio.envio      = envio

            self._soap_retorno = SOAPRetorno_200()
            self._soap_retorno.webservice = webservices_2.METODO_WS[servico]['webservice']
            self._soap_retorno.metodo     = webservices_2.METODO_WS[servico]['metodo']
            self._soap_retorno.resposta   = resposta

            if not self.tipo_contingencia:
                self._servidor = webservices_2.ESTADO_WS[self.estado][ambiente][u'servidor']
                self._url      = webservices_2.ESTADO_WS[self.estado][ambiente][servico]
            elif self.tipo_contingencia == 'SCAN':
                self._servidor = webservices_2.SCAN[ambiente][u'servidor']
                self._url      = webservices_2.SCAN[ambiente][servico]
            elif self.tipo_contingencia == 'SVC-AN':
                self._servidor = webservices_2.SVC_AN[ambiente][u'servidor']
                self._url      = webservices_2.SVC_AN[ambiente][servico]
            elif self.tipo_contingencia == 'SVC-RS':
                self._servidor = webservices_2.SVC_RS[ambiente][u'servidor']
                self._url      = webservices_2.SVC_RS[ambiente][servico]


        if self.versao == u'3.10':
            self._soap_envio   = SOAPEnvio_310()
            self._soap_envio.webservice = webservices_3.METODO_WS[servico]['webservice']
            self._soap_envio.metodo     = webservices_3.METODO_WS[servico]['metodo']
            self._soap_envio.cUF        = UF_CODIGO[self.estado]
            self._soap_envio.envio      = envio

            self._soap_retorno = SOAPRetorno_310()
            self._soap_retorno.webservice = webservices_3.METODO_WS[servico]['webservice']
            self._soap_retorno.metodo     = webservices_3.METODO_WS[servico]['metodo']
            self._soap_retorno.resposta   = resposta

            if not self.tipo_contingencia:
                self._servidor = webservices_3.ESTADO_WS[self.estado][ambiente][u'servidor']
                self._url      = webservices_3.ESTADO_WS[self.estado][ambiente][servico]
            elif self.tipo_contingencia == 'SCAN':
                self._servidor = webservices_3.SCAN[ambiente][u'servidor']
                self._url      = webservices_3.SCAN[ambiente][servico]
            elif self.tipo_contingencia == 'SVC-AN':
                self._servidor = webservices_3.SVC_AN[ambiente][u'servidor']
                self._url      = webservices_3.SVC_AN[ambiente][servico]
            elif self.tipo_contingencia == 'SVC-RS':
                self._servidor = webservices_3.SVC_RS[ambiente][u'servidor']
                self._url      = webservices_3.SVC_RS[ambiente][servico]

        #try:
        self.certificado.prepara_certificado_arquivo_pfx()

        #
        # Salva o certificado e a chave privada para uso na conexão HTTPS
        # Salvamos como um arquivo de nome aleatório para evitar o conflito
        # de uso de vários certificados e chaves diferentes na mesma máquina
        # ao mesmo tempo
        #
        self.caminho_temporario = self.caminho_temporario or u'/tmp/'


        nome_arq_chave = tempfile.NamedTemporaryFile('w')
        nome_arq_chave.write(self.certificado.chave)
        nome_arq_chave.flush()

        nome_arq_certificado = tempfile.NamedTemporaryFile('w')
        nome_arq_certificado.write(self.certificado.certificado)
        nome_arq_certificado.flush()


        con = HTTPSConnection(self._servidor, key_file=nome_arq_chave.name, cert_file=nome_arq_certificado.name)
        #con = ConexaoHTTPS(self._servidor, key_file=nome_arq_chave, cert_file=nome_arq_certificado)
        con.request(u'POST', u'/' + self._url, self._soap_envio.xml.encode(u'utf-8'), self._soap_envio.header)
        resp = con.getresponse()

        #
        # Apagamos os arquivos do certificado e o da chave privada, para evitar
        # um potencial risco de segurança; muito embora o uso da chave privada
        # para assinatura exija o uso da senha, pode haver serviços que exijam
        # apenas o uso do certificado para validar a identidade, independente
        # da existência de assinatura digital
        #

        nome_arq_chave.close()
        nome_arq_certificado.close()

        # Dados da resposta salvos para possível debug
        self._soap_retorno.resposta.version  = resp.version
        self._soap_retorno.resposta.status   = resp.status
        self._soap_retorno.resposta.reason   = unicode(resp.reason.decode('utf-8'))
        self._soap_retorno.resposta.msg      = resp.msg
        self._soap_retorno.resposta.original = unicode(resp.read().decode('utf-8'))
        print 'servidor', self._servidor
        print 'STATUS________________________________________-', self._soap_retorno.resposta.original
        # Tudo certo!
        if self._soap_retorno.resposta.status == 200:
            self._soap_retorno.xml = self._soap_retorno.resposta.original
            print 15*'=='
            print self._soap_retorno.xml
            print 15*'=='
        #except Exception, e:
            #raise e
        #else:
        con.close()

    def enviar_lote(self, numero_lote=None, lista_nfes=[]):
        novos_arquivos = []


        if self.versao == u'2.00':
            envio = EnviNFe_200()
            resposta = RetEnviNFe_200()
            webservice = WS_NFE_ENVIO_LOTE
        elif self.versao == u'3.10':
            envio = EnviNFe_310()
            resposta = RetEnviNFe_310()
            webservice = WS_NFE_AUTORIZACAO

        processo = ProcessoNFe(webservice=webservice, envio=envio, resposta=resposta)

        #
        # Vamos assinar e validar todas as NF-e antes da transmissão, evitando
        # rejeição na SEFAZ por incorreção no schema dos arquivos
        #
        for nfe in lista_nfes:
            self.certificado.assina_xmlnfe(nfe)
            nfe.validar()

        envio.NFe = lista_nfes

        if numero_lote is None:
            numero_lote = datetime.now().strftime('%Y%m%d%H%M%S')

        envio.idLote.valor = numero_lote
        novos_arquivos.append(('numero_lote', numero_lote))
        envio.validar()
        
        for n in lista_nfes:
            n.monta_chave()
            novo_arquivo_nome = n.chave + u'-nfe.xml'
            novo_arquivo = n.xml.encode('utf-8')
            novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        novo_arquivo_nome = unicode(envio.idLote.valor).strip().rjust(15, u'0') + u'-env-lot.xml'
        novo_arquivo = envio.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))
       


        self._conectar_servico(webservice, envio, resposta)

        novo_arquivo_nome = unicode(envio.idLote.valor).strip().rjust(15, u'0') + u'-rec'

        if resposta.cStat.valor == u'103':
            novo_arquivo_nome += u'.xml'
        else:
            novo_arquivo_nome += u'-rej.xml'

        novo_arquivo = resposta.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        return processo, novos_arquivos

    def consultar_recibo(self, ambiente=None, numero_recibo=None):
        novos_arquivos = []

        if self.versao == u'2.00':
            envio = ConsReciNFe_200()
            resposta = RetConsReciNFe_200()
            webservice = WS_NFE_CONSULTA_RECIBO
        elif self.versao == u'3.10':
            envio = ConsReciNFe_310()
            resposta = RetConsReciNFe_310()
            webservice = WS_NFE_RET_AUTORIZACAO

        processo = ProcessoNFe(webservice=webservice, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        envio.tpAmb.valor = ambiente
        envio.nRec.valor  = numero_recibo

        envio.validar()

        novo_arquivo_nome = unicode(envio.nRec.valor).strip().rjust(15, u'0') + u'-ped-rec.xml'
        novo_arquivo = envio.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        self._conectar_servico(webservice, envio, resposta, ambiente)

        novo_arquivo_nome = unicode(envio.nRec.valor).strip().rjust(15, u'0') + u'-pro-rec'

        if resposta.cStat.valor == u'104':
            novo_arquivo_nome += u'.xml'
        else:
            novo_arquivo_nome += u'-rej.xml'

        novo_arquivo = resposta.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

            #
            # Salvar os resultados dos processamentos
            #
        for pn in resposta.protNFe:
            novo_arquivo_nome = unicode(pn.infProt.chNFe.valor).strip().rjust(44, u'0') + u'-pro-nfe-'

            # NF-e autorizada
            if pn.infProt.cStat.valor == u'100':
                novo_arquivo_nome += u'aut.xml'

            # NF-e denegada
            elif pn.infProt.cStat.valor in (u'110', u'301', u'302'):
                novo_arquivo_nome += u'den.xml'

            # NF-e rejeitada
            else:
                novo_arquivo_nome += u'rej.xml'

            novo_arquivo = pn.xml.encode('utf-8')
            novos_arquivos.append((novo_arquivo_nome, novo_arquivo))
            #--
            novos_arquivos.append(('status_resp', (pn.infProt.cStat.valor,pn.infProt.xMotivo.valor)))
        return processo, novos_arquivos

    def consultar_manifesto_destinatario(self, cnpj=None, ambiente=None, tipo_evento=None, chave_nfe=None):
        novos_arquivos = []

        envio = EnvConfRecebto_200()
        resposta = RetEnvConfRecebto_200()

        processo = ProcessoNFe(webservice=WS_NFE_EVENTO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        self.caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=chave_nfe)

        #evento
        envio.infEvento.tpAmb.valor = ambiente
        envio.infEvento.chNFe.valor = chave_nfe
        envio.infEvento.descEvento.valor = 'Confirmacao da Operacao'
        envio.infEvento.cOrgao.valor = 91# UF_CODIGO[self.estado] #O correto deve ser o codigo do ESTADO, mas como nem todos os webservices ainda estão disponíveis será usado 91
        envio.infEvento.tpEvento.valor = tipo_evento
        envio.infEvento.CNPJ.valor = cnpj
        dt = datetime.now()
        dt = dt.replace(tzinfo=pytz.utc)
        data_hora_tz = datetime.astimezone(dt, pytz.timezone("Brazil/East"))

        data_evento = datetime.strftime(data_hora_tz, u'%Y-%m-%dT%H:%M:%S')+str(data_hora_tz)[-6:]

        envio.infEvento.dhEvento.valor = data_evento


        self.certificado.prepara_certificado_arquivo_pfx()
        self.certificado.assina_xmlnfe(envio)

        envio.validar()

        novo_arquivo_nome = unicode(envio.infEvento.chNFe.valor).strip().rjust(44, u'0') + u'-consulta-evento.xml'
        novo_arquivo = envio.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))
#        print 'nfeevento', WS_NFE_EVENTO
        self._conectar_servico(WS_NFE_EVENTO, envio, resposta, ambiente)

        # Se for autorizado, monta o processo
        if resposta.cStat.valor == u'128':

            processo_evento_nfe = ProcEventoNFeRecebto_200()

            processo_evento_nfe.envEvento = envio
            processo_evento_nfe.retEnvEvento = resposta

            processo_evento_nfe.validar()

            processo.processo_evento_nfe = processo_evento_nfe

            novo_arquivo_nome = unicode(envio.infEvento.chNFe.valor).strip().rjust(44, u'0') + u'-proc-evento-'

            # Evento autorizado
            if resposta.infEvento.cStat.valor in (u'135'):
                novo_arquivo_nome += u'aut.xml'
            else:
                novo_arquivo_nome += u'rej.xml'

            novo_arquivo = resposta.xml.encode('utf-8')
            novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

            # Se for autorizado, monta o processo do evento da manifestação do destinatário
            if resposta.infEvento.cStat.valor == u'135':

                novo_arquivo_nome = unicode(envio.infEvento.chNFe.valor).strip().rjust(44, u'0') + u'-evento.xml'
                novo_arquivo = processo_evento_nfe.xml.encode('utf-8')
                novos_arquivos.append((novo_arquivo_nome, novo_arquivo))



        return processo

    def consultar_notas_destinatario(self, cnpj=None, ambiente=None, indnfe=None, indemi=None, nsu='0'):
        novos_arquivos = []

        envio = ConsNFeDest_200()
        resposta = RetConsNFeDest_200()

        processo = ProcessoNFe(webservice=WS_NFE_CONSULTA_DESTINATARIO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        self.caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=cnpj)

        #evento
        envio.tpAmb.valor = ambiente
        envio.CNPJ.valor = cnpj
        envio.indNFe.valor = indnfe
        envio.indEmi.valor = indemi
        envio.ultNSU.valor = nsu

        self.certificado.prepara_certificado_arquivo_pfx()

        envio.validar()

        novo_arquivo_nome = unicode(envio.CNPJ.valor).strip().rjust(14, u'0') + u'-consulta-cnpj-evento.xml'
        novo_arquivo = envio.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))
        self._conectar_servico(WS_NFE_CONSULTA_DESTINATARIO, envio, resposta, ambiente)

        return processo


    def download_nfe_xml(self, cnpj=None,ambiente=None, chave_nfe=None):
        novos_arquivos = []
        if self.versao == u'2.00':
            envio = DownloadNFe_200()
            resposta = RetDownloadNFe_200()

        processo = ProcessoNFe(webservice=WS_NFE_DOWNLOAD_XML_DESTINATARIO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        self.caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=cnpj)

        #evento
        envio.tpAmb.valor = ambiente
        envio.CNPJ.valor = cnpj
        envio.chNFe.valor = chave_nfe
        envio.xServ.valor = u'DOWNLOAD NFE'

        self.certificado.prepara_certificado_arquivo_pfx()

        envio.validar()

        novo_arquivo_nome = unicode(envio.CNPJ.valor).strip().rjust(14, u'0') + u'-consulta-cnpj-evento.xml'
        novo_arquivo = envio.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))
        self._conectar_servico(WS_NFE_DOWNLOAD_XML_DESTINATARIO, envio, resposta, ambiente)

        return processo

    def consultar_cadastro_contribuinte(self, cpf_cnpj=None, inscricao_estadual=None, uf=None, ambiente=None):
        novos_arquivos = []
        if self.versao == u'2.00':
            envio = ConsCad_200()
            resposta = RetConsCad_200()
        elif self.versao == u'3.10':
            envio = ConsCad_310()
            resposta = RetConsCad_310()

        processo = ProcessoNFe(webservice=WS_NFE_CONSULTA_CADASTRO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente
        if not uf:
            uf = self.estado
        envio.infCons.UF.valor = uf

        if inscricao_estadual:
            envio.infCons.IE.valor = inscricao_estadual
            nome = 'IE_' + inscricao_estadual
        elif len(cpf_cnpj) == 11:
            envio.infCons.CPF.valor = cpf_cnpj
            nome = 'CPF_' + cpf_cnpj
        elif len(cpf_cnpj) == 14:
            envio.infCons.CNPJ.valor = cpf_cnpj
            nome = 'CNPJ_' + cpf_cnpj
        envio.validar()

        self._conectar_servico(WS_NFE_CONSULTA_CADASTRO, envio, resposta, 1)

        novo_arquivo_nome = nome + u'-cons-cad.xml'
        novo_arquivo = resposta.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        return processo

    def corrigir_nota(self, chave_nfe=None, cnpj=None, texto_correcao=None, ambiente=None,
                      sequencia=None):
        novos_arquivos = []
        if self.versao == u'3.10':
            envio = EnvEventoCCe_310()
            resposta = RetEnvEventoCCe_310()
        elif self.versao == u'2.00':
            envio = EnvEventoCCe_200()
            resposta = RetEnvEventoCCe_200()

        processo = ProcessoNFe(webservice=WS_NFE_EVENTO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        self.caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=cnpj)

        envio.infEvento.tpAmb.valor = ambiente
        envio.infEvento.cOrgao.valor = UF_CODIGO[self.estado]
        envio.infEvento.CNPJ.valor = cnpj
        envio.infEvento.chNFe.valor = chave_nfe
        dt = datetime.now()
        dt = dt.replace(tzinfo=pytz.utc)
        data_hora_tz = datetime.astimezone(dt, pytz.timezone("Brazil/East"))
        data_evento = datetime.strftime(data_hora_tz, u'%Y-%m-%dT%H:%M:%S')+str(data_hora_tz)[-6:]
        envio.infEvento.dhEvento.valor = data_evento
        envio.infEvento.detEvento.xCorrecao.valor = texto_correcao
        envio.infEvento.nSeqEvento.valor = sequencia or 1
        self.certificado.prepara_certificado_arquivo_pfx()
        self.certificado.assina_xmlnfe(envio)

        envio.validar()
        novo_arquivo_nome = unicode(envio.infEvento.chNFe.valor).strip().rjust(44, u'0') + u'-cce.xml'
        novo_arquivo = envio.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        self._conectar_servico(WS_NFE_EVENTO, envio, resposta, ambiente)


        # Se for autorizado
        if resposta.cStat.valor == u'128':
            if self.versao == u'2.00':
                processo_correcao_nfe = ProcEventoNFeCCe_200()
            elif self.versao == u'3.10':
                processo_correcao_nfe = ProcEventoNFeCCe_310()
            processo_correcao_nfe.envEvento = envio
            processo_correcao_nfe.retEnvEvento = resposta

#            processo_correcao_nfe.validar()

            processo.processo_correcao_nfe = processo_correcao_nfe
            if self.salvar_arquivos:
                novo_arquivo_nome = unicode(envio.infEvento.chNFe.valor).strip().rjust(44, u'0') + u'-cce'

                # Correção autorizada
                if resposta.infEvento.cStat.valor in (u'135'):
                    novo_arquivo_nome += u'aut.xml'
                else:
                    novo_arquivo_nome += u'rej.xml'

                novo_arquivo = resposta.xml.encode('utf-8')
                novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

                # Se for autorizado, monta o processo de cancelamento
                if resposta.infEvento.cStat.valor == u'135':
                    # Estranhamente, o nome desse arquivo, pelo manual, deve ser chave-can.xml
                    novo_arquivo_nome = unicode(envio.infEvento.chNFe.valor).strip().rjust(44, u'0') + u'-cce.xml'
                    novo_arquivo = processo_correcao_nfe.xml.encode('utf-8')
                    novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        return processo

    def cancelar_nota(self, cnpj=None, ambiente=None, chave_nfe=None, numero_protocolo=None,
                      justificativa=None):
        novos_arquivos = []

        if self.versao == u'2.00':
            envio = EnvEvento_200()
            resposta = RetEnvEvento_200()
        elif self.versao == u'3.10':
            envio = EnvEvento_310()
            resposta = RetEnvEvento_310()

        processo = ProcessoNFe(webservice=WS_NFE_EVENTO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        self.caminho = self.monta_caminho_nfe(ambiente=ambiente, chave_nfe=chave_nfe)

        #evento
        envio.infEvento.tpAmb.valor = ambiente
        envio.infEvento.chNFe.valor = chave_nfe
        envio.infEvento.nProt.valor = numero_protocolo
        envio.infEvento.xJust.valor = justificativa
        envio.infEvento.cOrgao.valor = UF_CODIGO[self.estado]
        dt = datetime.now()
        dt = dt.replace(tzinfo=pytz.utc)
        data_hora_tz = datetime.astimezone(dt, pytz.timezone("Brazil/East"))

        data_evento = datetime.strftime(data_hora_tz, u'%Y-%m-%dT%H:%M:%S')+str(data_hora_tz)[-6:]

        envio.infEvento.dhEvento.valor = data_evento
        envio.infEvento.CNPJ.valor = cnpj

        
        self.certificado.prepara_certificado_arquivo_pfx()
        self.certificado.assina_xmlnfe(envio)

        envio.validar()

        novo_arquivo_nome = unicode(envio.infEvento.chNFe.valor).strip().rjust(44, u'0') + u'-ped-can.xml'
        novo_arquivo = envio.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        self._conectar_servico(WS_NFE_EVENTO, envio, resposta, ambiente)

        # Se for autorizado, monta o processo de cancelamento
        if resposta.cStat.valor == u'128':
            if self.versao == u'2.00':
                processo_cancelamento_nfe = ProcEventoNFe_200()
            elif self.versao == u'3.10':
                processo_cancelamento_nfe = ProcEventoNFe_310()
            processo_cancelamento_nfe.envEvento = envio
            processo_cancelamento_nfe.retEnvEvento = resposta

            processo_cancelamento_nfe.validar()

            processo.processo_cancelamento_nfe = processo_cancelamento_nfe

            novo_arquivo_nome = unicode(envio.infEvento.chNFe.valor).strip().rjust(44, u'0') + u'-pro-can-'

            # Cancelamento autorizado
            if resposta.infEvento.cStat.valor in (u'135'):
                novo_arquivo_nome += u'aut.xml'
            else:
                novo_arquivo_nome += u'rej.xml'

            novo_arquivo = resposta.xml.encode('utf-8')
            novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

            # Se for autorizado, monta o processo de cancelamento
            if resposta.infEvento.cStat.valor == u'135':
                # Estranhamente, o nome desse arquivo, pelo manual, deve ser chave-can.xml
                novo_arquivo_nome = unicode(envio.infEvento.chNFe.valor).strip().rjust(44, u'0') + u'-can.xml'
                novo_arquivo = processo_cancelamento_nfe.xml.encode('utf-8')
                novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        return processo

    def inutilizar_nota(self, ambiente=None, codigo_estado=None, ano=None, cnpj=None, serie=None,
                        numero_inicial=None, numero_final=None, justificativa=None):
        novos_arquivos = []

        if self.versao == u'2.00':
            envio = InutNFe_200()
            resposta = RetInutNFe_200()
        elif self.versao == u'3.10':
            envio = InutNFe_310()
            resposta = RetInutNFe_310()

        processo = ProcessoNFe(webservice=WS_NFE_INUTILIZACAO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        if codigo_estado is None:
            codigo_estado = UF_CODIGO[self.estado]

        if ano is None:
            ano = datetime.now().strftime(u'%y')

        if numero_final is None:
            numero_final = numero_inicial

        self.caminho = self.monta_caminho_inutilizacao(ambiente=ambiente, serie=serie,
                                    numero_inicial=numero_inicial, numero_final=numero_final)

        envio.infInut.tpAmb.valor  = ambiente
        envio.infInut.cUF.valor    = codigo_estado
        envio.infInut.ano.valor    = ano
        envio.infInut.CNPJ.valor   = cnpj
        #envio.infInut.mod.valor    = 55
        envio.infInut.serie.valor  = serie
        envio.infInut.nNFIni.valor = numero_inicial
        envio.infInut.nNFFin.valor = numero_final
        envio.infInut.xJust.valor  = justificativa

        envio.gera_nova_chave()
        self.certificado.prepara_certificado_arquivo_pfx()
        self.certificado.assina_xmlnfe(envio)

        envio.validar()

        novo_arquivo_nome = unicode(envio.chave).strip().rjust(41, u'0') + u'-ped-inu.xml'
        novo_arquivo = envio.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))
    
        self._conectar_servico(WS_NFE_INUTILIZACAO, envio, resposta, ambiente)

        # Se for autorizada, monta o processo de inutilização
        if resposta.infInut.cStat.valor == u'102':
            if self.versao == u'2.00':
                processo_inutilizacao_nfe = ProcInutNFe_200()

            elif self.versao == u'3.10':
                processo_inutilizacao_nfe = ProcInutNFe_310()

            processo_inutilizacao_nfe.inutNFe = envio
            processo_inutilizacao_nfe.retInutNFe = resposta

            processo_inutilizacao_nfe.validar()

            processo.processo_inutilizacao_nfe = processo_inutilizacao_nfe
            

        if self.salvar_arquivos:
            novo_arquivo_nome = unicode(envio.chave).strip().rjust(41, u'0') + u'-pro-inu-'

            # Inutilização autorizada
            if resposta.infInut.cStat.valor == u'102':
                novo_arquivo_nome += u'aut.xml'
            else:
                novo_arquivo_nome += u'rej.xml'

            novo_arquivo = resposta.xml.encode('utf-8')
            novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

            # Se for autorizada, monta o processo de inutilização
            if resposta.infInut.cStat.valor == u'102':
                novo_arquivo_nome = unicode(envio.chave).strip().rjust(41, u'0') + u'-proc-inut-nfe.xml'
                novo_arquivo = processo_inutilizacao_nfe.xml.encode('utf-8')
                novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

                # Estranhamente, o nome desse arquivo, pelo manual, deve ser chave-inu.xml
                novo_arquivo_nome = unicode(envio.chave).strip().rjust(41, u'0') + u'-inu.xml'
                novo_arquivo = processo_inutilizacao_nfe.xml.encode('utf-8')
                novos_arquivos.append((novo_arquivo_nome, novo_arquivo))
    
        return processo

    def consultar_nota(self, ambiente=None, chave_nfe=None, nfe=None):
        novos_arquivos = []

        if self.versao == u'2.00':
            envio = ConsSitNFe_200()
            resposta = RetConsSitNFe_200()
        elif self.versao == u'3.10':
            envio = ConsSitNFe_310()
            resposta = RetConsSitNFe_310()

        processo = ProcessoNFe(webservice=WS_NFE_CONSULTA, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        self.caminho = self.monta_caminho_nfe(ambiente, chave_nfe)

        envio.tpAmb.valor = ambiente
        envio.chNFe.valor = chave_nfe
        
        envio.validar()

        novo_arquivo_nome = unicode(chave_nfe).strip().rjust(44, u'0') + u'-ped-sit.xml'
        novo_arquivo = envio.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))
        

        self._conectar_servico(WS_NFE_CONSULTA, envio, resposta, ambiente)

        novo_arquivo_nome = unicode(chave_nfe).strip().rjust(44, u'0') + u'-sit.xml'
        novo_arquivo = resposta.xml.encode('utf-8')
       
        
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        return processo, novos_arquivos

    def consultar_servico(self, ambiente=None, codigo_estado=None):
        novos_arquivos = []

        if self.versao == u'2.00':
            envio = ConsStatServ_200()
            resposta = RetConsStatServ_200()
        elif self.versao == u'3.10':
            envio = ConsStatServ_310()
            resposta = RetConsStatServ_310()

        processo = ProcessoNFe(webservice=WS_NFE_SITUACAO, envio=envio, resposta=resposta)

        if ambiente is None:
            ambiente = self.ambiente

        if codigo_estado is None:
            codigo_estado = UF_CODIGO[self.estado]

        envio.tpAmb.valor = ambiente
        envio.cUF.valor   = codigo_estado
        envio.data        = datetime.now()

        envio.validar()

        novo_arquivo_nome = envio.data.strftime(u'%Y%m%dT%H%M%S') + u'-ped-sta.xml'
        novo_arquivo = envio.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        self._conectar_servico(WS_NFE_SITUACAO, envio, resposta, ambiente)

        novo_arquivo_nome = envio.data.strftime(u'%Y%m%dT%H%M%S') + u'-sta.xml'
        novo_arquivo = resposta.xml.encode('utf-8')
        novos_arquivos.append((novo_arquivo_nome, novo_arquivo))

        return processo, novos_arquivos

    def processar_notas(self, lista_nfes):
        #
        # Definir o caminho geral baseado na 1ª NF-e
        #
        self.processos = processos = OrderedDict()
        novos_arquivos = []

        caminho_original = self.caminho
        nfe = lista_nfes[0]
        nfe.monta_chave()
        self.caminho = caminho_original
        ambiente = nfe.infNFe.ide.tpAmb.valor
        self.caminho = self.monta_caminho_nfe(ambiente=nfe.infNFe.ide.tpAmb.valor, chave_nfe=nfe.chave)

        proc_servico, novos_arquivos = self.consultar_servico(ambiente=ambiente)
        processos['servico'] = proc_servico, novos_arquivos
        yield proc_servico

        #
        # Serviço em operação?
        #
        print 'resposta', proc_servico.resposta.cStat.valor
        if proc_servico.resposta.cStat.valor == u'107':
            #
            # Verificar se as notas já não foram emitadas antes
            #
            for nfe in lista_nfes:
                nfe.monta_chave()
                self.caminho = caminho_original
                proc_consulta, novos_arquivos = self.consultar_nota(ambiente=nfe.infNFe.ide.tpAmb.valor, chave_nfe=nfe.chave)
                processos['consulta'] = proc_consulta, novos_arquivos
                yield proc_consulta

                #
                # Se a nota já constar na SEFAZ
                #
                if not (
                    ((self.versao == u'1.10') and (proc_consulta.resposta.infProt.cStat.valor in (u'217', u'999',)))
                    or
                    ((self.versao in (u'2.00',u'3.10')) and (proc_consulta.resposta.cStat.valor in (u'217', u'999',)))
                ):
                    #
                    # Interrompe todo o processo
                    #
                    return

            #
            # Nenhuma das notas estava já enviada, enviá-las então
            #
            nfe = lista_nfes[0]
            nfe.monta_chave()
            self.caminho = caminho_original
            self.caminho = self.monta_caminho_nfe(ambiente=nfe.infNFe.ide.tpAmb.valor, chave_nfe=nfe.chave)
            proc_envio, novos_arquivos = self.enviar_lote(lista_nfes=lista_nfes)
            processos['envio'] = proc_envio, novos_arquivos
            yield proc_envio

            ret_envi_nfe = proc_envio.resposta

            #
            # Deu certo?
            #
            print 'Deu certo.... :)',ret_envi_nfe.cStat.valor
            if ret_envi_nfe.cStat.valor == u'103':
                time.sleep(ret_envi_nfe.infRec.tMed.valor * 3) # Espere o processamento antes de consultar o recibo
                proc_recibo, novos_arquivos = self.consultar_recibo(ambiente=ret_envi_nfe.tpAmb.valor, numero_recibo=ret_envi_nfe.infRec.nRec.valor)
                processos['recibo'] = proc_recibo, novos_arquivos
                yield proc_recibo

                # Montar os processos das NF-es
                dic_protNFe = proc_recibo.resposta.dic_protNFe
                dic_procNFe = proc_recibo.resposta.dic_procNFe

                self.caminho = caminho_original
                novos_processos = self.montar_processo_lista_notas(lista_nfes, dic_protNFe, dic_procNFe)
                for i,novo_processo in enumerate(novos_processos):
                    processos['nota_%i' % i] = novo_processo
                return

    def montar_processo_lista_notas(self, lista_nfes, dic_protNFe, dic_procNFe):
        processos = []
        for nfe in lista_nfes:
            if dic_protNFe.has_key(nfe.chave):
                protocolo = dic_protNFe[nfe.chave]
                processo, novos_arquivos = self.montar_processo_uma_nota(nfe, protnfe_recibo=protocolo)
                processos.append((processo, novos_arquivos))
                if processo is not None:
                    dic_procNFe[nfe.chave] = processo
        return processos

    def montar_processo_uma_nota(self, nfe, protnfe_recibo=None, protnfe_consulta_110=None, retcancnfe=None):
        novos_arquivos = []
        #
        # Somente para a versão 1.10
        # Caso processarmos o protocolo vindo de uma consulta,
        # temos que converter esse protocolo no formato
        # do protocolo que retorna quando o recibo do lote é consultado.
        #
        # Sim, as informações são as mesmas, mas o leiaute não...
        # Vai entender...
        #

        caminho_original = self.caminho
        self.caminho = self.monta_caminho_nfe(ambiente=nfe.infNFe.ide.tpAmb.valor, chave_nfe=nfe.chave)

        processo = None
        # Se nota foi autorizada ou denegada
        if protnfe_recibo.infProt.cStat.valor in (u'100', u'110', u'301', u'302'):

            if self.versao == u'2.00':
                processo = ProcNFe_200()
            elif self.versao == u'3.10':
                processo = ProcNFe_310()

            processo.NFe     = nfe
            processo.protNFe = protnfe_recibo
            novos_arquivos.append(('numero_protocolo', protnfe_recibo.infProt.nProt.valor))
            
            novo_arquivo_nome = unicode(nfe.chave).strip().rjust(44, u'0') + u'-proc-nfe.xml'
            novo_arquivo = processo.xml.encode('utf-8')
            novos_arquivos.append((novo_arquivo_nome, novo_arquivo))
            
            # Estranhamente, o nome desse arquivo, pelo manual, deve ser chave-nfe.xml ou chave-den.xml
            # para notas denegadas
            if protnfe_recibo.infProt.cStat.valor == u'100':
                novo_arquivo_nome = unicode(nfe.chave).strip().rjust(44, u'0') + u'-nfe.xml'
            else:
                novo_arquivo_nome = unicode(nfe.chave).strip().rjust(44, u'0') + u'-den.xml'

            novo_arquivo_nome = novo_arquivo_nome
            novo_arquivo = processo.xml.encode('utf-8')
            novos_arquivos.append((novo_arquivo_nome, novo_arquivo))
                

        self.caminho = caminho_original
        return processo, novos_arquivos

    def monta_caminho_nfe(self, ambiente, chave_nfe):
        caminho = self.caminho

        if ambiente == 1:
            caminho = os.path.join(caminho, 'producao/')
        else:
            caminho = os.path.join(caminho, 'homologacao/')

        data = u'20' + chave_nfe[2:4] + u'-' + chave_nfe[4:6]
        serie = chave_nfe[22:25]
        numero = chave_nfe[25:34]

        caminho = os.path.join(caminho, data + u'/')
        caminho = os.path.join(caminho, serie + u'-' + numero + u'/')

        try:
            os.makedirs(caminho)
        except:
            pass

        return caminho

    def monta_caminho_inutilizacao(self, ambiente=None, data=None, serie=None, numero_inicial=None, numero_final=None):
        caminho = self.caminho

        if ambiente == 1:
            caminho = os.path.join(caminho, 'producao/')
        else:
            caminho = os.path.join(caminho, 'homologacao/')

        if data is None:
            data = datetime.now()

        caminho = os.path.join(caminho, data.strftime(u'%Y-%m') + u'/')

        serie          = unicode(serie).strip().rjust(3, u'0')
        numero_inicial = unicode(numero_inicial).strip().rjust(9, u'0')
        numero_final   = unicode(numero_final).strip().rjust(9, u'0')

        caminho = os.path.join(caminho, serie + u'-' + numero_inicial + u'-' + numero_final + u'/')

        try:
            os.makedirs(caminho)
        except:
            pass

        return caminho

    def salvar_arquivos_agora(self):
        caminho = self.caminho

        if self.ambiente == 1:
            caminho = os.path.join(caminho, 'producao/')
        else:
            caminho = os.path.join(caminho, 'homologacao/')

        try:
            os.makedirs(caminho)
        except:
            pass

        for nome, processo in self.processos.iteritems():
            for arquivo in processo[1]:
                nome_arquivo, conteudo = arquivo
                arquivo_em_disco = open(os.path.join(caminho, nome_arquivo), 'w')
                if hasattr(conteudo, 'getvalue'):
                    arquivo_em_disco.write(conteudo.getvalue())
                else:
                    arquivo_em_disco.write(conteudo)
                arquivo_em_disco.close()



class DANFE(object):
    def __init__(self):
        self.imprime_canhoto        = True
        self.imprime_local_retirada = True
        self.imprime_local_entrega  = True
        self.imprime_fatura         = True
        self.imprime_duplicatas     = True
        self.imprime_issqn          = True

        self.caminho           = u''
        self.salvar_arquivo    = False

        self.NFe        = None
        self.protNFe    = None
        self.retCancNFe = None
        self.danfe      = None
        self.versao     = '2.00'

        self.obs_impressao    = u'DANFE gerado em %(now:%d/%m/%Y, %H:%M:%S)s'
        self.nome_sistema     = u''
        self.site             = u''
        self.logo             = u''
        self.leiaute_logo_vertical = False
        self.dados_emitente   = []

    def gerar_danfe(self):
        if self.NFe is None:
            raise ValueError(u'Não é possível gerar um DANFE sem a informação de uma NF-e')

        if self.protNFe is None:
            if self.versao == u'2.00':
                self.protNFe = ProtNFe_200()
            elif self.versao == u'3.10':
                self.protNFe = ProtNFe_310()

        if self.retCancNFe is None:
            if self.versao == u'2.00':
                self.retCancNFe = RetCancNFe_200()
            elif self.versao == u'3.10':
                self.retCancNFe = RetCancNFe_310()

        #
        # Prepara o queryset para impressão
        #
        self.NFe.monta_chave()
        self.NFe.monta_dados_contingencia_fsda()
        self.NFe.site = self.site

        for detalhe in self.NFe.infNFe.det:
            detalhe.NFe = self.NFe
            detalhe.protNFe = self.protNFe
            detalhe.retCancNFe = self.retCancNFe

        #
        # Prepara as bandas de impressão para cada formato
        #
        if self.NFe.infNFe.ide.tpImp.valor == 2:
            raise ValueError(u'DANFE em formato paisagem ainda não implementado')
        else:
            self.danfe = DANFERetrato()
            self.danfe.queryset = self.NFe.infNFe.det

        if self.imprime_canhoto:
            self.danfe.band_page_header = self.danfe.canhoto
            self.danfe.band_page_header.child_bands = []
            self.danfe.band_page_header.child_bands.append(self.danfe.remetente)
        else:
            self.danfe.band_page_header = self.danfe.remetente
            self.danfe.band_page_header.child_bands = []

        # Emissão para simples conferência / sem protocolo de autorização
#        self.protNFe
 
        if not self.protNFe.infProt.nProt.valor:
            self.danfe.remetente.campo_variavel_conferencia()

        # NF-e denegada
        elif self.protNFe.infProt.cStat.valor == u'110':
            self.danfe.remetente.campo_variavel_denegacao()
            self.danfe.remetente.obs_denegacao()

        # Emissão em contingência com FS ou FSDA
        elif self.NFe.infNFe.ide.tpEmis.valor in (2, 5,):
            self.danfe.remetente.campo_variavel_contingencia_fsda()
            self.danfe.remetente.obs_contingencia_normal_scan()

        # Emissão em contingência com DPEC
        elif self.NFe.infNFe.ide.tpEmis.valor == 4:
            self.danfe.remetente.campo_variavel_contingencia_dpec()
            self.danfe.remetente.obs_contingencia_dpec()

        # Emissão normal ou contingência SCAN, SVC-AN e SVC-RS
        else:
            self.danfe.remetente.campo_variavel_normal()
            # Contingência SCAN,SVC-AN e SVC-RS
            if self.NFe.infNFe.ide.tpEmis.valor in (3, 6, 7):
                self.danfe.remetente.obs_contingencia_normal_scan()

        # A NF-e foi cancelada, no DANFE imprimir o "carimbo" de cancelamento
        if self.retCancNFe.infCanc.nProt.valor:
            self.danfe.remetente.obs_cancelamento()

        # Observação de ausência de valor fiscal
        # se não houver protocolo ou se o ambiente for de homologação
        if (not self.protNFe.infProt.nProt.valor) or self.NFe.infNFe.ide.tpAmb.valor == 2:
            self.danfe.remetente.obs_sem_valor_fiscal()

        self.danfe.band_page_header.child_bands.append(self.danfe.destinatario)

        if self.imprime_local_retirada and len(self.NFe.infNFe.retirada.xml):
            self.danfe.band_page_header.child_bands.append(self.danfe.local_retirada)

        if self.imprime_local_entrega and len(self.NFe.infNFe.entrega.xml):
            self.danfe.band_page_header.child_bands.append(self.danfe.local_entrega)

        if self.imprime_fatura:
            # Pagamento a prazo
            if (self.NFe.infNFe.ide.indPag.valor == 1) or \
                (len(self.NFe.infNFe.cobr.dup) > 1) or \
                ((len(self.NFe.infNFe.cobr.dup) == 1) and \
                (self.NFe.infNFe.cobr.dup[0].dVenc.xml > self.NFe.infNFe.ide.dEmi.xml)):

                if self.imprime_duplicatas:
                    self.danfe.fatura_a_prazo.elements.append(self.danfe.duplicatas)

                self.danfe.band_page_header.child_bands.append(self.danfe.fatura_a_prazo)

            # Pagamento a vista
            else:
                self.danfe.band_page_header.child_bands.append(self.danfe.fatura_a_vista)

        self.danfe.band_page_header.child_bands.append(self.danfe.calculo_imposto)
        self.danfe.band_page_header.child_bands.append(self.danfe.transporte)
        self.danfe.band_page_header.child_bands.append(self.danfe.cab_produto)

#        self.danfe.band_page_footer = self.danfe.iss

        if self.imprime_issqn and len(self.NFe.infNFe.total.ISSQNTot.xml):
            self.danfe.band_page_footer = self.danfe.iss
        else:
            self.danfe.band_page_footer = self.danfe.dados_adicionais

        self.danfe.band_detail = self.danfe.det_produto

        #
        # Observação de impressão
        #
        if self.nome_sistema:
            self.danfe.ObsImpressao.expression = self.nome_sistema + u' - ' + self.obs_impressao
        else:
            self.danfe.ObsImpressao.expression = self.obs_impressao

        #
        # Quadro do emitente
        #
        # Personalizado?
        if self.dados_emitente:
            self.danfe.remetente.monta_quadro_emitente(self.dados_emitente)
        else:
            # Sem logotipo
            if not self.logo:
                self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_sem_logo())

            # Logotipo na vertical
            elif self.leiaute_logo_vertical:
                self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_logo_vertical(self.logo))

            # Logotipo na horizontal
            else:
                self.danfe.remetente.monta_quadro_emitente(self.danfe.remetente.dados_emitente_logo_horizontal(self.logo))

        if self.salvar_arquivo:
            nome_arq = self.caminho + self.NFe.chave + u'.pdf'
            type(self.danfe.generate_by(PDFGenerator, filename=nome_arq))


