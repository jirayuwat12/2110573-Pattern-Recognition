from asyncore import loop
import pandas as pd
import numpy as np
from tqdm import tqdm

class KNN():
    def __init__(self,
                 mode='mean'):
        '''
        K nearest neighbor 
        '''
        self.mode=mode

    def fit(self,
            df=None,
            k=None,
            centriods=None,
            inplace=False,
            max_iter=1000,
            explain=False):
        '''
        fit KNN with `k` group
        '''
        if not inplace:
            df = df.copy()
        df['label'] = None

        # initialization
        if not centriods:
            centriods = df.sample(k).iloc[:, :-1].to_numpy().astype(float)
        elif len(centriods) != k:
            raise ValueError('Invalid centriod\'s shape')
        if explain:
            print(f"Init centriod : {centriods}")

        # loop until done
        looper = tqdm(range(max_iter), desc=f'Fitting KNN for k={k}') \
            if not explain else range(max_iter)
        for iter in looper:
            # assign
            if explain:
                print(f"Assign #{iter+1}")
            for row_idx in range(df.shape[0]):
                data_point = df.iloc[row_idx, :-1].to_numpy()
                min_dist = float('inf')
                centriod_idx = 0
                for idx, centriod in enumerate(centriods):
                    dist = self.distance(centriod, data_point)
                    if dist < min_dist:
                        min_dist = dist
                        centriod_idx = idx
                if df.iloc[row_idx, -1] != centriod_idx and explain:
                    print(f"row #{row_idx} is change from group {df.iloc[row_idx, -1]} to {centriod_idx}")
                df.iloc[row_idx, -1] = centriod_idx
            if explain:
                print(df)

            # update
            change = False
            if explain:
                print(f"Update #{iter+1}")
            for centriod_idx in range(k):
                new_centriod = self.mean_point(df[df['label']==centriod_idx])
                dist = self.distance(centriods[centriod_idx], new_centriod)
                if not explain:
                    looper.set_postfix({'centriod_move':dist})
                if dist > 1e-9:
                    change = True
                if explain:
                    print(f"for centriod #{centriod_idx} change from {centriods[centriod_idx]} to {new_centriod} which diff {dist} units")
                centriods[centriod_idx] = new_centriod
            if explain:
                print(df)

            # break condition
            if not change:
                looper.set_description_str(f'Fitting KNN for k={k} done at #{iter+1}')
                break

        return df

    def mean_point(self, df):
        '''
        calculate centriod of given data point
        '''
        df = df.copy()
        data_point = df.iloc[:, :-1].to_numpy()
        mean = data_point.mean(axis=0)
        return mean


    def distance(self, x1, x2):
        '''
        calculate by Euclidean distance
        '''
        return np.sqrt(((x1-x2)**2).sum())

if __name__ == "__main__":
    # performance test
    from sklearn.datasets import make_blobs
    from sklearn.metrics import silhouette_score
    from sklearn.cluster import KMeans
    import time

    print("Performance test for 1000 data points with 2 features and 5 groups")
    # generate data
    X, y = make_blobs(n_samples=1000, centers=5, n_features=2, random_state=0)
    df = pd.DataFrame(X, columns=['x1', 'x2'])
    df['label'] = y

    # KNN
    start = time.time()
    knn = KNN()
    knn.fit(df, k=5, explain=False)
    end = time.time()
    print(f"KNN time : {end-start}")
    print(f"KNN score : {silhouette_score(df.iloc[:, :-1], df['label'])}")

    # KMeans
    start = time.time()
    kmeans = KMeans(n_clusters=5, n_init=10)
    kmeans.fit(df.iloc[:, :-1])
    end = time.time()
    print(f"KMeans time : {end-start}")
    print(f"KMeans score : {silhouette_score(df.iloc[:, :-1], kmeans.labels_)}")

    # plot
    import matplotlib.pyplot as plt
    plt.scatter(df['x1'], df['x2'], c=df['label'])
    plt.show()
