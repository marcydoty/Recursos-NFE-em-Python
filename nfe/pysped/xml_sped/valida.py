# -*- coding: utf-8 -*-

from lxml import etree
import os
DIRNAME = os.path.dirname(__file__)
#Realizando a validacao e salvando o erro em um arquivo de log... usado somente no caso do openerp
xml = open('/tmp/xml.txt', 'r').read()
arquivo_esquema = open('/tmp/arquivo_esquema.txt', 'r').read()
esquema = etree.XMLSchema(etree.parse(arquivo_esquema))
if not esquema.validate(etree.fromstring(xml)):
    msg = esquema.error_log.last_error
    open('/tmp/erro_log_nfe.txt', 'wb').write(str(msg))
