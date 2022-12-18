import modulos
from ..mod2.modulo2 import modulo2 ##ruta relativa
import sys 
sys.path.insert(1, 'C:path/etc') ## ruta completa

modulos.saludo("Paola")
modulo2.traeEdad("27")
