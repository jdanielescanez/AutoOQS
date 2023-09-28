
from server import Server
import subprocess

class Apache(Server):
  def __init__(self):
    super().__init__('Apache')

  def run(self):
    super().run()
    self.process = subprocess.Popen(['sudo', 'docker', 'run', '--network', 'httpd-test', '--name', 'oqs-httpd', '-p', '4433:4433', 'openquantumsafe/httpd'],
                                    shell=False, stdout=self.output_file, stderr=subprocess.DEVNULL)

  def stop(self):
    super().stop()
    self.process.send_signal(subprocess.signal.SIGINT)
    subprocess.run(['sudo', 'docker', 'stop', 'oqs-httpd'],
                   shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(['sudo', 'docker', 'rm', 'oqs-httpd'],
                   shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
