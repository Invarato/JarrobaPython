# Artículo relaccionado con la web de www.Jarroba.com
El código de esta carpeta forma parte del artículo https://jarroba.com/vistas-de-los-diccionarios-de-python-keys-values-e-items/


## Nota sobre las versiones de Python
En estos ejemplos se utiliza la última versión.

Para compatibilidad hay que usar para la **versión de Python:**
* **\>= 3.3:** Heredar de `from collections import abc`, ejemplo:
```
from collections import abc

class MiColeccion(abc.Collection):
    # ...
```
* **< 3.3:** Heredar de `import collections`, ejemplo:
```
import collections

class MiColeccion(collections.Collection):
    # ...
```
