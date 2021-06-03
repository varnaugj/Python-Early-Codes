#check library versions

import sys
#print('Python: {}'.format(sys.version))
# scipy
import scipy
#print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
#print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
#print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
#print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
#print('sklearn: {}'.format(sklearn.__version__))


# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
print(dataset.shape)        #prints dimensions of dataset
print(dataset.head(20))     #prints first 20 lines of data including headers
print(dataset.describe())    ##gives basic stats on data such as mean, count, min, max, etc.
print(dataset.groupby('class').size())  #determines number in each instance and prints value type (float, int, etc.)


#dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)  #box and whisker plot 
#pyplot.show()

#dataset.hist()     #histogram plots
#pyplot.show()

#scatter_matrix(dataset)     #plots data against each other with histograms on the diagonal. Helps in revealing possible correlations 
#pyplot.show()

#process divides data into training and validation data sets. in this case, 80% training, 20% validation
array = dataset.values
X = array[:,0:4]
y = array[:,4]
X_train,X_validation,Y_train,Y_validation = train_test_split(X,y,test_size=0.2, random_state=1)


models = []
models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))    #logistical regression algorithm
models.append(('LDA', LinearDiscriminantAnalysis()))                                #linear discriminant analysis
models.append(('KNN', KNeighborsClassifier()))                                      #K-nearest neighbors
models.append(('CART', DecisionTreeClassifier()))                                   #classification and regression trees
models.append(('NB', GaussianNB()))                                                 #gaussian naive bayes
models.append(('SVM', SVC(gamma='auto')))                                           #support vector machines

# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
	cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring='accuracy')
	results.append(cv_results)
	names.append(name)
	print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))

# Compare Algorithms
#pyplot.boxplot(results, labels=names)
#pyplot.title('Algorithm Comparison')
#pyplot.show()

#based on results, SVM seems most ideal algorithm

# Make predictions on validation dataset
model = SVC(gamma='auto')
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)


# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
