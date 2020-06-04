from utils.processing import *


#---
# Pipeline 1 - first thoughts
#---

# Example - configure entire experiment with JSON
cf1 = {
    'numerical':{
        'normalise':True
    },
    'binary':{
        'normalise':True
    },
    'categorical':{
        'normalise':True
    },
    'ml':{
        'models':['knn','rf','nb']
    },
    'explainability':{
        'models':['shap', 'pca', 'saliency'],
        'params':[
            'shap':{'alpha':0.1}
        ],
    }
}


def compile_pipeline(config):
    """TO DO: Construct processing and/or modelling pipeline from JSON config.
    """
    return None


pipe1 = compile_pipeline(cf1)