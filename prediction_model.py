
from preprocessing_data.preprocessing import preprocessar
from File_operation.File_operation import model_file
import pandas as pd
import numpy as np


class model_prediction:
    def __init__(self, path):
        self.inputfile = path
        self.preprocesar = preprocessar
        self.file_opreation = model_file()

    def final_clus_pre(self):

        data = pd.read_csv(self.inputfile)
        km = self.file_opreation.load_model("kmeans_clu")
        cluster = km.predict(data)
        data["cluster"] = cluster
        list_cluster = data["cluster"].unique()
        final = []
        for clus in list_cluster:
            cluster_data = data[data["cluster"] == clus]
            cluster_feature = cluster_data.drop(columns="cluster")
            self.bestfile = model_file()
            file_name = self.bestfile.find_correct_model_file(clus)

            model = self.file_opreation.load_model(file_name)
            # model=self.file_opreation.load_model(final_value1)

            cluster_data["defaluter"] = model.predict(cluster_feature)
            cluster_data.to_csv("Final_Dataset/cluster_data1" + str(clus) + ".csv")








