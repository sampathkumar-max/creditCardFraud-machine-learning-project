from Log_Main_Fail.Main_Log import APP_logger
import json
import shutil
import os
import pandas as pd
import numpy as np
from datetime import datetime
import re

class prediction_val:

    def __init__(self,prediction_file_dir):
        self.Batch_dir=prediction_file_dir
        self.Log=APP_logger()
        self.schema="schema_prediction.json"

    def schema_values(self):
        try:
            with open(self.schema,"r")as f:
                dic=json.load(f)
            SampleFileName=dic["SampleFileName"]
            LengthOfDateStampInFile=dic["LengthOfDateStampInFile"]
            LengthOfTimeStampInFile=dic["LengthOfTimeStampInFile"]
            NumberofColumns=dic["NumberofColumns"]
            ColName=dic["ColName"]
            message="succesfully schema_value created"
            self.Log.log("log_msg//schema_values_pre.txt",message)
            return SampleFileName,LengthOfDateStampInFile,LengthOfTimeStampInFile,NumberofColumns,ColName
        except Exception as e:
            message = "there is some error schema_values function ,the error is {a}".format(a=e)
            self.Log.log("log_msg//schema_values_pre.txt", message)
            return e

    def create_good_bad_folder(self):
        try:
            path=os.path.join("prediction_raw_file//Good_data")
            if not os.path.isdir(path):
                os.makedirs(path)
            path=os.path.join("prediction_raw_file//bad_data")
            if not os.path.isdir(path):
                os.makedirs(path)
            message = "succesfully  created good and bad raw data folder"
            self.Log.log("log_msg//create_good_bad_pre.txt", message)

        except Exception as e:
            message = "there is some error in create good and bad data folder  function ,the error is {a}".format(a=e)
            self.Log.log("log_msg//create_good_bad_pre.txt", message)
            return e

    def delete_good_data(self):
        try:
            path="prediction_raw_file//Good_data"
            if os.path.isdir(path):
                shutil.rmtree(path)
            message = "succesfully   deleted good raw data folder"
            self.Log.log("log_msg//delete_good_pre.txt", message)
        except Exception as e:
            message = "there is some error in delete good data folder function ,the error is {a}".format(a=e)
            self.Log.log("log_msg//delete_good_pre.txt", message)
            return e
    def delete_bad_data(self):
        try:
            path="prediction_raw_file//bad_data"
            if os.path.isdir(path):
                shutil.rmtree(path)
            message = "succesfully   deleted bad raw data folder"
            self.Log.log("log_msg//delete_bad_pre.txt", message)
        except Exception as e:
            message = "there is some error in delete bad data folder function ,the error is {a}".format(a=e)
            self.Log.log("log_msg//delete_bad_pre.txt", message)
            return e
    def move_bad_to_archivedbad(self):
        try:
            now=datetime.now()
            date=now.date()
            current_time=date.strftime("%H%M%S")
            source="prediction_raw_file//bad_data"
            if os.path.isdir(source):
                path="prediction_Archived"
                if not os.path.isdir(path):
                    os.makedirs(path)
                source1=path+"\\bad_data_"+str(date)+"-"+str(current_time)
                if not os.path.isdir(source1):
                    os.makedirs(source1)
                list_files=os.listdir(source)
                for file in list_files:
                    if file not in os.listdir(source1):
                        shutil.move(source+"//"+file,source1)
            message = "succesfully   moved bad_file to  Archivedbad folder raw data folder"
            self.Log.log("log_msg//Archived_bad_pre.txt", message)

        except Exception as e:
            message = "there is some error in move_bad_to_archivedbad function ,the error is {a}".format(a=e)
            self.Log.log("log_msg//Archived_bad_pre.txt", message)
            return e
    def cheack_filename(self,len_date,lentime):
        try:
            list_files=os.listdir("prediction_Batch_Files")
            for file in list_files:
                f_split=re.split(".csv",file)[0]
                s_split=re.split("_",f_split)
                if (s_split[0]=="creditCardFraud") and (len(s_split[1])==len_date) and (len(s_split[2])==lentime):
                    shutil.copy("prediction_Batch_Files//"+file,"prediction_raw_file//Good_data")
                else:
                    shutil.copy("prediction_Batch_Files//" + file, "prediction_raw_file//bad_data")
            message = "succesfully   checked all the correct file and copyed to respect folders"
            self.Log.log("log_msg//check_filename_.txt", message)
        except Exception as e:
            message = "there is having some error in file checked  function ,the error is {a}".format(a=e)
            self.Log.log("log_msg//check_filename.txt", message)
            return e

    def cheack_col(self,numofcol):
        try:
            list_files=os.listdir("prediction_raw_file//Good_data")
            for file in list_files:
                data=pd.read_csv("prediction_raw_file//Good_data//"+file)
                if data.shape[1]==numofcol:
                    pass
                else:
                    shutil.move("prediction_raw_file//Good_data//"+file,"prediction_raw_file//bad_data")
            message = "succesfully   checked all columns and copyed to the respect folders"
            self.Log.log("log_msg//check_column_pre.txt", message)
        except Eception as e:
            message = "there is having some error in column checked  function ,the error is {a}".format(a=e)
            self.Log.log("log_msg//check_column_pre.txt", message)
            return e

    def cheack_mis_col(self):
        try:
            list_files = os.listdir("prediction_raw_file//Good_data")
            for file in list_files:
                data=pd.read_csv("prediction_raw_file//Good_data//"+file)
                for col in data.columns:
                    if len(data[col])-data[col].count()==len(data[col]):
                        shutil.move("prediction_raw_file//Good_data//"+file,"prediction_raw_file//bad_data")
            message = "succesfully   checked all columns and copyed to the respect folders"
            self.Log.log("log_msg//check_missing_column_pre.txt", message)
        except Exception as e:
            message = "there is having some error in this   function ,the error is {a}".format(a=e)
            self.Log.log("log_msg//check_missing_column_pre.txt", message)
            return e






















