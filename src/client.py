
from abc import ABC, abstractmethod
from colorama import Fore

class Client(ABC):
    def __init__(self, name='ClientName'):
        self.name = name
        self.output_path = 'output/' + self.name.lower() + '.txt'
        self.output_file = None

    @abstractmethod
    def run(self):
        print(Fore.GREEN + '[C] Ejecutando cliente' + Fore.RESET)
        try:
            with open(self.output_path, 'w'):
                pass
        except IOError as err:
            raise err
        self.output_file = open(self.output_path, 'wb')

    @abstractmethod
    def check(self):
        pass

    def stop(self):
        print(Fore.GREEN + '\r[C] El cliente terminó su ejecución' + Fore.RESET)
        self.output_file.close()
