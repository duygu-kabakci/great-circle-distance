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
                    data.append(json.loads(line))
                #json_file.close()
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

# performs query/sort/filter operations on dictionaries. Data should be list of dictionaries
class ListOp:
    def __init__(self, data: list):
        """

        :type data: list[dict]
        """
        self.data = data
    # filter customer list by key and limit
    def filter_data(self, limit: float, key: str):
        try:
            self.data = list(filter(lambda d: d[key] <= limit, self.data))
        except KeyError:
            logging.error("Filter key does not exist!: {}".format(key))
            return False
        return True

    #sort customer list by key
    def sort_data(self, key: str):
        try:
            self.data = sorted(self.data, key=lambda k: k[key])
        except KeyError:
            logging.error("Sort key does not exist!: {}".format(key))
            return False
        return True

    # query name and user id of customer list data
    def getNameAndIDs(self):
        return list(map(lambda d: (d["name"], d["user_id"]), self.data)) # burda keywordun sabit olmasi kotu? anlamsiz context
