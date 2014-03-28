
from setuptools import setup, find_packages
setup(
	name = "python-nfe",
	version = "1.06",
	include_package_data=True,
	author = "Marcilene Ribeiro",
	author_email = "marcilene@sigsolucoes.net.br",
	description = ("Biblioteca para implementacao de notas fiscais eletronicas"),
	license = "LGPL",
	keywords = "NF-e",
	url = "http://github.com/marcydoty",
	packages = find_packages(),
	classifiers = ["Development Status :: 1.0",
	"Topic :: NFe",
	"License :: LGPL",],
    package_dir={'nfe': 'nfe'},
    package_data={'nfe': ['pysped/relato_sped/fonts/*','pysped/nfe/danfe/fonts/*']},

)
