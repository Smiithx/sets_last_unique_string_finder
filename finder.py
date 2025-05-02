def find_unique_string(words: list[str]) -> str:
    """
    Devuelve la última cadena que aparece exactamente una vez en 'words'.
    Si no hay ninguna única o la lista está vacía, devuelve "".
    Implementación basada en sets para tracking de vistos y repetidos.
    """
    # 1. Tipo de retorno correcto para lista vacía
    if not words:
        return ''
    seen, repeated = set(), set()

    # 2. Construir sets de vistos y repetidos
    for word in words:
        if word in seen:
            repeated.add(word)
        else:
            seen.add(word)

    # 3. Recorrer en reversa para respetar orden original
    for word in reversed(words):
        if word not in repeated:
            return word

    return ''
