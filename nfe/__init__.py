import nfe
import geraldo

__version__ = 3.7
__license__ = 'GNU Lesser General Public License (LGPL)'
__url__ = 'http://github.com/marcydoty/Recursos-NFE-em-Python'

if not geraldo.__version__=='0.4.10-stable_sig':
    raise  Exception('A versao do geraldo deve ser igual a 0.4.10-stable_sig')