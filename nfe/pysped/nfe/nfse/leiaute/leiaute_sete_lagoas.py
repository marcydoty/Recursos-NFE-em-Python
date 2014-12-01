# -*- coding: utf-8 -*-
__author__ = 'marcilene.ribeiro'

from nfe.pysped.xml_sped import *

import os

DIRNAME = os.path.dirname(__file__)

ABERTURA_CIDADE = u'<?xml version="1.0" encoding="iso-8859-1"?>'

class CodServico(XMLNFe):
    def __init__(self):
        super(CodServico, self).__init__()
        self.codservico = TagCaracter(nome=u'codservico', codigo=u'', tamanho=[1, 15], raiz=u'/codservico')
        self.basecalculo = TagDecimal(nome=u'basecalculo', codigo=u'', tamanho=[1, 15, 1], decimais=[0, 2, 2], raiz=u'//codservico')
        self.issretido = TagDecimal(nome=u'issretido', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//codservico')
        self.discriminacao = TagCaracter(nome=u'discriminacao', codigo=u'', tamanho=[1, 400], raiz=u'//codservico')

    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += u'<codservico>'
        xml += self.codservico.xml
        xml += self.basecalculo.xml
        xml += self.issretido.xml
        xml += self.discriminacao.xml
        xml += u'</codservico>'
        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.codservico.xml = arquivo
            self.basecalculo.xml = arquivo
            self.issretido.xml = arquivo
            self.discriminacao.xml = arquivo

    xml = property(get_xml, set_xml)


class  Importacao(XMLNFe):
    def __init__(self):
        super(Importacao, self).__init__()
        self.rps_numero = TagCaracter(nome=u'rps_numero', codigo=u'',  tamanho=[0, 20], raiz=u'//importacao')#, obrigatorio=False)
        self.rps_data = TagData(nome=u'rps_data', codigo=u'', raiz=u'//importacao/nota')#, obrigatorio=False)
        self.tomador_nome = TagCaracter(nome=u'tomador_nome', codigo=u'', tamanho=[0, 100], raiz=u'//importacao/nota')
        self.tomador_cnpjcpf = TagCaracter(nome=u'tomador_cnpjcpf', codigo=u'', tamanho=[13, 18], raiz=u'//importacao/nota')
        self.tomador_inscrmunicipal = TagCaracter(nome=u'tomador_inscrmunicipal', codigo=u'', tamanho=[0, 20], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.tomador_logradouro = TagCaracter(nome=u'tomador_logradouro', codigo=u'', tamanho=[0, 40], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.tomador_numero = TagInteiro(nome=u'tomador_numero', codigo=u'', tamanho=[1, 5], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.tomador_complemento = TagCaracter(nome=u'tomador_complemento', codigo=u'', tamanho=[1, 10], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.tomador_bairro = TagCaracter(nome=u'tomador_bairro', codigo=u'', tamanho=[1, 15], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.tomador_cep = TagCaracter(nome=u'tomador_cep', codigo=u'', tamanho=[1, 12], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.tomador_municipio = TagCaracter(nome=u'tomador_municipio', codigo=u'', tamanho=[1, 100], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.tomador_uf = TagCaracter(nome=u'tomador_uf', codigo=u'', tamanho=[0, 3], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.tomador_email = TagCaracter(nome=u'tomador_email', codigo=u'', tamanho=[1, 100], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.discriminacao = TagCaracter(nome=u'discriminacao', codigo=u'', tamanho=[1, 400], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.observacao = TagCaracter(nome=u'observacao', codigo=u'', tamanho=[1, 300], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.deducaoirrf = TagDecimal(nome=u'deducaoirrf', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.cofins = TagDecimal(nome=u'cofins', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.pispasep = TagDecimal(nome=u'pispasep', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.contribuicaosocial = TagDecimal(nome=u'contribuicaosocial', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.irrf = TagDecimal(nome=u'irrf', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.totalretencoes = TagDecimal(nome=u'totalretencoes', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.valortotal = TagDecimal(nome=u'valortotal', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.valordeducoes = TagDecimal(nome=u'valordeducoes', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.basecalculo = TagDecimal(nome=u'basecalculo', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.valoriss = TagDecimal(nome=u'valoriss', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.issretido = TagDecimal(nome=u'issretido', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.credito = TagDecimal(nome=u'credito', codigo=u'', tamanho=[1, 10, 1], decimais=[0, 2, 2], raiz=u'//importacao/nota')#, obrigatorio=False)
        self.estado = TagCaracter(nome=u'estado', codigo=u'', tamanho=[1, 20], raiz=u'//importacao/nota')
        self.codservico = []
            # CodServico()


    def get_xml(self):
        xml = XMLNFe.get_xml(self)
        xml += ABERTURA_CIDADE
        xml += u'<importacao>'
        xml += u'<nota>'

        xml += self.rps_numero.xml
        xml += self.rps_data.xml
        xml += self.tomador_nome.xml
        xml += self.tomador_cnpjcpf.xml
        xml += self.tomador_inscrmunicipal.xml
        xml += self.tomador_logradouro.xml
        xml += self.tomador_numero.xml
        xml += self.tomador_complemento.xml
        xml += self.tomador_bairro.xml
        xml += self.tomador_cep.xml
        xml += self.tomador_municipio.xml
        xml += self.tomador_uf.xml
        xml += self.tomador_email.xml
        xml += self.discriminacao.xml
        xml += self.observacao.xml
        xml += self.deducaoirrf.xml
        xml += self.cofins.xml
        xml += self.pispasep.xml
        xml += self.contribuicaosocial.xml
        xml += self.irrf.xml
        xml += self.totalretencoes.xml
        xml += self.valortotal.xml
        xml += self.valordeducoes.xml
        xml += self.basecalculo.xml
        xml += self.valoriss.xml
        xml += self.issretido.xml
        xml += self.credito.xml
        xml += self.estado.xml
        for d in self.codservico:
            xml += d.xml

        xml += u'</nota>'
        xml += u'</importacao>'

        return xml

    def set_xml(self, arquivo):
        if self._le_xml(arquivo):
            self.rps_numero.xml = arquivo
            self.rps_data.xml = arquivo
            self.tomador_nome.xml = arquivo
            self.tomador_cnpjcpf.xml = arquivo
            self.tomador_inscrmunicipal.xml = arquivo
            self.tomador_logradouro.xml = arquivo
            self.tomador_numero.xml = arquivo
            self.tomador_complemento.xml = arquivo
            self.tomador_bairro.xml = arquivo
            self.tomador_cep.xml = arquivo
            self.tomador_municipio.xml = arquivo
            self.tomador_uf.xml = arquivo
            self.tomador_email.xml = arquivo
            self.discriminacao.xml = arquivo
            self.observacao.xml = arquivo
            self.deducaoirrf.xml = arquivo
            self.cofins.xml = arquivo
            self.pispasep.xml = arquivo
            self.contribuicaosocial.xml = arquivo
            self.irrf.xml = arquivo
            self.totalretencoes.xml = arquivo
            self.valortotal.xml = arquivo
            self.valordeducoes.xml = arquivo
            self.basecalculo.xml = arquivo
            self.valoriss.xml = arquivo
            self.issretido.xml = arquivo
            self.credito.xml = arquivo
            self.estado.xml = arquivo
            # self.codservico.xml = arquivo
            self.ret = self.le_grupo('//importacao/nota/codservico', CodServico)

    xml = property(get_xml, set_xml)




