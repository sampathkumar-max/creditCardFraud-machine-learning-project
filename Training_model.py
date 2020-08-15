from preprocessing_data.preprocessing import preprocessar
from preprocessing_data.clustering import cluter
from File_operation.File_operation import model_file
from best_model_finder.best_model import best_model_tuner
from Log_Main_Fail.Main_Log import APP_logger
from sklearn.model_selection import train_test_split
import pandas as pd


class model_training:
    def __init__(self, path):
        self.input_file = path
        self.preprocesser = preprocessar()
        self.cluster = cluter()
        self.best_model = best_model_tuner()
        self.log = APP_logger()
        self.model_save = model_file()

    def training_model(self):
        #try:

            data = pd.read_csv(self.input_file)
            X, Y = self.preprocesser.splite_data(data, "default payment next month")
            # x_train,x_test,y_train,y_test=self.preprocesser.train_test_splt(X,Y)
            n_cluster = self.cluster.num_cluster(X)
            x = self.cluster.K_cluster(X, n_cluster)
            self.model_save.model_save(self.cluster,"KMeans")
            x["label"] = Y

            list_of_cluster = x["cluster"].unique()
            for i in list_of_cluster:
                cluster_data = X[X["cluster"] == i]
                cluster_feature = cluster_data.drop(columns=["cluster", "label"])
                cluster_label = cluster_data["label"]
                x_train, x_test, y_train, y_test = train_test_split(cluster_feature, cluster_label, test_size=.30,
                                                                    random_state=42)

                model, model_name = self.best_model.best_model(x_train, x_test, y_train, y_test)

                self.model_save.model_save(model, model_name + str(i))

            message = "succesfully trainied model"
            self.log.log("log_msg//model_finaltrain.txt", message)

        #except Exception as e:
            #message = "there is some error in database creation  function ,the error is {a}".format(a=e)
            #self.log.log("log_msg//finaltrain.txt", message)
            #return e