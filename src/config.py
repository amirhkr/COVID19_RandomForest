import os
from pathlib import Path

# Latest file name - update when you update your data
LATEST = 'v0.1.0_2020-05-25'

# Paths
HOME      = Path(f'{os.getcwd()}/../../')
SRC       = HOME/'src'
DATA      = HOME/'data'
DEID      = DATA/'data_deidentified'
CURRENT   = DEID/LATEST
PROCESSED = DATA/'processed'