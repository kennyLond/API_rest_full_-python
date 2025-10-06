import pathlib
import json

class ManageDB:
    def __init__(self):
        base_dir = pathlib.Path(__file__).resolve().parent.parent
        self.__address_file = base_dir / "db" / "dbInvoice.json"

    def read_invoice(self):
        with open(self.__address_file, "r", encoding="utf-8")as data:
            return json.load(data)
        
    def write_invoice(self, new_data):
        with open(self.__address_file, "w") as data:
            data.write(json.dumps(new_data))