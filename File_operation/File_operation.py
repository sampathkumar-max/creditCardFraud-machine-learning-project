import os
import shutil
import pickle
from Log_Main_Fail.Main_Log import APP_logger


class model_file:
    def __init__(self):
        self.file="model//"
        self.log=APP_logger()
        self.pickle=pickle



    def model_save(self,model,filename):
        try:
            path=self.file+filename
            if os.path.isdir(path):
                shutil.rmtree(path)
                os.makedirs(path)
            else:
                os.makedirs(path)
            with open(path+"//"+filename+".pickle","wb")as f:


                pickle.dump(model,f)
                f.close()
            message="{a} model saved succesfully".format(a=model)
            self.log.log("log_msg//model_load_pre.txt",message)

        except Exception as e:
            message="there is some erroe in this funtion,the error is {fun}".format(fun=e)
            self.log.log("log_msg//model_load_pre.txt",message)
            return e

    def load_model(self,filename):
        try:

            self.file=filename
            path="model//"+self.file
            with open(path+"//"+self.file+".pickle","rb")as f:
                model=pickle.load(f)
                f.close()


            message="successfully {model} imported ".format(model=filename)
            self.log.log("log_msg//load_mdel.txt",message)
            return model
        except Exception as e:

            message = "there is some erroe in this funtion,the error is {fun}".format(fun=e)
            self.log.log("log_msg//load_model.txt",message)
            return e

    def find_correct_model_file(self,num_clu):
        #try:


            list_file=os.listdir(self.file)
            for file in list_file:
                if file[-1]==str(num_clu):
                    return file


            message = "successfully runed this programme"
            self.log.log("log_msg//model_best_pre..txt", message)


        #except Exception as e:
            #message = "there is some erroe in this funtion,the error is {fun}".format(fun=e)
            #self.log.log("log_msg//model_best_pre.txt",message)
           # return e









