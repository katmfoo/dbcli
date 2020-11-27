from abc import ABC, abstractmethod

class Driver(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute(self):
        pass

class ExecutionResponse():

    def __init__(self, success=True, headers=None, result=None, rowcount=None, error_message=None):
        self.success = success
        self.headers = headers
        self.result = result
        self.rowcount = rowcount
        self.error_message = error_message
