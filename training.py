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



def predict(data):
    model = pickle.load(open('model.pkl','rb'))
    return model.predict(data)
