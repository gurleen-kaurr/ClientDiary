from ClientDiary.settings import mongo_db

class Client:
    def __init__(self, client_name, client_address, client_area=None, client_phno=None, client_service_date=None, client_paymentmode=None, client_staff="self"):
        self.client_name = client_name
        self.client_address = client_address
        self.client_area = client_area
        self.client_phno = client_phno
        self.client_service_date = client_service_date
        self.client_paymentmode = client_paymentmode
        self.client_staff = client_staff

    def save(self):
        client_data = {
            "client_name": self.client_name,
            "client_address": self.client_address,
            "client_area": self.client_area,
            "client_phno": self.client_phno,
            "client_service_date": self.client_service_date,
            "client_paymentmode": self.client_paymentmode,
            "client_staff": self.client_staff,
        }
        mongo_db.clients.insert_one(client_data)

    @staticmethod
    def get_all_clients():
        return list(mongo_db.clients.find())

    @staticmethod
    def get_client_by_name(client_name):
        return mongo_db.clients.find_one({"client_name": client_name})

    def __str__(self):
        return self.client_name