import json
import logging

# reads input from given file path and returns
class InputReader:
    @staticmethod
    def load_data(file_name: str):
        data = []
        try:
            with open(file_name, "r") as json_file:
                for line in json_file:
                    data.append(Customer(**json.loads(line)) )
        except FileNotFoundError:
            logging.error("Input file not file: {}".format(file_name) )
        if len(data) == 0:
            logging.error("No customer data specified in input file!")
        return data
# Open the given out file and writes result data.
class OutWriter:
    @staticmethod
    def output(file_name, out):
        f = open(file_name, "w")
        if not f:
            logging.error("Cannot open out file: {}".format(file_name) )
        else:
            f.write(str(out))
            f.close()

class Customer:
    def __init__(self, user_id:int, name: str, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id
        self.name = name

    def getNameAndIDs(self) -> tuple:
        return (self.name, self.user_id)

