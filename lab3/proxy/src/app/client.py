def request_ingredient(source, name: str) -> None:
    result = source.get(name)
    if result is None:
        print(f"Cliente: '{name}' no existe\n")
    else:
        print(f"Cliente: obtuve '{result}'\n")
