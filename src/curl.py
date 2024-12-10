
from client import Client
import subprocess

class Curl(Client):
  def __init__(self, curve):
    super().__init__('Curl')
    self.curve = curve

  def run(self):
    super().run()

    subprocess.run(['sudo', 'docker', 'run', '--network', 'httpd-test', '-it', 'openquantumsafe/curl', 'curl', '-k', 'https://oqs-httpd:4433', '--curves', self.curve],
                   shell=False, stdout=self.output_file, stderr=subprocess.DEVNULL)
    
    super().stop()

  def check(self):
    super().check()
    f = open(self.output_path, 'r')
    content = f.read()
    f.close()
    return content == '<html><body><h1>It works!</h1></body></html>\n'

    