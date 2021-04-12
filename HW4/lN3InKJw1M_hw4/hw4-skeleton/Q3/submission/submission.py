
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: Q3.ipynb

import numpy as np
import pandas as pd
import time
import gc
import random
from sklearn.model_selection import cross_val_score, GridSearchCV, cross_validate, train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

class GaTech():
    # Change to your GA Tech Username
    def GTusername(self):
        gt_username = "fjpm3"
        return gt_username

class Data():

    # points [1]
    def dataAllocation(self,path):
        # TODO: Separate out the x_data and y_data and return each
        # args: string path for .csv file
        # return: pandas dataframe, pandas series
        # -------------------------------
        # ADD CODE HERE
        data = pd.read_csv(path)
        y_data = data['y']
        x_data = data[['x1','x2','x3','x4','x5','x6','x7','x8']]
        # -------------------------------
        return x_data,y_data

    # points [1]
    def trainSets(self,x_data,y_data):
        # TODO: Split 70% of the data into training and 30% into test sets. Call them x_train, x_test, y_train and y_test.
        # Use the train_test_split method in sklearn with the parameter 'shuffle' set to true and the 'random_state' set to 614.
        # args: pandas dataframe, pandas dataframe
        # return: pandas dataframe, pandas dataframe, pandas series, pandas series
        # -------------------------------
        # ADD CODE HERE
        x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.3, random_state=614)
        # -------------------------------
        return x_train, x_test, y_train, y_test

##################################################
##### Do not add anything below this line ########
##################################################

class LinearRegressionModel():

    # points [2]
    def linearClassifier(self,x_train, x_test, y_train):
        # TODO: Create a LinearRegression classifier and train it.
        # args: pandas dataframe, pandas dataframe, pandas series
        # return: numpy array, numpy array
        # -------------------------------
        # ADD CODE HERE
        reg = LinearRegression().fit(x_train, y_train)
        y_predict_train = reg.predict(x_train)
        y_predict_test = reg.predict(x_test)
        # -------------------------------
        return y_predict_train, y_predict_test

    # points [1]
    def lgTrainAccuracy(self,y_train,y_predict_train):
        # TODO: Return accuracy (on the training set) using the accuracy_score method.
        # Note: Round the output values greater than or equal to 0.5 to 1 and those less than 0.5 to 0. You can use any method that satisfies the requriements.
        # args: pandas series, numpy array
        # return: float
        # -------------------------------
        # ADD CODE HERE

        for j in range(len(y_predict_train)):
            if y_predict_train[j] >= 0.5:
                y_predict_train[j] = 1.0
            else:
                y_predict_train[j] = 0.0

        train_accuracy = accuracy_score(y_train, y_predict_train,normalize=True)
        # -------------------------------
        return train_accuracy

    # points [1]
    def lgTestAccuracy(self,y_test,y_predict_test):
        # TODO: Return accuracy (on the testing set) using the accuracy_score method.
        # Note: Round the output values greater than or equal to 0.5 to 1 and those less than 0.5 to 0. You can use any method that satisfies the requriements.
        # args: pandas series, numpy array
        # return: float
        # -------------------------------
        # ADD CODE HERE
        for j in range(len(y_predict_test)):
            if y_predict_test[j] >= 0.5:
                y_predict_test[j] = 1.0
            else:
                y_predict_test[j] = 0.0

        test_accuracy = accuracy_score(y_test, y_predict_test,normalize=True)

        # -------------------------------
        return test_accuracy

##################################################
##### Do not add anything below this line ########
##################################################

class RFClassifier():

    # points [2]
    def randomForestClassifier(self,x_train,x_test, y_train):
        # TODO: Create a RandomForestClassifier and train it. Set Random state to 614.
        # args: pandas dataframe, pandas dataframe, pandas series
        # return: RandomForestClassifier object, numpy array, numpy array
        # -------------------------------
        # ADD CODE HERE
        #clf =
        rf_clf = RandomForestClassifier(n_estimators=100,random_state=614).fit(x_train, y_train)
        y_predict_train = rf_clf.predict(x_train)
        y_predict_test = rf_clf.predict(x_test)
        # -------------------------------
        return rf_clf,y_predict_train, y_predict_test

    # points [1]
    def rfTrainAccuracy(self,y_train,y_predict_train):
        # TODO: Return accuracy on the training set using the accuracy_score method.
        # args: pandas series, numpy array
        # return: float
        # -------------------------------
        # ADD CODE HERE
        train_accuracy = accuracy_score(y_train, y_predict_train)
        # -------------------------------
        return train_accuracy

    # points [1]
    def rfTestAccuracy(self,y_test,y_predict_test):
        # TODO: Return accuracy on the test set using the accuracy_score method.
        # args: pandas series, numpy array
        # return: float
        # -------------------------------
        # ADD CODE HERE
        test_accuracy = accuracy_score(y_test, y_predict_test)
        # -------------------------------
        return test_accuracy

# Q3.3.1 Feature Importance

    # points [1]
    def rfFeatureImportance(self,rf_clf):
        # TODO: Determine the feature importance as evaluated by the Random Forest Classifier.
        # args: RandomForestClassifier object
        # return: float array
        # -------------------------------
        # ADD CODE HERE
        feature_importance = rf_clf.feature_importances_
        # -------------------------------
        return feature_importance

    # points [1]
    def sortedRFFeatureImportanceIndicies(self,rf_clf):
        # TODO: Sort them in the ascending order and return the feature numbers[0 to ...].
        #       Hint: There is a direct function available in sklearn to achieve this. Also checkout argsort() function in Python.
        # args: RandomForestClassifier object
        # return: int array
        # -------------------------------
        # ADD CODE HERE

        sorted_indices = np.argsort(rf_clf.feature_importances_)[::-1]
        # -------------------------------
        return sorted_indices

# Q3.3.2 Hyper-parameter Tuning

    # points [2]
    def hyperParameterTuning(self,rf_clf,x_train,y_train):
        # TODO: Tune the hyper-parameters 'n_estimators' and 'max_depth'.
        # args: RandomForestClassifier object, pandas dataframe, pandas series
        # return: GridSearchCV object
        # 'n_estimators': [4, 16, 256]
        # 'max_depth': [2, 8, 16]
        # -------------------------------
        # ADD CODE HERE
        parameters = {'n_estimators': [4, 16, 256], 'max_depth': [2, 8, 16]}
        gscv = GridSearchCV(rf_clf,parameters)
        gscv_rfc = gscv.fit(x_train,y_train)
        # -------------------------------
        return gscv_rfc

    # points [1]
    def bestParams(self,gscv_rfc):
        # TODO: Get the best params, using .best_params_
        # args:  GridSearchCV object
        # return: parameter dict
        # -------------------------------
        # ADD CODE HERE
        best_params = gscv_rfc.best_params_
        # -------------------------------
        return best_params

    # points [1]
    def bestScore(self,gscv_rfc):
        # TODO: Get the best score, using .best_score_.
        # args: GridSearchCV object
        # return: float
        # -------------------------------
        # ADD CODE HERE
        best_score = gscv_rfc.best_score_
        # -------------------------------
        return best_score

##################################################
##### Do not add anything below this line ########
##################################################

class SupportVectorMachine():

# Q3.4.1 Pre-process

    # points [1]
    def dataPreProcess(self,x_train,x_test):
        # TODO: Pre-process the data to standardize it, otherwise the grid search will take much longer.
        # args: pandas dataframe, pandas dataframe
        # return: pandas dataframe, pandas dataframe
        # -------------------------------
        # ADD CODE HERE
        sc = StandardScaler()
        sc.fit(x_train)

        scaled_x_train = sc.transform(x_train)
        #sc.fit(x_test)
        scaled_x_test = sc.transform(x_test)

        # -------------------------------
        return scaled_x_train, scaled_x_test

# Q3.4.2 Classification

    # points [1]
    def SVCClassifier(self,scaled_x_train,scaled_x_test, y_train):
        # TODO: Create a SVC classifier and train it. Set gamma = 'auto'
        # args: pandas dataframe, pandas dataframe, pandas series
        # return: numpy array, numpy array
        # -------------------------------
        # ADD CODE HERE
        clf = SVC(gamma = 'auto')
        clf.fit(scaled_x_train,y_train)
        y_predict_train = clf.predict(scaled_x_train)
        y_predict_test = clf.predict(scaled_x_test)
        # -------------------------------
        return y_predict_train,y_predict_test

    # points [1]
    def SVCTrainAccuracy(self,y_train,y_predict_train):
        # TODO: Return accuracy on the training set using the accuracy_score method.
        # args: pandas series, numpy array
        # return: float
        # -------------------------------
        # ADD CODE HERE
        train_accuracy = accuracy_score(y_train, y_predict_train)
        # -------------------------------
        return train_accuracy

    # points [1]
    def SVCTestAccuracy(self,y_test,y_predict_test):
        # TODO: Return accuracy on the test set using the accuracy_score method.
        # args: pandas series, numpy array
        # return: float
        # -------------------------------
        # ADD CODE HERE
        test_accuracy = accuracy_score(y_test, y_predict_test)
        # -------------------------------
        return test_accuracy

# Q3.4.3 Hyper-parameter Tuning

    # points [1]
    def SVMBestScore(self, scaled_x_train, y_train):
        # TODO: Tune the hyper-parameters 'C' and 'kernel' (use rbf and linear).
        # Note: Set n_jobs = -1 and return_train_score = True and gamma = 'auto'
        # args: pandas dataframe, pandas series
        # return: GridSearchCV object, float
        # -------------------------------
        svm_parameters = {'kernel':('linear', 'rbf'), 'C':[0.01, 0.1, 1.0]}
        # ADD CODE HERE
        clf = SVC(gamma = 'auto')
        clf.fit(scaled_x_train,y_train)
        svm_cv = GridSearchCV(clf,n_jobs = -1,return_train_score = True, param_grid = svm_parameters)

        svm_cv = svm_cv.fit(scaled_x_train,y_train)
        best_score = svm_cv.best_score_



        # -------------------------------

        return svm_cv, best_score

    # points [1]
    def SVCClassifierParam(self,svm_cv,scaled_x_train,scaled_x_test,y_train):
        # TODO: Calculate the training and test set accuracy values after hyperparameter tuning and standardization.
        # args: GridSearchCV object, pandas dataframe, pandas dataframe, pandas series
        # return: numpy series, numpy series
        # -------------------------------
        # ADD CODE HERE
        y_predict_train = svm_cv.predict(scaled_x_train)
        y_predict_test = svm_cv.predict(scaled_x_test)
        # -------------------------------
        return y_predict_train,y_predict_test

    # points [1]
    def svcTrainAccuracy(self,y_train,y_predict_train):
        # TODO: Return accuracy (on the training set) using the accuracy_score method.
        # args: pandas series, numpy array
        # return: float
        # -------------------------------
        # ADD CODE HERE
        train_accuracy = accuracy_score(y_train, y_predict_train)
        # -------------------------------
        return train_accuracy

    # points [1]
    def svcTestAccuracy(self,y_test,y_predict_test):
        # TODO: Return accuracy (on the test set) using the accuracy_score method.
        # args: pandas series, numpy array
        # return: float
        # -------------------------------
        # ADD CODE HERE
        test_accuracy = accuracy_score(y_test, y_predict_test)
        # -------------------------------
        return test_accuracy

# Q3.4.4 Cross Validation Results

    # points [1]
    def SVMRankTestScore(self,svm_cv):
        # TODO: Return the rank test score for all hyperparameter values that you obtained in Q3.4.3. The
        # GridSearchCV class holds a 'cv_results_' dictionary that should help you report these metrics easily.
        # args: GridSearchCV object
        # return: int array
        # -------------------------------
        # ADD CODE HERE
        rts = svm_cv.cv_results_
        rank_test_score = rts['rank_test_score']

        # -------------------------------
        return rank_test_score

    # points [1]
    def SVMMeanTestScore(self,svm_cv):
        # TODO: Return mean test score for all of hyperparameter values that you obtained in Q3.4.3. The
        # GridSearchCV class holds a 'cv_results_' dictionary that should help you report these metrics easily.
        # args: GridSearchCV object
        # return: float array
        # -------------------------------
        # ADD CODE HERE
        mts = svm_cv.cv_results_
        mean_test_score = mts['mean_test_score']
        # -------------------------------
        return mean_test_score

##################################################
##### Do not add anything below this line ########
##################################################

class PCAClassifier():

    # points [2]
    def pcaClassifier(self,x_data):
        # TODO: Perform dimensionality reduction of the data using PCA.
        #       Set parameters n_components to 8 and svd_solver to 'full'. Keep other parameters at their default value.
        # args: pandas dataframe
        # return: pca_object
        # -------------------------------
        # ADD CODE HERE
        pca = PCA(n_components=8,svd_solver='full')
        pca.fit(x_data)
        # -------------------------------
        return pca

    # points [1]
    def pcaExplainedVarianceRatio(self, pca):
        # TODO: Return percentage of variance explained by each of the selected components
        # args: pca_object
        # return: float array
        # -------------------------------
        # ADD CODE HERE
        explained_variance_ratio = pca.explained_variance_ratio_
        # -------------------------------
        return explained_variance_ratio

    # points [1]
    def pcaSingularValues(self, pca):
        # TODO: Return the singular values corresponding to each of the selected components.
        # args: pca_object
        # return: float array
        # -------------------------------
        # ADD CODE HERE
        singular_values = pca.singular_values_
        # -------------------------------
        return singular_values

##################################################
##### Do not add anything below this line ########
##################################################