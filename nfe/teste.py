# -*- coding: utf-8 -*-


from nfe.nf_e import *
from lxml import etree
from OpenSSL import crypto



'''************************TESTES*****************************'''

#n=nf_e()


###*******************************teste extrair certificado A1***************************
#
#cert1=u'/home/marcilene/Aptana Studio 3 Workspace/certificado.pfx'
#pwd1=u'123'
#a= n.extrair_certificado_a1(cert1,pwd1)
#cert=a['cert']
#key=a['key']

#***************************************************************************************


#***************************teste consulta servidor*********************************

#retorno=n.consultar_servidor(cert,key)
#print 'retorno xml',retorno


##*****************************teste validar,assinar,enviar**************************
#
#xml=u'/home/marcilene/Aptana Studio 3 Workspace/nfe_a1/naoassinada/31110301526558000178550010000002361000002363-nfe.xml'
#raiz = etree.parse(xml)
#xml=etree.tostring(raiz,pretty_print=True)
#
#print n.processar_nfe(xml,cert,pwd)
#print 'processou'

##*****************************teste validar,assinar e enviar lote********************

#lista=[]
#xml=u'/home/marcilene/Aptana Studio 3 Workspace/removidos_nfe/naoassinada/31110301526558000178550010000002381000002384-nfe.xml'
#for xml in caminhos:
#raiz = etree.parse(xml)
#xml=etree.tostring(raiz,pretty_print=True)
#    lista.append(xml)

#print 'lista',lista
#n.processar_nfe(xml,cert,key)

#print 'processou o lote'

##*****************************teste cancelamento*************************************
#
#ch=u'31110301526558000178550010000002341289546081'
#prot=u'131110024593073'
#just=u'Somente um teste de cancelamento'
#    
#print n.cancelar_nota(ch,prot,just,cert,pwd)



##*****************************teste inutilizacao*************************************
#
#cnpj=u'01526558000178'
#serie=u'1'
#num=27
#just=u'Testando a inutilização de NF-e'
#   
#print n.inutilizar_nota(cnpj,serie,num,just,cert,pwd)

##*****************************teste faixa numeracao**********************************
#
#cnpj=u'01526558000178'
#serie=u'1'
#ini=22
#fim=25
#just=u'Testando a inutilização de NF-e'
#print n.inutilizar_faixa_numeracao(cnpj,serie,ini,fim,just,cert,pwd)











