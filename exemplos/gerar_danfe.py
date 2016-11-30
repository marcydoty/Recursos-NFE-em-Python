# -*- coding: utf-8 -*-

import os, sys

sys.path.insert(0, os.path.abspath(".."))

from nfe.nf_e import nf_e

if __name__ == '__main__':
    nova_nfe = nf_e()
    
    ##Gerar danfe a partir de uma NFe ja processada
    f = open("procNFe_Exemplo_DANFE.xml", encoding='utf8')
    nfe_str = f.read()
    f.close()
    
    danfe = nova_nfe.gerar_danfe(nfe_str, versao='2.00')
    
    with open("DANFE_Exemplo.pdf", 'wb') as f:
        f.write(danfe)