# Last Unique String Finder

## Descripción

`Last Unique String Finder` es una utilidad en Python que utiliza **sets** para identificar la **última** cadena única en una lista de cadenas.  
- Si todas se repiten → devuelve `""`.  
- Si la lista está vacía → devuelve `""`.  

## Reglas del ejercicio

1. **Entrada:**  
   - Una lista de cadenas (`list[str]`), p. ej. `['apple', 'banana', 'apple', 'mango', 'banana']`.  
   - Puede contener cualquier palabra, repetida o no.  
   - Puede ser una lista vacía.

2. **Salida:**  
   - La **última** cadena que aparece **exactamente una vez** en toda la lista.  
   - Si no hay ninguna o la lista está vacía, devuelve `""`.

3. **Cómo se determina “última única”:**  
   - “Única” = aparece **una sola vez** en toda la lista.  
   - “Última” = de esas únicas, la que tiene el índice más alto (más a la derecha).

## Ejemplos

| Entrada                                              | Salida     |
|------------------------------------------------------|------------|
| `['apple','banana','apple','mango','banana']`        | `"mango"`  |
| `['hello','world','hello']`                          | `"world"`  |
| `['hello','world','hello','world']`                  | `""`       |
| `[]`                                                 | `""`       |

## Uso
```
from finder import find_unique_string

fruits = ['apple','banana','apple','mango','banana']
print(find_unique_string(fruits))  # ➞ 'mango'

```

## Tests

- **Básico:**
  ```bash
  python -m unittest discover
  ```

- **Verbose (más información de cada prueba):**
  ```bash
  python -m unittest discover -v
  ```

## Contribuciones

1. Haz un _fork_ de este repositorio.  
2. Crea una rama (`git checkout -b mejora-feature`).  
3. Realiza tus cambios y haz _commit_ (`git commit -am "Agrega nueva función"`).  
4. Empuja la rama (`git push origin mejora-feature`).  
5. Abre un _Pull Request_.

## Licencia

MIT License – consulta el archivo [LICENSE](LICENSE) para más detalles.
