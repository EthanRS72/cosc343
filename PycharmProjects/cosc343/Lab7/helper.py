__author__ = "Lech Szymanski"
__organization__ = "COSC343/AIML402, University of Otago"
__email__ = "lech.szymanski@otago.ac.nz"
__date__ = "August 2022"

import numpy as np
from sklearn import datasets


# AND dataset
def load_and():
    """ Loads the AND dataset of 4 samples

    :return: (X,y) - a 2x4 data matrix and corresponding 4-dim vector of labels
    """
    X = np.array([[-1, -1],
                  [-1, 1],
                  [1, -1],
                  [1, 1]]).astype('float32')
    y = np.array([0,
                  0,
                  0,
                  1]).astype('uint8')

    return X, y


def load_xor():
    """ Loads the XOR dataset of 4 samples

    :return: (X,y) - a 2x4 data matrix and corresponding 4-dim vector of labels
    """
    X = np.array([[-1, -1],
                  [-1, 1],
                  [1, -1],
                  [1, 1]]).astype('float32')
    y = np.array([0,
                  1,
                  1,
                  0]).astype('uint8')

    return X, y


def load_iris(ver2D=False):
    """ Loads the iris dataset of 4 samples.

    :param ver2D: a boolean, if True loads the D=2 attribute
                  version of the dataset, otherwise loads
                  the D=4 attribute version
    :return: (X,y) - a 150xD data matrix and corresponding 150-dim vector of labels
    """

    # Load the dataset from sklearn
    iris = datasets.load_iris()
    X = iris.data

    if ver2D:
        # If 2D mode requested use PCA to cast
        # data from 4D to 2D
        from sklearn.decomposition import PCA
        X = PCA(n_components=2, random_state=0).fit_transform(X)

    y = iris.target.astype('uint8')

    return X, y


def load_iris2D():
    """ Loads the 2D version of iris dataset.

    :return: (X,y) - a 150x2 data matrix and corresponding 150-dim vector of labels
    """
    return load_iris(ver2D=True)


# Digits dataset - 8x8 pixel image version of the MNIST dataset
def load_digits():
    """ Loads the Sklearn's digits dataset of 8x8 grayscale images
        of digits.

    :return: (X,y) - a Nx64 data matrix and corresponding N-dim vector of labels
    """

    digits = datasets.load_digits()

    X = digits.data
    y = digits.target

    return X, y
