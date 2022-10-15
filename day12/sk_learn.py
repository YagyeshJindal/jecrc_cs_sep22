from pyexpat import features
from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(features, target , test_size=0.25, random_state=101)

