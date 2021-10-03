import pandas as pd
import numpy as np
import os

# import seaborn as sns
# import matplotlib.pyplot as plt
# %matplotlib inline
# plt.style.use('ggplot')

def alzheimer_clusterPlot():
    dataset = pd.read_csv(os.getcwd() + "\\app\\datasets\\alzheimer.csv")
    dataset = dataset[dataset['Group'].str.contains('Demented')]

    dataset = dataset.dropna()
    dataset.drop('Group',axis=1,inplace=True)
    dataset = dataset[['MMSE','eTIV','nWBV']].values

    from sklearn.cluster import KMeans
    model = KMeans(n_clusters = 3, init = "k-means++", max_iter = 300, n_init = 10, random_state = 0)
    y_clusters = model.fit_predict(dataset)

    # from mpl_toolkits.mplot3d import Axes3D
    import plotly.graph_objs as go
    # from plotly import tools
    # from plotly.subplots import make_subplots
    # import plotly.offline as py
    # 3d scatterplot using plotly
    Scene = dict(xaxis = dict(title  = 'eTIV'),yaxis = dict(title  = 'nWBV'),zaxis = dict(title  = 'ASF'))

    # model.labels_ is nothing but the predicted clusters i.e y_clusters
    labels = model.labels_
    trace = go.Scatter3d(x=dataset[:, 0], y=dataset[:, 1], z=dataset[:, 2], mode='markers',marker=dict(color = labels, size= 10, line=dict(color= 'blue',width = 1)))
    layout = go.Layout(margin=dict(l=0,r=0),scene = Scene,height = 1000,width = 1000)
    data = [trace]
    fig = go.Figure(data = data, layout = layout)
    # fig.show()
    # print("number of cluster found: {}".format(len(set(model.labels_))))
    # print('cluster for each point: ', model.labels_)

    return fig