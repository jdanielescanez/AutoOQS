
import subprocess
from colorama import Fore

class Tshark():
  def __init__(self):
    self.name = 'TShark'
    self.output_path = 'output/' + self.name.lower() + '.txt'

  def listen(self, duration):
    print(Fore.YELLOW + '[TSHARK] Escuchando el tráfico con tshark' + Fore.RESET)
    self.output_file = open(self.output_path, 'wb')
    self.process = subprocess.Popen(['sudo', 'tshark', '-a', 'duration:' + str(duration), '-T', 'tabs','-i', 'br-b6c73a98d4d0'], \
                                    shell=False, stdout=self.output_file, stderr=subprocess.DEVNULL)

  def stop(self):
    print(Fore.YELLOW + '\r[TSHARK] Cerrando tshark' + Fore.RESET)
    self.output_file.close()
    self.process.send_signal(subprocess.signal.SIGINT)
