import cell_creation


def graphical_descriptions(config: dict):
    if 'visualizations' not in config:
        raise ValueError("'visualizations' key not found in config")
    
    cells = []

    vis = config["visualizations"]

    ### The correlation matrix
    cells.append(cell_creation.md_cell("#### The co-relation matrix"))
    cells.append(cell_creation.code_cell(f"{vis}.corr()"))
    cells.append(
        cell_creation.code_cell(f"sns.heatmap({vis}.corr, annot=True)\nplt.show()")
    )

    return cells
