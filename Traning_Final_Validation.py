from Fol_cre_val_Training.Fol_cre_Val import  Training_val
from Database_validation.database_validation import db_vali
from Log_Main_Fail.Main_Log import APP_logger
import os

class Final_validation:
    def __init__(self,path):
        self.path=path
        self.Training_val=Training_val(self.path)
        self.db_vali=db_vali()
        self.log=APP_logger()

    def validation(self):
        try:

            Sample_file, lendatestamp, lentimeStamp, no_col, col_name=self.Training_val.schema_values()
            self.Training_val.create_good_bad_folder()
            self.Training_val.cheack_filename(lendatestamp,lentimeStamp)
            self.Training_val.cheack_col(no_col)
            self.Training_val.cheack_mis_col()
            self.Training_val.move_bad_to_archivedbad()
            self.Training_val.delete_bad_data()
            self.db_vali.DBconnection("Training")
            self.db_vali.dbtablecreation("Training",col_name)
            self.db_vali.insert_table_into_db("Training")
            self.db_vali.Export_DB_csv("Training")
            #self.Training_val.delete_good_data()
        except Exception as e:
            return e


