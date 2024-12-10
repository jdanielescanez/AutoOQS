
import subprocess
from colorama import Fore

class Tshark():
  def __init__(self):
    self.name = 'TShark'
    self.output_path = 'output/' + self.name.lower() + '.txt'
    procces_id = subprocess.Popen(['sudo', 'docker', 'network', 'ls', '-f', 'name=httpd-test', '--format', '"{{.ID}}"'], \
                                    shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    self.interface_id = str(procces_id.stdout.read()).split('"')[1]

  def listen(self, duration):
    print(Fore.YELLOW + '[TSHARK] Escuchando el tráfico con tshark' + Fore.RESET)
    self.output_file = open(self.output_path, 'wb')
    self.process = subprocess.Popen(['sudo', 'tshark', '-a', 'duration:' + str(duration), '-T', 'tabs','-i', 'br-' + self.interface_id], \
                                    shell=False, stdout=self.output_file, stderr=subprocess.DEVNULL)

  def stop(self):
    print(Fore.YELLOW + '\r[TSHARK] Cerrando tshark' + Fore.RESET)
    self.output_file.close()
    self.process.send_signal(subprocess.signal.SIGINT)
