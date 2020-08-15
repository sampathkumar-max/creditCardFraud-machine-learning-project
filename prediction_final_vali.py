from FOL_cre_val_prediction.FOL_cre_val import prediction_val
from prediction_database_validataion.pre_database_vali import db_vali
from Log_Main_Fail.Main_Log import APP_logger
import os

class Final_validation:
    def __init__(self,path):
        self.path=path
        self.prediction_val=prediction_val(self.path)
        self.db_vali=db_vali()
        self.log=APP_logger()

    def validation(self):
        try:

            Sample_file, lendatestamp, lentimeStamp, no_col, col_name=self.prediction_val.schema_values()
            self.prediction_val.create_good_bad_folder()
            self.prediction_val.cheack_filename(lendatestamp,lentimeStamp)
            self.prediction_val.cheack_col(no_col)
            self.prediction_val.cheack_mis_col()
            self.prediction_val.move_bad_to_archivedbad()
            #self.prediction_val.delete_bad_data()
            self.db_vali.DBconnection("prediction")
            self.db_vali.dbtablecreation("prediction",col_name)
            self.db_vali.insert_table_into_db("prediction")
            self.db_vali.Export_DB_csv("prediction")
            #self.Training_val.delete_good_data()
        except Exception as e:
            return e



