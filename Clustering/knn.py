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
    df = pd.DataFrame(data=[[1, 1], 
                            [2, 2], 
                            [3, 3], 
                            [4, 4],
                            [100, 100],
                            [104, 102]], columns=['x', 'y'])
    knn = KNN()
    knn.fit(df, 2, inplace=True)
    print(df)
