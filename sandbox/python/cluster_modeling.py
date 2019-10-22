import pandas as pd
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE
from sklearn.svm import SVC, NuSVC, LinearSVC
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis



sm = SMOTE(random_state=1)
X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

names = ["Nearest Neighbors", "Linear SVM", "Gaussian Process",
         "Decision Tree", "Random Forest", "AdaBoost",
         "Naive Bayes", "QDA"]

classifiers = [
    KNeighborsClassifier(6),
    SVC(kernel="linear", C=0.025),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()]



scores = cross_val_score(classifier, X_train_res, y_train_res, cv=5)
print(f"scores: {scores}\n95% CI: {round(scores.mean(), 2)} ",
     f"(+/- {round(scores.std() * 2, 2)})")



for name, clf in zip(names, classifiers):
    clf.fit(X_train_res, y_train_res)
    preds = clf.predict(X_test)
    print(f"{name}\naccuracy: {accuracy_score(y_test, preds)}\nF1: ",
        f"{f1_score(y_test, preds)}\nconfusion matrix: \n", 
        f"{confusion_matrix(y_test, preds, labels=[0, 1])}")


def bag_model(df, target, depth, samples):

    X = df.drop([target], axis=1)
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                   random_state=1)

    rt = DecisionTreeRegressor(random_state=1, max_depth=depth)

    rf = RandomForestRegressor(n_estimators=100, max_features='sqrt', random_state=1)

    bag = BaggingRegressor(n_estimators=100,
                       max_features=X.shape[1],
                       max_samples=samples,
                       random_state=1)

    rt.fit(X_train, y_train)
    rf.fit(X_train, y_train)
    bag.fit(X_train, y_train)

    return f"""Decision Tree Score = {rt.score(X_test, y_test)}, ---
    Bagging Score = {bag.score(X_test, y_test)}, --- Random Forest Score
    {rf.score(X_test, y_test)}"""