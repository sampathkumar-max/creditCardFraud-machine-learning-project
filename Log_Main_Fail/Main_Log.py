from datetime import datetime

class APP_logger:
    def __init__(self):
        pass

    def log(self, file_object, log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.file_object=file_object
        self.log_message=log_message
        self.current_time = self.now.strftime("%H:%M:%S")
        self.file=open(file_object,"a+")
        self.log_message=log_message
        self.file.write(str(self.date)+" "+str(self.current_time)+" "+ self.log_message+"\n")
        self.file.close()














