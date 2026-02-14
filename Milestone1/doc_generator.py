
def generate_docstring(function):
    name = function["name"]
    params = function["parameters"]

    doc = f'    """\n'
    doc += f"    Auto-generated documentation for `{name}` function.\n\n"

    if params:
        doc += "    Parameters:\n"
        for p in params:
            doc += f"        {p} : Description of {p}\n"

    doc += "\n    Returns:\n"
    doc += "        Description of return value\n"
    doc += '    """\n'

    return doc
