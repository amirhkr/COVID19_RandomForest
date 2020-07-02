import os
from pathlib import Path

# Latest file name - update when you update your data
LATEST = 'v0.2.0_2020-07-02'

# Paths
HOME      = Path(f'{os.getcwd()}/../../')
SRC       = HOME/'src'
DATA      = HOME/'data'
DEID      = DATA/'data_deidentified'
CURRENT   = DEID/LATEST
PROCESSED = DATA/'processed'