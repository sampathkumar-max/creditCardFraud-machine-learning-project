import sqlite3
import os
from Log_Main_Fail.Main_Log import APP_logger
import pandas as pd
import shutil
import csv
from datetime import datetime


class db_vali:
    def __init__(self):
        self.path = "Training_database//"
        self.log = APP_logger()
        self.good_file_path = "Training_raw_file//Good_data"
        self.bad_file_path = "Training_raw_file//bad_data"

    def DBconnection(self, DatabaseName):
        try:
            conn = sqlite3.connect(self.path + DatabaseName + ".db")
            message = "succesfully Database connection done"
            self.log.log("log_msg//database.txt", message)
        except Exception as e:
            message = "there is some error in database creation  function ,the error is {a}".format(a=e)
            self.log.log("log_msg//database.txt", message)
            return e
        return conn

    def dbtablecreation(self, Databasename, column):
        try:
            conn = self.DBconnection(Databasename)
            c = conn.cursor()
            c.execute("SELECT count(name)  FROM sqlite_master WHERE type = 'table'AND name = 'Good_Raw_Data'")
            if c.fetchone()[0] == 1:
                conn.close()
            else:
                for col in column.keys():
                    type=column[col]
                    try:
                        c.execute("ALTER TABLE Good_Raw_Data ADD column'{col_name}'{type}".format(col_name=col,type=type))
                    except:
                        c.execute("CREATE TABLE Good_Raw_Data({col_name} {type})".format(col_name=col,type=type))
                message = "succesfully Database table_creation connection done"
                self.log.log("log_msg//database.txt", message)

        except Exception as e:
            message = "there is some error in database creation  function ,the error is {a}".format(a=e)
            self.log.log("log_msg//database.txt", message)
            return e
        conn.close()
    def insert_table_into_db(self,Databasename):
        try:


            conn=self.DBconnection(Databasename)
            c=conn.cursor()
            list_files=os.listdir("training_raw_file//Good_data//")
            for i in list_files:
                with open("training_raw_file//Good_data//"+i,"r")as f:
                    next(f,1)
                    for j in enumerate(f):
                        c.execute("INSERT INTO Good_Raw_Data VALUES ({VALUE})".format(VALUE=j[1]))
            message = "succesfully Database connection done"
            self.log.log("log_msg//database.txt", message)
            conn.commit()
            c.close()
            conn.close()
        except Exception as e:
            message = "there is some error in database creation  function ,the error is {a}".format(a=e)
            self.log.log("log_msg//database.txt", message)
            return e
        conn.close()

    def Export_DB_csv(self,Databasename):
        try:
            input_file = "FileFrom_DB"
            conn = self.DBconnection(Databasename)
            c = conn.cursor()
            if not os.path.isdir(input_file):
                os.makedirs(input_file)
            c.execute("SELECT * FROM Good_Raw_Data")
            result=c.fetchall()
            header=[i[0] for i in c.description]
            csv_file=csv.writer(open("FileFrom_DB//input.csv","w",newline=""),delimiter=",")
            csv_file.writerow(header)
            csv_file.writerows(result)
            message = "succesfully Database Exported into csv file  connection done"
            self.log.log("log_msg//database.txt", message)
        except Exception as e:
            message = "there is some error in database creation  function ,the error is {a}".format(a=e)
            self.log.log("log_msg//database.txt", message)
        c.close()






























