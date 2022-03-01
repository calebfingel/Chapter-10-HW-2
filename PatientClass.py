
class Patient:

    def __init__(self, patientid, name, address, phone, veteran_status):

        self.__name = name
        self.__address = address
        self.__phone = phone
        self.__veteran_status = veteran_status
        self.__patientid = patientid
    
    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_veteran_status(self):
        return self.__veteran_status

    def get_phone(self):
        return self.__phone

    def get_patientid(self):
        return self.__patientid

