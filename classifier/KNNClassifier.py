from sklearn.neighbors import KNeighborsClassifier

from . import AbstractZnormClassifier, test_classifier



class KNNClassifier(AbstractZnormClassifier):
    """Classifier which uses the K-nearest neighbor algorithms"""
    def __init__(self, k, **kwargs):
        # keyword arguments are passed on to scikit-learn's KNN implementation
        # see http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html#sklearn.neighbors.KNeighborsClassifier
        # relevant kwargs:
        #     weights (string): "uniform", "distance"
        #     p (int): 1 (Manhattan distance), 2 (Euclidean distance)
        #     n_jobs (int): 1 or more (used to parallelize neighbor search)
        super(AbstractZnormClassifier, self).__init__("KNN", k=k, **kwargs)
        self.knn = KNeighborsClassifier(n_neighbors=self.params["k"], **kwargs)

    # train a KNN classifier on a provided dataset
    def _train(self, X, Y):
        self.knn.fit(X, Y)

    # classify a set of test points
    def _classify(self, test_X):
        return self.knn.predict(test_X)

#for k in (3, 5, 10, 20):
#    for w in ("uniform", "distance"):
#        for p in (1, 2):
#            test_classifier(KNNClassifier(10, weights=w, p=p, n_jobs=4))