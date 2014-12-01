# -*- coding: utf-8 -*-


ESQUEMA_ATUAL = u'pl_008e'


#
# Envelopes SOAP
#
from soap_310 import SOAPEnvio as SOAPEnvio_310
from soap_310 import SOAPRetorno as SOAPRetorno_310

#
# Emissão de NF-e 3.10
#
from nfe_310 import NFe as NFe_310
from nfe_310 import NFRef as NFRef_310
from nfe_310 import Det as Det_310
from nfe_310 import DI as DI_310
from nfe_310 import Adi as Adi_310
from nfe_310 import Med as Med_310
from nfe_310 import Arma as Arma_310
from nfe_310 import Reboque as Reboque_310
from nfe_310 import Vol as Vol_310
from nfe_310 import Lacres as Lacres_310
from nfe_310 import Dup as Dup_310
from nfe_310 import ObsCont as ObsCont_310
from nfe_310 import ObsFisco as ObsFisco_310
from nfe_310 import ProcRef as ProcRef_310

#
# Envio de lote de NF-e
#
from envinfe_310 import EnviNFe as EnviNFe_310
from envinfe_310 import RetEnviNFe as RetEnviNFe_310

#
# Consulta do recibo do lote de NF-e
#
from consrecinfe_310 import ConsReciNFe as ConsReciNFe_310
from consrecinfe_310 import RetConsReciNFe as RetConsReciNFe_310
from consrecinfe_310 import ProtNFe as ProtNFe_310
from consrecinfe_310 import ProcNFe as ProcNFe_310

#
# Cancelamento de NF-e
#
from cancnfe_310 import CancNFe as CancNFe_310
from cancnfe_310 import RetCancNFe as RetCancNFe_310
from cancnfe_310 import ProcCancNFe as ProcCancNFe_310

#
# Cancelamento de NF-e por EVENTO

from cancnfe_evento import EnvEvento as EnvEvento_310
from cancnfe_evento import RetEnvEvento as RetEnvEvento_310
from cancnfe_evento import ProcEventoNFe as ProcEventoNFe_310

#
# Carta de Correção

from carta_correcao import EnvEvento as EnvEventoCCe_310
from carta_correcao import RetEnvEvento as RetEnvEventoCCe_310
from carta_correcao import ProcEventoNFe as ProcEventoNFeCCe_310

#
# Inutilização de NF-e
#
from inutnfe_310 import InutNFe as InutNFe_310
from inutnfe_310 import RetInutNFe as RetInutNFe_310
from inutnfe_310 import ProcInutNFe as ProcInutNFe_310

#
# Consulta a situação de NF-e
#
from conssitnfe_310 import ConsSitNFe as ConsSitNFe_310
from conssitnfe_310 import RetConsSitNFe as RetConsSitNFe_310

#
# Consulta a situação do serviço
#
from consstatserv_310 import ConsStatServ as ConsStatServ_310
from consstatserv_310 import RetConsStatServ as RetConsStatServ_310

#
# Consulta cadastro

from conscad_310 import ConsCad as ConsCad_310
from conscad_310 import RetConsCad as RetConsCad_310

