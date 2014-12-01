# -*- coding: utf-8 -*-

from webservices_flags import *


METODO_WS = {
    WS_NFE_ENVIO_LOTE: {
        u'webservice': u'NfeRecepcao2',
        u'metodo'    : u'nfeRecepcaoLote2',
        },
    WS_NFE_CONSULTA_RECIBO: {
        u'webservice': u'NfeRetRecepcao2',
        u'metodo'    : u'nfeRetRecepcao2',
        },
    WS_NFE_CANCELAMENTO: {
        u'webservice': u'NfeCancelamento2',
        u'metodo'    : u'nfeCancelamentoNF2',
        },

    WS_NFE_EVENTO: {
        u'webservice': u'RecepcaoEvento',
        u'metodo'    : u'nfeRecepcaoEvento',
        },

    WS_NFE_CONSULTA_DESTINATARIO: {
        u'webservice': u'NfeConsultaDest',
        u'metodo'    : u'nfeConsultaDest',
        },
    WS_NFE_DOWNLOAD_XML_DESTINATARIO: {
        u'webservice': u'NfeDownloadNF',
        u'metodo'    : u'nfeDownloadNF',
        },

    WS_NFE_INUTILIZACAO: {
        u'webservice': u'NfeInutilizacao2',
        u'metodo'    : u'nfeInutilizacaoNF2',
        },
    WS_NFE_CONSULTA: {
        u'webservice': u'NfeConsulta2',
        u'metodo'    : u'nfeConsultaNF2',
        },
    WS_NFE_SITUACAO: {
        u'webservice': u'NfeStatusServico2',
        u'metodo'    : u'nfeStatusServicoNF2',
        },
    WS_NFE_CONSULTA_CADASTRO: {
        u'webservice': u'CadConsultaCadastro2',
        u'metodo'    : u'consultaCadastro2',
        },

    WS_NFE_AUTORIZACAO:{
        u'webservice': u'NfeAutorizacao',
        u'metodo': u'nfeAutorizacaoLote'
    },

    WS_NFE_RET_AUTORIZACAO:{
        u'webservice': u'NfeRetAutorizacao',
        u'metodo': u'nfeRetAutorizacaoLote'
    },

}

'''Fonte:http://www.nfe.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=Wak0FwB7dKs=
Ultima atualizacao 01-09-2014'''


'''
Sefaz Virtual Rio Grande do Sul - (SVRS)
Serviço	Versão	URL
RecepcaoEvento	1.00	https://nfe.sefazvirtual.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx
NfeRecepcao	2.00	https://nfe.sefazvirtual.rs.gov.br/ws/Nferecepcao/NFeRecepcao2.asmx
NfeRetRecepcao	2.00	https://nfe.sefazvirtual.rs.gov.br/ws/NfeRetRecepcao/NfeRetRecepcao2.asmx
NfeConsultaCadastro	2.00	https://svp-ws.sefazvirtual.rs.gov.br/ws/CadConsultaCadastro/CadConsultaCadastro2.asmx
NfeInutilizacao	2.00 / 3.10	https://nfe.sefazvirtual.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao2.asmx
NfeConsultaProtocolo	2.00 / 3.10	https://nfe.sefazvirtual.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx
NfeStatusServico	2.00 / 3.10	https://nfe.sefazvirtual.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx
NFeAutorizacao	3.10	https://nfe.sefazvirtual.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx
NFeRetAutorizacao	3.10	https://nfe.sefazvirtual.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx
'''

SVRS = {

    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE        : u'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO: u'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'ws/recepcaoevento/recepcaoevento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'ws/nfeConsultaDest/nfeConsultaDest.asmx',
        WS_NFE_INUTILIZACAO    : u'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'ws/nfestatusservico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'ws/CadConsultaCadastro/CadConsultaCadastro2.asmx',
        WS_NFE_AUTORIZACAO: u'ws/NFeAutorizacao/NFeAutorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'ws/NFeRetAutorizacao/NFeRetAutorizacao.asmx'
        },


    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'homologacao.nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE        : u'ws/nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO: u'ws/nferetrecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'ws/nfecancelamento/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'ws/recepcaoevento/recepcaoevento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'ws/nfeConsultaDest/nfeConsultaDest.asmx',
        WS_NFE_INUTILIZACAO    : u'ws/nfeinutilizacao/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'ws/nfeconsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'ws/nfestatusservico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'ws/CadConsultaCadastro/CadConsultaCadastro2.asmx',
        WS_NFE_AUTORIZACAO: u'ws/NFeAutorizacao/NFeAutorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'ws/NFeRetAutorizacao/NFeRetAutorizacao.asmx'
        }
}





SVAN = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'www.sefazvirtual.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NFeRetRecepcao2/NFeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NFeCancelamento2/NFeCancelamento2.asmx',
        WS_NFE_EVENTO : u'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'NFeConsultaDest/NFeConsultaDest.asmx',
        WS_NFE_INUTILIZACAO    : u'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'nfeconsulta2/nfeconsulta2.asmx',
        WS_NFE_SITUACAO        : u'NFeStatusServico2/NFeStatusServico2.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hom.nfe.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NFeRetRecepcao2/NFeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NFeCancelamento2/NFeCancelamento2.asmx',
        WS_NFE_EVENTO : u'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'NFeConsultaDest/NFeConsultaDest.asmx',
        WS_NFE_DOWNLOAD_XML_DESTINATARIO: u'NfeDownloadNF/NfeDownloadNF.asmx',
        WS_NFE_INUTILIZACAO    : u'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'nfeconsulta2/nfeconsulta2.asmx',
        WS_NFE_SITUACAO        : u'NFeStatusServico2/NFeStatusServico2.asmx'
    }
}


#Ambiente Nacional - (AN)
#Serviço	Versão	URL
#RecepcaoEvento	2.00	https://www.nfe.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx
#NfeConsultaDest	2.00	https://www.nfe.fazenda.gov.br/NFeConsultaDest/NFeConsultaDest.asmx
#NfeDownloadNF	2.00	https://www.nfe.fazenda.gov.br/NfeDownloadNF/NfeDownloadNF.asmx
#NfeRecepcao	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeRecepcao2/NfeRecepcao2.asmx
#NfeRetRecepcao	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeRetRecepcao2/NfeRetRecepcao2.asmx
#NfeInutilizacao	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeInutilizacao2/NfeInutilizacao2.asmx
#NfeConsultaProtocolo	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeConsulta2/NfeConsulta2.asmx
#NfeStatusServico	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeStatusServico2/NfeStatusServico2.asmx
#RecepcaoEvento	2.00	https://www.sefazvirtual.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx
#NfeDownloadNF	2.00	https://www.sefazvirtual.fazenda.gov.br/NfeDownloadNF/NfeDownloadNF.asmx

SCAN = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'www.scan.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NfeRetRecepcao2/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NfeCancelamento2/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'NFeConsultaDest/NFeConsultaDest.asmx',
        WS_NFE_INUTILIZACAO    : u'NfeInutilizacao2/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'NfeConsulta2/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'NfeStatusServico2/NfeStatusServico2.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hom.nfe.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'SCAN/NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'SCAN/NfeRetRecepcao2/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'SCAN/NfeCancelamento2/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'SCAN/RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_CONSULTA_DESTINATARIO : u'SCAN/NFeConsultaDest/NFeConsultaDest.asmx',
        WS_NFE_INUTILIZACAO    : u'SCAN/NfeInutilizacao2/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'SCAN/NfeConsulta2/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'SCAN/NfeStatusServico2/NfeStatusServico2.asmx'
    }
}


#Sefaz Contingência Ambiente Nacional - (SCAN)
#Serviço	Versão	URL
#NfeRecepcao	2.00	https://www.scan.fazenda.gov.br/NfeRecepcao2/NfeRecepcao2.asmx
#NfeRetRecepcao	2.00	https://www.scan.fazenda.gov.br/NfeRetRecepcao2/NfeRetRecepcao2.asmx
#NfeInutilizacao	2.00	https://www.scan.fazenda.gov.br/NfeInutilizacao2/NfeInutilizacao2.asmx
#NfeConsultaProtocolo	2.00	https://www.scan.fazenda.gov.br/NfeConsulta2/NfeConsulta2.asmx
#NfeStatusServico	2.00	https://www.scan.fazenda.gov.br/NfeStatusServico2/NfeStatusServico2.asmx
#RecepcaoEvento	2.00	https://www.scan.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx


DPEC = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'     : u'www.nfe.fazenda.gov.br',
        WS_DPEC_CONSULTA: u'SCERecepcaoRFB/SCERecepcaoRFB.asmx',
        WS_DPEC_RECEPCAO: u'SCEConsultaRFB/SCEConsultaRFB.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'     : u'hom.nfe.fazenda.gov.br',
        WS_DPEC_CONSULTA: u'SCERecepcaoRFB/SCERecepcaoRFB.asmx',
        WS_DPEC_RECEPCAO: u'SCEConsultaRFB/SCEConsultaRFB.asmx'
    }
}

#UFAM = {
#NFE_AMBIENTE_PRODUCAO: {
#u'servidor'            : u'nfe.sefaz.am.gov.br',
#WS_NFE_ENVIO_LOTE        : u'ws/services/NfeRecepcao',
#WS_NFE_CONSULTA_RECIBO: u'ws/services/NfeRetRecepcao',
#WS_NFE_CANCELAMENTO    : u'ws/services/NfeCancelamento',
#WS_NFE_INUTILIZACAO    : u'ws/services/NfeInutilizacao',
#WS_NFE_CONSULTA        : u'ws/services/NfeConsulta',
#WS_NFE_SITUACAO        : u'ws/services/NfeStatusServico'
#},
#NFE_AMBIENTE_HOMOLOGACAO: {
#u'servidor'            : u'homnfe.sefaz.am.gov.br',
#WS_NFE_ENVIO_LOTE        : u'ws/services/NfeRecepcao',
#WS_NFE_CONSULTA_RECIBO: u'ws/services/NfeRetRecepcao',
#WS_NFE_CANCELAMENTO    : u'ws/services/NfeCancelamento',
#WS_NFE_INUTILIZACAO    : u'ws/services/NfeInutilizacao',
#WS_NFE_CONSULTA        : u'ws/services/NfeConsulta',
#WS_NFE_SITUACAO        : u'ws/services/NfeStatusServico'
#}
#}


'''
Sefaz Amazonas - (AM)
Serviço	Versão	URL
RecepcaoEvento	1.00	https://nfe.sefaz.am.gov.br/services2/services/RecepcaoEvento
NfeRecepcao	2.00	https://nfe.sefaz.am.gov.br/services2/services/NfeRecepcao2
NfeRetRecepcao	2.00	https://nfe.sefaz.am.gov.br/services2/services/NfeRetRecepcao2
NfeInutilizacao	2.00 / 3.10	https://nfe.sefaz.am.gov.br/services2/services/NfeInutilizacao2
NfeConsultaProtocolo	2.00 / 3.10	https://nfe.sefaz.am.gov.br/services2/services/NfeConsulta2
NfeStatusServico	2.00 / 3.10	https://nfe.sefaz.am.gov.br/services2/services/NfeStatusServico2
NfeConsultaCadastro	2.00 / 3.10	https://nfe.sefaz.am.gov.br/services2/services/cadconsultacadastro2
NFeAutorizacao	3.10	https://nfe.sefaz.am.gov.br/services2/services/NfeAutorizacao
NFeRetAutorizacao	3.10	https://nfe.sefaz.am.gov.br/services2/services/NfeRetAutorizacao
'''



UFAM = {
    # NfeConsultaCadastro	2.00	https://nfe.sefaz.am.gov.br/services2/services/cadconsultacadastro2
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe.sefaz.am.gov.br',
        WS_NFE_ENVIO_LOTE       : u'services2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'services2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'services2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'services2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'services2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'services2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'services2/services/cadconsultacadastro2',
        #        WS_NFE_RECEPCAO_EVENTO  : 'services2/services/RecepcaoEvento',
        WS_NFE_AUTORIZACAO: u'services2/services/NFeAutorizacao',
        WS_NFE_RET_AUTORIZACAO: u'services2/services/NFeRetAutorizacao'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'            : u'homnfe.sefaz.am.gov.br',
        WS_NFE_ENVIO_LOTE       : u'services2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'services2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'services2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'services2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'services2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'services2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'services2/services/cadconsultacadastro2',
        #        WS_NFE_RECEPCAO_EVENTO  : 'services2/services/RecepcaoEvento',
        WS_NFE_AUTORIZACAO: u'services2/services/NFeAutorizacao',
        WS_NFE_RET_AUTORIZACAO: u'services2/services/NFeRetAutorizacao'
    }
}


'''
Sefaz Bahia - (BA)
Serviço	Versão	URL
NfeRecepcao	2.00	https://nfe.sefaz.ba.gov.br/webservices/nfenw/NfeRecepcao2.asmx
NfeRetRecepcao	2.00	https://nfe.sefaz.ba.gov.br/webservices/nfenw/NfeRetRecepcao2.asmx
NfeConsultaProtocolo	2.00	https://nfe.sefaz.ba.gov.br/webservices/nfenw/nfeconsulta2.asmx
NfeStatusServico	2.00	https://nfe.sefaz.ba.gov.br/webservices/nfenw/NfeStatusServico2.asmx
NfeInutilizacao	2.00 / 3.10	https://nfe.sefaz.ba.gov.br/webservices/nfenw/nfeinutilizacao2.asmx
NfeConsultaCadastro	2.00 / 3.10	https://nfe.sefaz.ba.gov.br/webservices/nfenw/CadConsultaCadastro2.asmx
RecepcaoEvento	2.00 / 3.10	https://nfe.sefaz.ba.gov.br/webservices/sre/recepcaoevento.asmx
NfeConsultaProtocolo	3.10	https://nfe.sefaz.ba.gov.br/webservices/NfeConsulta/NfeConsulta.asmx
NfeStatusServico	3.10	https://nfe.sefaz.ba.gov.br/webservices/NfeStatusServico/NfeStatusServico.asmx
NFeAutorizacao	3.10	https://nfe.sefaz.ba.gov.br/webservices/NfeAutorizacao/NfeAutorizacao.asmx
NFeRetAutorizacao	3.10	https://nfe.sefaz.ba.gov.br/webservices/NfeRetAutorizacao/NfeRetAutorizacao.asmx
'''



UFBA = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'             : u'nfe.sefaz.ba.gov.br',
        WS_NFE_ENVIO_LOTE       : u'webservices/nfenw/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'webservices/nfenw/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'webservices/nfenw/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'webservices/sre/RecepcaoEvento.asmx',
        WS_NFE_INUTILIZACAO     : u'webservices/nfenw/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'webservices/nfenw/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : u'webservices/nfenw/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'webservices/nfenw/CadConsultaCadastro2.asmx',
        WS_NFE_AUTORIZACAO: u'webservices/NfeAutorizacao/NfeAutorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'webservices/NfeRetAutorizacao/NfeRetAutorizacao.asmx'
        #        WS_NFE_RECEPCAO_EVENTO  : 'webservices/sre/RecepcaoEvento.asmx',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hnfe.sefaz.ba.gov.br',
        WS_NFE_ENVIO_LOTE      : u'webservices/nfenw/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'webservices/nfenw/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'webservices/nfenw/NfeCancelamento2.asmx',
        WS_NFE_EVENTO : u'webservices/sre/RecepcaoEvento.asmx',
        WS_NFE_INUTILIZACAO    : u'webservices/nfenw/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'webservices/nfenw/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'webservices/nfenw/NfeStatusServico2.asmx',
        WS_NFE_AUTORIZACAO: u'webservices/NfeAutorizacao/NfeAutorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'webservices/NfeRetAutorizacao/NfeRetAutorizacao.asmx'
    }
}

UFCE = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe.sefaz.ce.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe2/services/CadConsultaCadastro2',
        #        WS_NFE_RECEPCAO_EVENTO  : 'nfe2/services/RecepcaoEvento',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'              : u'nfeh.sefaz.ce.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe2/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe2/services/CadConsultaCadastro2',
        #        WS_NFE_RECEPCAO_EVENTO  : 'nfe2/services/RecepcaoEvento',
    }
}

#UFDF = {
#NFE_AMBIENTE_PRODUCAO: {
#u'servidor'             : u'dec.fazenda.df.gov.br',
#WS_NFE_ENVIO_LOTE         : u'nfe/ServiceRecepcao.asmx',
#WS_NFE_CONSULTA_RECIBO : u'nfe/ServiceRetRecepcao.asmx',
#WS_NFE_CANCELAMENTO     : u'nfe/ServiceCancelamento.asmx',
#WS_NFE_INUTILIZACAO     : u'nfe/ServiceInutilizacao.asmx',
#WS_NFE_CONSULTA         : u'nfe/ServiceConsulta.asmx',
#WS_NFE_SITUACAO         : u'nfe/ServiceStatus.asmx',
#WS_NFE_CONSULTA_CADASTRO: u'nfe/ServiceConsultaCadastro.asmx',
#},
#NFE_AMBIENTE_HOMOLOGACAO: {
#u'servidor'             : u'homolog.nfe.fazenda.df.gov.br',
#WS_NFE_ENVIO_LOTE         : u'nfe/ServiceRecepcao.asmx',
#WS_NFE_CONSULTA_RECIBO : u'nfe/ServiceRetRecepcao.asmx',
#WS_NFE_CANCELAMENTO     : u'nfe/ServiceCancelamento.asmx',
#WS_NFE_INUTILIZACAO     : u'nfe/ServiceInutilizacao.asmx',
#WS_NFE_CONSULTA         : u'nfe/ServiceConsulta.asmx',
#WS_NFE_SITUACAO         : u'nfe/ServiceStatus.asmx',
#WS_NFE_CONSULTA_CADASTRO: u'nfe/ServiceConsultaCadastro.asmx'
#}
#}

UFGO = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.sefaz.go.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe/services/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe/services/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe/services/v2/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfe/services/v2/RecepcaoEvento',
        WS_NFE_INUTILIZACAO     : u'nfe/services/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe/services/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe/services/v2/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe/services/v2/CadConsultaCadastro2?wsdl',
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homolog.sefaz.go.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe/services/v2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe/services/v2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe/services/v2/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfe/services/v2/RecepcaoEvento',
        WS_NFE_INUTILIZACAO     : u'nfe/services/v2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe/services/v2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe/services/v2/NfeStatusServico2',
        }
}

UFMT = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.sefaz.mt.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfews/v2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfews/v2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfews/v2/services/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfews/v2/services/RecepcaoEvento',
        WS_NFE_INUTILIZACAO     : u'nfews/v2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfews/v2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfews/v2/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfews/v2/services/CadConsultaCadastro2?wsdl'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homologacao.sefaz.mt.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfews/v2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfews/v2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfews/v2/services/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfews/v2/services/RecepcaoEvento',
        WS_NFE_INUTILIZACAO     : u'nfews/v2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfews/v2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfews/v2/services/NfeStatusServico2',
        #WS_NFE_CONSULTA_CADASTRO: u'nfews/CadConsultaCadastro'
    }
}

UFMS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe.fazenda.ms.gov.br',
        WS_NFE_ENVIO_LOTE       : u'producao/services2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'producao/services2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'producao/services2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'producao/services2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'producao/services2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'producao/services2/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'producao/services2/CadConsultaCadastro2',
        #        WS_NFE_RECEPCAO_EVENTO  : 'producao/services2/RecepcaoEvento',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : u'homologacao.nfe.ms.gov.br',
        WS_NFE_ENVIO_LOTE       :u'homologacao/services2/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'homologacao/services2/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'homologacao/services2/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'homologacao/services2/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'homologacao/services2/NfeConsulta2',
        WS_NFE_SITUACAO         : u'homologacao/services2/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'homologacao/services2/CadConsultaCadastro2',
        #        WS_NFE_RECEPCAO_EVENTO  : 'homologacao/services2/RecepcaoEvento',
    }
}


'''Sef Minas Gerais - (MG)
Serviço	Versão	URL
NfeRecepcao	2.00	https://nfe.fazenda.mg.gov.br/nfe2/services/NfeRecepcao2
NfeRetRecepcao	2.00	https://nfe.fazenda.mg.gov.br/nfe2/services/NfeRetRecepcao2
NfeInutilizacao	2.00	https://nfe.fazenda.mg.gov.br/nfe2/services/NfeInutilizacao2
NfeConsultaProtocolo	2.00	https://nfe.fazenda.mg.gov.br/nfe2/services/NfeConsulta2
NfeStatusServico	2.00	https://nfe.fazenda.mg.gov.br/nfe2/services/NfeStatus2
NfeConsultaCadastro	2.00	https://nfe.fazenda.mg.gov.br/nfe2/services/cadconsultacadastro2
RecepcaoEvento	2.00	https://nfe.fazenda.mg.gov.br/nfe2/services/RecepcaoEvento
NFeAutorizacao	3.10	https://nfe.fazenda.mg.gov.br/nfe2/services/NfeAutorizacao
NFeRetAutorizacao	3.10	https://nfe.fazenda.mg.gov.br/nfe2/services/NfeRetAutorizacao'''


'''Sef Minas Gerais - (MG)
Serviço	Versão	URL
RecepcaoEvento	1.00	https://hnfe.fazenda.mg.gov.br/nfe2/services/RecepcaoEvento
NfeRecepcao	2.00	https://hnfe.fazenda.mg.gov.br/nfe2/services/NfeRecepcao2
NfeRetRecepcao	2.00	https://hnfe.fazenda.mg.gov.br/nfe2/services/NfeRetRecepcao2
NfeInutilizacao	2.00 / 3.10	https://hnfe.fazenda.mg.gov.br/nfe2/services/NfeInutilizacao2
NfeConsultaProtocolo	2.00 / 3.10	https://hnfe.fazenda.mg.gov.br/nfe2/services/NfeConsulta2
NfeStatusServico	2.00 / 3.10	https://hnfe.fazenda.mg.gov.br/nfe2/services/NfeStatusServico2
NfeConsultaCadastro	2.00 / 3.10	https://hnfe.fazenda.mg.gov.br/nfe2/services/cadconsultacadastro2
NFeAutorizacao	3.10	https://hnfe.fazenda.mg.gov.br/nfe2/services/NfeAutorizacao
NFeRetAutorizacao	3.10	https://hnfe.fazenda.mg.gov.br/nfe2/services/NfeRetAutorizacao'''



UFMG = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'             : u'nfe.fazenda.mg.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe2/services/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfe2/services/RecepcaoEvento',
        WS_NFE_CONSULTA_DESTINATARIO : u'nfe2/services/nfeConsultaDest/nfeConsultaDest.asmx',
        WS_NFE_DOWNLOAD_XML_DESTINATARIO: u'nfe2/services/nfeDownloadNF/nfeDownloadNF.asmx',
        WS_NFE_INUTILIZACAO     : u'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe2/services/NfeStatus2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe2/services/cadconsultacadastro2',
        WS_NFE_AUTORIZACAO: u'nfe2/services/NfeAutorizacao',
        WS_NFE_RET_AUTORIZACAO: u'nfe2/services/NfeRetAutorizacao'
        },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'hnfe.fazenda.mg.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe2/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe2/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe2/services/NfeCancelamento2',
        WS_NFE_EVENTO : u'nfe2/services/RecepcaoEvento',
        WS_NFE_CONSULTA_DESTINATARIO : u'nfe2/services/RecepcaoEvento',
        WS_NFE_DOWNLOAD_XML_DESTINATARIO: u'nfe2/services/nfeDownloadNF/nfeDownloadNF.asmx',
        WS_NFE_INUTILIZACAO     : u'nfe2/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe2/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe2/services/NfeStatus2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe2/services/cadconsultacadastro2',
        WS_NFE_AUTORIZACAO: u'nfe2/services/NfeAutorizacao',
        WS_NFE_RET_AUTORIZACAO: u'nfe2/services/NfeRetAutorizacao'
        }
}

UFPR = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe2.fazenda.pr.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe/NFeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe/NFeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe/NFeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe/NFeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe/NFeConsulta2',
        WS_NFE_SITUACAO         : u'nfe/NFeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe/CadConsultaCadastro2?wsdl',
        #        WS_NFE_RECEPCAO_EVENTO  : 'nfe-evento/NFeRecepcaoEvento',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homologacao.nfe2.fazenda.pr.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe/NFeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe/NFeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe/NFeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe/NFeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe/NFeConsulta2',
        WS_NFE_SITUACAO         : u'nfe/NFeStatusServico2'
    }
}

UFPE = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe.sefaz.pe.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe-service/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe-service/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe-service/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe-service/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe-service/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe-service/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe-service/services/CadConsultaCadastro2',
        #        WS_NFE_RECEPCAO_EVENTO  : 'nfe-service/services/RecepcaoEvento',
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : u'nfehomolog.sefaz.pe.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfe-service/services/NfeRecepcao2',
        WS_NFE_CONSULTA_RECIBO  : u'nfe-service/services/NfeRetRecepcao2',
        WS_NFE_CANCELAMENTO     : u'nfe-service/services/NfeCancelamento2',
        WS_NFE_INUTILIZACAO     : u'nfe-service/services/NfeInutilizacao2',
        WS_NFE_CONSULTA         : u'nfe-service/services/NfeConsulta2',
        WS_NFE_SITUACAO         : u'nfe-service/services/NfeStatusServico2',
        WS_NFE_CONSULTA_CADASTRO: u'nfe-service/services/CadConsultaCadastro2',
        #        WS_NFE_RECEPCAO_EVENTO  : 'nfe-service/services/RecepcaoEvento',
    }
}
# https://sef.sefaz.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro2.asmx

'''Sefaz Rio Grande do Sul - (RS)
Serviço	Versão	URL
RecepcaoEvento	1.00	https://nfe.sefaz.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx
NfeRecepcao	2.00	https://nfe.sefaz.rs.gov.br/ws/Nferecepcao/NFeRecepcao2.asmx
NfeRetRecepcao	2.00	https://nfe.sefaz.rs.gov.br/ws/NfeRetRecepcao/NfeRetRecepcao2.asmx
NfeConsultaCadastro	2.00	https://sef.sefaz.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro2.asmx
NfeConsultaDest	2.00	https://nfe.sefaz.rs.gov.br/ws/nfeConsultaDest/nfeConsultaDest.asmx
NfeDownloadNF	2.00	https://nfe.sefaz.rs.gov.br/ws/nfeDownloadNF/nfeDownloadNF.asmx
NfeInutilizacao	2.00 / 3.10	https://nfe.sefaz.rs.gov.br/ws/NfeInutilizacao/NfeInutilizacao2.asmx
NfeConsultaProtocolo	2.00 / 3.10	https://nfe.sefaz.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx
NfeStatusServico	2.00 / 3.10	https://nfe.sefaz.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx
NFeAutorizacao	3.10	https://nfe.sefaz.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx
NFeRetAutorizacao	3.10	https://nfe.sefaz.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx'''

UFRS = {
    NFE_AMBIENTE_PRODUCAO: {
        'servidor'              : u'nfe.sefaz.rs.gov.br',
        WS_NFE_ENVIO_LOTE       : u'ws/Nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'ws/NfeRetRecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'ws/NfeCancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'ws/nfeinutilizacao/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'ws/NfeConsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : u'ws/NfeStatusServico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'ws/cadconsultacadastro/cadconsultacadastro2.asmx',
        #        WS_NFE_RECEPCAO_EVENTO  : 'ws/recepcaoevento/recepcaoevento.asmx',
        WS_NFE_AUTORIZACAO: u'ws/NfeAutorizacao/NFeAutorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        'servidor'             : u'homologacao.nfe.sefaz.rs.gov.br',
        WS_NFE_ENVIO_LOTE       : u'ws/Nferecepcao/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'ws/NfeRetRecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'ws/NfeCancelamento/NfeCancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'ws/nfeinutilizacao/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'ws/NfeConsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO         : u'ws/NfeStatusServico/NfeStatusServico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'ws/cadconsultacadastro/cadconsultacadastro2.asmx',
        #        WS_NFE_RECEPCAO_EVENTO  : 'ws/recepcaoevento/recepcaoevento.asmx',
        WS_NFE_AUTORIZACAO: u'ws/NfeAutorizacao/NFeAutorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx'
    }
}


'''Sefaz São Paulo - (SP)
Serviço	Versão	URL - PRODUCAO
NfeRecepcao	2.00	https://nfe.fazenda.sp.gov.br/nfeweb/services/nferecepcao2.asmx
NfeRetRecepcao	2.00	https://nfe.fazenda.sp.gov.br/nfeweb/services/nferetrecepcao2.asmx
NfeInutilizacao	2.00	https://nfe.fazenda.sp.gov.br/nfeweb/services/nfeinutilizacao2.asmx
NfeConsultaProtocolo	2.00	https://nfe.fazenda.sp.gov.br/nfeweb/services/nfeconsulta2.asmx
NfeStatusServico	2.00	https://nfe.fazenda.sp.gov.br/nfeweb/services/nfestatusservico2.asmx
NfeConsultaCadastro	2.00	https://nfe.fazenda.sp.gov.br/nfeweb/services/cadconsultacadastro2.asmx
RecepcaoEvento	2.00	https://nfe.fazenda.sp.gov.br/eventosWEB/services/RecepcaoEvento.asmx
NfeInutilizacao	3.10	https://nfe.fazenda.sp.gov.br/ws/nfeinutilizacao2.asmx
NfeConsultaProtocolo	3.10	https://nfe.fazenda.sp.gov.br/ws/nfeconsulta2.asmx
NfeStatusServico	3.10	https://nfe.fazenda.sp.gov.br/ws/nfestatusservico2.asmx
NfeConsultaCadastro	3.10	https://nfe.fazenda.sp.gov.br/ws/cadconsultacadastro2.asmx
RecepcaoEvento	3.10	https://nfe.fazenda.sp.gov.br/ws/recepcaoevento.asmx
NFeAutorizacao	3.10	https://nfe.fazenda.sp.gov.br/ws/nfeautorizacao.asmx
NFeRetAutorizacao	3.10	https://nfe.fazenda.sp.gov.br/ws/nferetautorizacao.asmx'''


'''Sefaz São Paulo - (SP)
Serviço	Versão	URL - Homologacao
NfeConsultaCadastro	2.0	https://homologacao.nfe.fazenda.sp.gov.br/nfeweb/services/cadconsultacadastro2.asmx
NfeRecepcao	2.00	https://homologacao.nfe.fazenda.sp.gov.br/nfeweb/services/NfeRecepcao2.asmx
NfeRetRecepcao	2.00	https://homologacao.nfe.fazenda.sp.gov.br/nfeweb/services/NfeRetRecepcao2.asmx
NfeInutilizacao	2.00	https://homologacao.nfe.fazenda.sp.gov.br/nfeweb/services/nfeinutilizacao2.asmx
NfeConsultaProtocolo	2.00	https://homologacao.nfe.fazenda.sp.gov.br/nfeweb/services/nfeconsulta2.asmx
NfeStatusServico	2.00	https://homologacao.nfe.fazenda.sp.gov.br/nfeweb/services/nfestatusservico2.asmx
RecepcaoEvento	2.00	https://homologacao.nfe.fazenda.sp.gov.br/eventosWEB/services/RecepcaoEvento.asmx
NfeInutilizacao	3.10	https://homologacao.nfe.fazenda.sp.gov.br/ws/nfeinutilizacao2.asmx
NfeConsultaProtocolo	3.10	https://homologacao.nfe.fazenda.sp.gov.br/ws/nfeconsulta2.asmx
NfeStatusServico	3.10	https://homologacao.nfe.fazenda.sp.gov.br/ws/nfestatusservico2.asmx
NfeConsultaCadastro	3.10	https://homologacao.nfe.fazenda.sp.gov.br/ws/cadconsultacadastro2.asmx
RecepcaoEvento	3.10	https://homologacao.nfe.fazenda.sp.gov.br/ws/recepcaoevento.asmx
NFeAutorizacao	3.10	https://homologacao.nfe.fazenda.sp.gov.br/ws/nfeautorizacao.asmx
NFeRetAutorizacao	3.10	https://homologacao.nfe.fazenda.sp.gov.br/ws/nferetautorizacao.asmx'''
UFSP = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'              : u'nfe.fazenda.sp.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfeweb/services/nferecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'nfeweb/services/nferetrecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'nfeweb/services/nfecancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'nfeweb/services/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'nfeweb/services/nfeconsulta2.asmx',
        WS_NFE_SITUACAO         : u'nfeweb/services/nfestatusservico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'nfeweb/services/cadconsultacadastro2.asmx',
        WS_NFE_EVENTO  : u'eventosWEB/services/RecepcaoEvento.asmx',
        WS_NFE_AUTORIZACAO: u'ws/nfeautorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'ws/nferetautorizacao.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'             : u'homologacao.nfe.fazenda.sp.gov.br',
        WS_NFE_ENVIO_LOTE       : u'nfeweb/services/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO  : u'nfeweb/services/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO     : u'nfeweb/services/nfecancelamento2.asmx',
        WS_NFE_INUTILIZACAO     : u'nfeweb/services/nfeinutilizacao2.asmx',
        WS_NFE_CONSULTA         : u'nfeweb/services/nfeconsulta2.asmx',
        WS_NFE_SITUACAO         : u'nfeweb/services/nfestatusservico2.asmx',
        WS_NFE_CONSULTA_CADASTRO: u'nfeweb/services/cadconsultacadastro2.asmx',
        WS_NFE_EVENTO  : u'eventosWEB/services/RecepcaoEvento.asmx',
        WS_NFE_AUTORIZACAO: u'ws/nfeautorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'ws/nferetautorizacao.asmx'
    }
}
'''
Producao
Sefaz Virtual de Contingência Ambiente Nacional - (SVC-AN)
Data: 10-09-2014
RecepcaoEvento	1.00	https://www.svc.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx
NfeRecepcao	2.00	https://www.svc.fazenda.gov.br/NfeRecepcao2/NfeRecepcao2.asmx
NfeRetRecepcao	2.00	https://www.svc.fazenda.gov.br/NfeRetRecepcao2/NfeRetRecepcao2.asmx
NfeConsultaProtocolo	2.00 / 3.10	https://www.svc.fazenda.gov.br/NfeConsulta2/NfeConsulta2.asmx
NfeStatusServico	2.00 / 3.10	https://www.svc.fazenda.gov.br/NfeStatusServico2/NfeStatusServico2.asmx
NFeAutorizacao	3.10	https://www.svc.fazenda.gov.br/NfeAutorizacao/NfeAutorizacao.asmx
NFeRetAutorizacao	3.10	https://www.svc.fazenda.gov.br/NfeRetAutorizacao/NfeRetAutorizacao.asmx

Homologacao
SVC-AN
• https://hom.svc.fazenda.gov.br/NfeRecepcao2/NfeRecepcao2.asmx
• https://hom.svc.fazenda.gov.br/NfeRetRecepcao2/NfeRetRecepcao2.asmx
• https://hom.svc.fazenda.gov.br/NfeInutilizacao2/NfeInutilizacao2.asmx
• https://hom.svc.fazenda.gov.br/NfeConsulta2/NfeConsulta2.asmx
• https://hom.svc.fazenda.gov.br/NfeStatusServico2/NfeStatusServico2.asmx
• https://hom.svc.fazenda.gov.br/RecepcaoEvento/RecepcaoEvento.asmx
NFeAutorizacao	3.10	https://hom.svc.fazenda.gov.br/NfeAutorizacao/NfeAutorizacao.asmx
NFeRetAutorizacao	3.10	https://hom.svc.fazenda.gov.br/NfeRetAutorizacao/NfeRetAutorizacao.asmx
'''


SVC_AN = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'www.svc.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NfeRetRecepcao2/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NfeCancelamento2/NfeCancelamento2.asmx',
        WS_NFE_EVENTO          : u'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_INUTILIZACAO    : u'NFeInutilizacao2/NFeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'NfeConsulta2/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'NFeStatusServico2/NFeStatusServico2.asmx',
        WS_NFE_AUTORIZACAO: u'NfeAutorizacao/NfeAutorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'NfeRetAutorizacao/NfeRetAutorizacao.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'hom.svc.fazenda.gov.br',
        WS_NFE_ENVIO_LOTE      : u'NfeRecepcao2/NfeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'NfeRetRecepcao2/NfeRetRecepcao2.asmx',
        WS_NFE_CANCELAMENTO    : u'NfeCancelamento2/NfeCancelamento2.asmx',
        WS_NFE_EVENTO          : u'RecepcaoEvento/RecepcaoEvento.asmx',
        WS_NFE_INUTILIZACAO    : u'NfeInutilizacao2/NfeInutilizacao2.asmx',
        WS_NFE_CONSULTA        : u'NfeConsulta2/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'NfeStatusServico2/NfeStatusServico2.asmx',
        WS_NFE_AUTORIZACAO: u'NfeAutorizacao/NfeAutorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'NfeRetAutorizacao/NfeRetAutorizacao.asmx'
    }
}


'''
Producao

Sefaz Virtual de Contingência Rio Grande do Sul - (SVC-RS)
Data: 10-09-2014
RecepcaoEvento	1.00	https://nfe.sefazvirtual.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx
NfeRecepcao	2.00	https://nfe.sefazvirtual.rs.gov.br/ws/Nferecepcao/NFeRecepcao2.asmx
NfeRetRecepcao	2.00	https://nfe.sefazvirtual.rs.gov.br/ws/NfeRetRecepcao/NfeRetRecepcao2.asmx
NfeConsultaProtocolo	2.00 / 3.10	https://nfe.sefazvirtual.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx
NfeStatusServico	2.00 / 3.10	https://nfe.sefazvirtual.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx
NFeAutorizacao	3.10	https://nfe.sefazvirtual.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx
NFeRetAutorizacao	3.10	https://nfe.sefazvirtual.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx

Homologacao
SVC-RS (mesmos endereços da SVRS)
• https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/Nferecepcao/NFeRecepcao2.asmx
• https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/NfeRetRecepcao/NfeRetRecepcao2.asmx
• https://homologacao.nfe.sefaz.rs.gov.br/ws/recepcaoevento/recepcaoevento.asmx
• https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/NfeConsulta/NfeConsulta2.asmx
• https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/NfeStatusServico/NfeStatusServico2.asmx
NFeAutorizacao	3.10	https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao.asmx
NFeRetAutorizacao	3.10	https://homologacao.nfe.sefazvirtual.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx

'''


SVC_RS = {
    NFE_AMBIENTE_PRODUCAO: {
        u'servidor'            : u'nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE      : u'ws/Nferecepcao/NFeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'ws/NfeRetRecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_EVENTO          : u'ws/recepcaoevento/recepcaoevento.asmx',
        WS_NFE_CONSULTA        : u'ws/NfeConsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'ws/NfeStatusServico/NfeStatusServico2.asmx',
        WS_NFE_AUTORIZACAO: u'ws/NfeAutorizacao/NFeAutorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx'
    },
    NFE_AMBIENTE_HOMOLOGACAO: {
        u'servidor'            : u'homologacao.nfe.sefazvirtual.rs.gov.br',
        WS_NFE_ENVIO_LOTE      : u'ws/Nferecepcao/NFeRecepcao2.asmx',
        WS_NFE_CONSULTA_RECIBO : u'ws/NfeRetRecepcao/NfeRetRecepcao2.asmx',
        WS_NFE_EVENTO          : u'ws/recepcaoevento/recepcaoevento.asmx',
        WS_NFE_CONSULTA        : u'ws/NfeConsulta/NfeConsulta2.asmx',
        WS_NFE_SITUACAO        : u'ws/NfeStatusServico/NfeStatusServico2.asmx',
        WS_NFE_AUTORIZACAO: u'ws/NfeAutorizacao/NFeAutorizacao.asmx',
        WS_NFE_RET_AUTORIZACAO: u'ws/NfeRetAutorizacao/NFeRetAutorizacao.asmx'
    }
}


ESTADO_WS = {
    u'AC': SVRS,
    u'AL': SVRS,
    u'AM': UFAM,
    u'AP': SVRS,
    u'BA': UFBA,
    u'CE': UFCE,
    u'DF': SVRS,
    u'ES': SVAN,
    u'GO': UFGO,
    u'MA': SVAN,
    u'MG': UFMG,
    u'MS': SVRS,
    u'MT': UFMT,
    u'PA': SVAN,
    u'PB': SVRS,
    u'PE': UFPE,
    u'PI': SVAN,
    u'PR': UFPR,
    u'RJ': SVRS,
    u'RN': SVAN,
    u'RO': SVRS,
    u'RR': SVRS,
    u'RS': UFRS,
    u'SC': SVRS,
    u'SE': SVRS,
    u'SP': UFSP,
    u'TO': SVRS
}
