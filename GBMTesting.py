from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score


def main():
    data = pd.read_csv('dataSet.csv')
    data = data.sample(frac=1)  # shuffle -> fixes boosting errors

    y = data.Risk
    x = data.drop('Risk', axis=1)

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

    model = GradientBoostingClassifier(n_estimators=100, max_depth=5)

    print('Shape of training data :', x_train.shape)
    print('Shape of testing data :', x_test.shape)
    model.fit(x_train, y_train)

    predict_train = model.predict(x_train)
    print('\nTarget on train data', predict_train)

    accuracy_train = accuracy_score(y_train, predict_train)
    print('\naccuracy_score on train dataset : ', accuracy_train)

    predict_test = model.predict(x_test)
    print('\nTarget on test data', predict_test)

    accuracy_test = accuracy_score(y_test, predict_test)
    print('\naccuracy_score on test dataset : ', accuracy_test)


if __name__ == "__main__":
    main()
