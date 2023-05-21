def defangIPaddr(self, address: str) -> str:
    out = str()
    for char in address:
        if char == ".":
            out += "[.]"
        else:
            out += char
    return out # address.replace(".", "[.]") would work too but cmon