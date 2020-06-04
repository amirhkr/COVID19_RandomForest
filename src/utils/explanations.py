# Feature Explanation Utils
#
# Utils to explain data and models. Both supervised and unsupervised explainability techniques.
#
# Authors: Athon Millane, 2020
#
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

from umap import UMAP
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA, KernelPCA, SparsePCA
import warnings
warnings.filterwarnings('ignore')
CPU = True


if CPU:
    def t(df):
        r = df.astype(np.float32).values
        if r.shape[1] == 1:
            r = r.reshape(-1, )
        return r
    def f(res):
        return pd.DataFrame(res)
else:
    def t(df):
        return df
    
    
def get_pc(df, pca_algo=PCA, dim=2):
    df_out = pd.Series(df.columns).to_frame('feature')
    for i in range(dim):
        df_out[f'pc_{i}'] = pca_algo(n_components=dim).fit(t(df)).components_[i]
        df_out[f'pc_{i}_abs'] = df_out[f'pc_{i}'].apply(np.abs)
    
    return df_out


def pca_explain(df, pca_algo=PCA, dim=2):
    return pca_algo(n_components=dim).fit(t(df)).components_
#     return f(pca_algo(n_components=dim).fit_transform(t(df))).set_index(df.index)