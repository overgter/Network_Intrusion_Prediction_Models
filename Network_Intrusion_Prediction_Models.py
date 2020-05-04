import numpy as np
import pandas as pd
from sklearn import preprocessing
from scipy.io.arff import loadarff
from sklearn.naive_bayes import GaussianNB
import sklearn_NaiveBayees_UNSW_NB15


def load_nb15_csv():
    nb15_train = pd.read_csv('Datasets/UNSW-NB15/csv/UNSW_NB15_training-set.csv', delimiter=',')
    nb15_test = pd.read_csv('Datasets/UNSW-NB15/csv/UNSW_NB15_testing-set.csv', delimiter=',')
    return nb15_train.to_numpy(), nb15_test.to_numpy()


def load_nslkdd_arff():
    kdd_train, train_metadata = loadarff("Datasets/NSL-KDD/arff/KDDTrain+.arff")
    kdd_test, test_metadata = loadarff("Datasets/NSL-KDD/arff/KDDTest+.arff")
    return np.asarray(kdd_train.tolist()), np.asarray(kdd_test.tolist())


datasets = {1: ("UNSW-NB15 (csv)", load_nb15_csv), 2: ("NSL-KDD (arff)", load_nslkdd_arff)}
algorithms = {1: ("UNSW-NB15 (csv)", load_nb15_csv), 2: ("NSL-KDD (arff)", load_nslkdd_arff)}

def main():
    dataset_selection = get_dataset_selection()

    algorithm_selection = get_algorithm_selection()

    train, test = datasets[dataset_selection][1]()

    sklearn_NaiveBayees_UNSW_NB15.run_naiveBayes(train, test)

def get_dataset_selection():
    while True:
        print("Which dataset would you like to use:")
        for i in range(len(datasets)):
            print("{}. {}".format(i+1, datasets[i+1][0]))

        try:
            user_input = int(input("Your selection: "))
            if user_input > len(datasets) or user_input < 1:
                raise ValueError
        except ValueError:
            print("\nPlease enter a valid number\n\n")
            continue
        else:
            return user_input


def get_algorithm_selection():
    print()


if __name__ == "__main__":
    main()