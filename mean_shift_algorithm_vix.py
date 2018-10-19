import numpy as np
import pandas as pd
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
from itertools import cycle


def main(filename,b):

    df = pd.read_csv(filename)
    grouped_data = df.dropna()
    grouped_data = grouped_data[1:]
    grouped_data=grouped_data[['Date', 'Close']][1:]
    sell_data = grouped_data.as_matrix(columns=['Close'])
    ms = MeanShift(bandwidth=b, bin_seeding=True)
    ms.fit(sell_data)
    ml_resultsmin = []
    ml_resultsmax = []
    for k in range(len(np.unique(ms.labels_))):
        my_members = ms.labels_ == k
        values = sell_data[my_members, 0]
        ml_resultsmin.append(min(values))
        ml_resultsmax.append(max(values))

    print ml_resultsmin
    print ml_resultsmax
    print ms.labels_

    labels = ms.labels_
    cluster_centers = ms.cluster_centers_
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    print("number of estimated clusters : %d" % n_clusters_)
    print np.array(cluster_centers)
    plt.plot( sell_data, color='#52a0d8', linewidth=.7)
    for i in xrange(0,n_clusters_):
        plt.axhline(cluster_centers[i], color='k', linestyle='dashed', linewidth=1)
        #plt.axhline(ml_resultsmax[i], color='g', linestyle='dashed', linewidth=1)
        #plt.axhline(ml_resultsmin[i], color='r', linestyle='dashed', linewidth=1)

    plt.title(' VIX Mean Shift Algorithm - Estimated Number of Clusters: %d' % n_clusters_)
    plt.yticks(np.arange(0, 80, step=2))
    plt.show()

main('data/VIXVXO.csv',2) #scan data with a kde bandwidth parameter of 2
