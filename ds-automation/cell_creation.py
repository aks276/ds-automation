import nbformat


def code_cell(code: str):
    return nbformat.v4.new_code_cell(code)


def md_cell(md: str):
    return nbformat.v4.new_markdown_cell(md)
