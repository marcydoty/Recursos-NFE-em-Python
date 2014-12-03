from setuptools import setup, find_packages
import os

setup(
    name="python-nfe",
    version="3.8",
    include_package_data=True,
    author="Marcilene Ribeiro",
    author_email="marcilene@sigsolucoes.net.br",
    description=("Biblioteca para implementacao de notas fiscais eletronicas"),
    license="LGPLv2.1",
    keywords="NF-e",
    url="http://github.com/marcydoty",
    packages=find_packages(),
    classifiers=["Development Status :: 1.0",
                 "Topic :: NFe",
                 "License :: LGPL", ],
    package_dir={'nfe': 'nfe'},
    package_data={'nfe': ['pysped/relato_sped/fonts/*', 'pysped/nfe/danfe/fonts/*'],
                  'nfe.pysped.nfe.manual_401': [os.path.join('schema', 'pl_006j', '*'),
                                                os.path.join('schema', 'pl_006r', '*'),
                                                os.path.join('schema', 'pl_006s', '*')],
                  'nfe.pysped.nfe.manual_500': [os.path.join('schema', 'pl_008e', '*')],
                  'nfe.pysped.xml_sped': [os.path.join('schema', '*'),
                                          os.path.join('cadeia-certificadora', 'README'),
                                          os.path.join('cadeia-certificadora', 'certificados', '*')],
                  'nfe.pysped.nfe.manifestacao_destinatario': [os.path.join('schema', 'pl', '*')]

    }
)
