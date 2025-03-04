from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import svm
from datetime import datetime


# define a Gaussain NB classifier
clf = GaussianNB()
# Declare the SVM classifier
svm_clf = svm.SVC(kernel='poly', degree=2, max_iter=3000)

# define the class encodings and reverse encodings
classes = {0: "Iris Setosa", 1: "Iris Versicolour", 2: "Iris Virginica"}
r_classes = {y: x for x, y in classes.items()}

# function to train and load the model during startup
def load_model():
    # load the dataset from the official sklearn datasets
    X, y = datasets.load_iris(return_X_y=True)

    # do the test-train split and train the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    svm_clf.fit(X_train, y_train)

    # calculate the print the accuracy score
    acc = accuracy_score(y_test, svm_clf.predict(X_test))
    print(f"Model trained with accuracy: {round(acc, 3)}")


# function to predict the flower using the model
def predict(query_data):
    x = list(query_data.dict().values())
    prediction = svm_clf.predict([x])[0]
    print(f"Model prediction: {classes[prediction]}")
    current_time = datetime.now().time()
    print("Current Time =", current_time)
    return [classes[prediction], current_time] 

# function to retrain the model as part of the feedback loop
def retrain(data):
    # pull out the relevant X and y from the FeedbackIn object
    X = [list(d.dict().values())[:-1] for d in data]
    y = [r_classes[d.flower_class] for d in data]

    # fit the classifier again based on the new data obtained
    svm_clf.fit(X, y)
