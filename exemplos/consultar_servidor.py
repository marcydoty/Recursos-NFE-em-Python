# -*- coding: utf-8 -*-

import os, sys

sys.path.insert(0, os.path.abspath(".."))

from nfe.nf_e import nf_e

if __name__ == '__main__':
    nova_nfe = nf_e()
    
    #Associacao.pfx nao e valido, utilize um certificado valido
    caminho_certificado = "certificado/Associacao.pfx"
    with open(caminho_certificado, 'rb') as f:
        arquivo = f.read()
    
    info_certificado = nova_nfe.extrair_certificado_a1(arquivo, "associacao")

    resultado = nova_nfe.consultar_servidor(cert=info_certificado['cert'], key=info_certificado['key'], versao=u'2.00', ambiente=2, estado=u'MG', tipo_contingencia=False)
    print 'Status: '+str(resultado['status'])
    print 'Razao: '+str(resultado['reason'])