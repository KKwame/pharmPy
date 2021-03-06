#spliting data into training and testing phases
from sklearn.model_selection import train_test_split
#importing the Gaussian model
#from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
#importing everything from data processing file
from pandas import read_csv

#Importing modeule for accuracy calculation
from sklearn import metrics
import pickle



filename = "DataReal.csv"
datafile = read_csv(filename)

features = ['Headache','Fever','Chills','Spasm','Arthralgia','Asthenia','Sweating','Dizziness','Nausea','Bitter_Mouth','Inaptence','Abdominal_Pains','Cough','Sore_Throat','Sneeze','Diarrhea','Restlessness','Thirst']
X = datafile.loc[:, features]
Y = datafile.Outcome


#Split dataset into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4)
#creating Gaussian model
model = BernoulliNB()
# # training the model with training sets
model.fit(X_train, y_train)


#Predict the response for the test dataset
print("x-test", X_test)
y_predict = model.predict(X_test)
print(y_predict)


##saving mddel
with open("model.pkl", "wb") as f:
    pickle.dump(model,f)



#Model Accuracy
model_accuracy_measure = metrics.accuracy_score(y_test, y_predict)
print("Accuracy:", model_accuracy_measure)

#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predict)
print('Confusion Matrix:',cm)
#if __name__ == 'main':
    #print(model_accuracy_measure)
#loading model for testing
model = pickle.load(open('model.pkl','rb'))
print("Test Outcome:", model.predict([[1,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0]]))
