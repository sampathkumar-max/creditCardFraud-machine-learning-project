import Traning_Final_Validation
import Training_model
import prediction_model
import prediction_final_vali

class final:
    def __init__(self,batch_path_tra,db_file_tre,batch_path_pre,db_file_pre):
        self.trainig_val=Traning_Final_Validation.Final_validation(batch_path_tra)
        self.model_training=Training_model.model_training(db_file_tre)
        self.prediction_val=prediction_final_vali.Final_validation(batch_path_pre)
        self.model_prediction=prediction_model.model_prediction(db_file_pre)

    def final(self):
        self.trainig_val.validation()
        self.model_training.training_model()
        self.prediction_val.validation()
        self.model_prediction.final_clus_pre()






