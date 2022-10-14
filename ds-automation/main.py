import yaml
import nbformat

import inputs
import cell_creation
import stats_descriptions
import graphical_descriptions as gpd

#### Reading the yaml config.
with open("config.yaml", "r") as yaml_config:
    config = yaml.load(yaml_config, Loader=yaml.FullLoader)

nb = nbformat.v4.new_notebook()

#### This list holds all the cells returned from various functions.
nb_cells = []

#### install libraries
nb_cells.append(cell_creation.code_cell("!pip install pandas seaborn"))

#### import libraries
nb_cells.append(cell_creation.code_cell("import pandas as pd"))
nb_cells.append(cell_creation.code_cell("import seaborn as sns"))

#### Block for reading in the data
nb_cells.extend(inputs.read_csv_to_dataframe(config=config))

#### Block for statistical descriptions
nb_cells.extend(stats_descriptions.statistical_desciptions(config=config))

#### Blocks for graphical descriptions
nb_cells.extend(gpd.graphical_descriptions(config=config))

nb["cells"] = nb_cells

nbformat.write(nb, f"{config['Name']}.ipynb")
