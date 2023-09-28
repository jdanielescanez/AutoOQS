
from abc import ABC, abstractmethod
from colorama import Fore

class Server(ABC):
    def __init__(self, name='ServerName'):
        self.name = name
        self.output_path = 'output/' + self.name.lower() + '.txt'
        self.output_file = None

    @abstractmethod
    def run(self):
        print(Fore.BLUE + '[S] Levantando servidor' + Fore.RESET)
        self.output_file = open(self.output_path, 'wb')

    @abstractmethod
    def stop(self):
        print(Fore.BLUE + '\r[S] Cerrando servidor' + Fore.RESET)
        self.output_file.close()
