
class Procedure:

    def __init__(self,name,date,practitioner,charges,patientid):

        self.__name = name
        self.__date = date
        self.__practitioner = practitioner
        self.__charges = charges 
        self.__patientid = patientid

    def set_name(self,name1):
        self.__name = name1
    def set_date(self,date1):
        self.__date = date1
    def set_practitioner(self,prac1):
        self.__practitioner = prac1
    def set_charges(self,charges1):
        self.__charges = charges1
    def set_patientid(self,patient1):
        self.__patientid = patient1


    def get_name(self):
        return self.__name
    def get_date(self):
        return self.__date
    def get_practitioner(self):
        return self.__practitioner
    def get_charges(self):
        return self.__charges
    def get_patientid(self):
        return self.__patientid

