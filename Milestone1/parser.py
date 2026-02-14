
import ast

def extract_functions(code: str):
    tree = ast.parse(code)
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            parameters = [arg.arg for arg in node.args.args]

            functions.append({
                "name": function_name,
                "parameters": parameters
            })

    return functions
