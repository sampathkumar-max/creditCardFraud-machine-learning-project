from xgboost import XGBClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from Log_Main_Fail.Main_Log import APP_logger
from sklearn.metrics import accuracy_score
import numpy as np


class best_model_tuner:
    def __init__(self):
        self.xgboost = XGBClassifier()
        self.naive = GaussianNB()
        self.log = APP_logger()

    def best_para_for_naive(self, x_train, y_train):
        try:
            self.para_gired = {"var_smoothing": [1e-9, .001, .05, .08, .1, .5, 1e-8, 1e-7, 1e-6]}
            giried = GridSearchCV(self.naive, self.para_gired, cv=5, verbose=3)
            giried.fit(x_train, y_train)
            best_var_smoothing = giried.best_params_["var_smoothing"]
            # return best_var_smoothing
            self.naive1 = GaussianNB(var_smoothing=best_var_smoothing)
            self.naive1.fit(x_train, y_train)
            message = "succesfully naive model best parameter find"
            self.log.log("log_msg//naive_model.txt", message)
            return self.naive1
        except Exception as e:
            message = "there is some error in database creation  function ,the error is {a}".format(a=e)
            self.log.log("log_msg//naive_model.txt", message)
            return e

    def best_para_for_XGboost(self, x_train, y_train):
        try:

            para = {"n_estimators": [100, 200, 250],
                    "max_depth": [2, 6, 10]}
            gired = GridSearchCV(self.xgboost, param_grid=para, cv=5, verbose=3)
            gired.fit(x_train, y_train)
            # return gired.best_params_
            self.n_estimater = gired.best_params_["n_estimators"]
            self.max_depth = gired.best_params_["max_depth"]
            self.xgboost = XGBClassifier(n_estimators=self.n_estimater, max_depth=self.max_depth)
            self.xgboost.fit(x_train, y_train)
            message = "succesfully xgboost model best parameter find"
            self.log.log("log_msg//xgboost_model.txt", message)
            return self.xgboost
        except Exception as e:
            message = "there is some error in database creation  function ,the error is {a}".format(a=e)
            self.log.log("log_msg//xgboost_model.txt", message)
            return e

    def best_model(self, x_train, x_test, y_train, y_test):
        try:

            self.xgboost = self.best_para_for_XGboost(x_train, y_train)
            self.naive = self.best_para_for_naive(x_train, y_train)
            xg_pre = self.xgboost.predict(x_test)
            naive_pre = self.naive.predict(x_test)
            xg_score = accuracy_score(y_test, xg_pre)
            naive_score = accuracy_score(y_test, naive_pre)
            message = "succesfully best model find"
            self.log.log("log_msg//best_model.txt", message)
            # return naive_score,xg_score

            if xg_score > naive_score:
                return self.xgboost, "xgboost"
            else:
                return self.naive, "naive"

        except Exception as e:
            message = "there is some error in database creation  function ,the error is {a}".format(a=e)
            self.log.log("log_msg//best_model.txt", message)
            return e