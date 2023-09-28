
from tshark import Tshark
import subprocess
import time
import json

class Experiment():
    def __init__(self, server, client, isTshark=False):
        self.server = server
        self.client = client
        self.tshark = Tshark() if isTshark else None
        self.is_valid = False
        self.results = {
            'time': None,
            'client_packets': None,
            'server_packets': None,
            'client_bytes': None,
            'server_bytes': None,
            'json_packets': None
        }

    def isTshark(self):
        return self.tshark != None

    def run(self):
        with_tshark_if_is_required = ' [with tshark]' if self.isTshark() else ''
        header = 'Experimento ' + self.client.curve + ' (' + self.server.name + ' - ' + self.client.name + ')' + with_tshark_if_is_required 
        print('\n' + header)
        print('=' * len(header) + '\n')

        self.server.run()

        if self.isTshark():
            self.tshark.listen(3)

        time.sleep(1)
        pre_client = time.time()
        self.client.run()
        post_client = time.time()

        if self.isTshark():
            self.tshark.stop()

        self.server.stop()

        self.is_valid = self.client.check()

        self.results['time'] = post_client - pre_client
        if self.is_valid:
            print('\r\n[*] Experimento realizado con éxito en ' + str(self.results['time']) + ' segundos \n')
        else:
            print('\r\n[!] Algo ha salido mal... El experimento fallido ha durado ' + str(self.results['time']) + ' segundos \n')
        tshark_path_if_is_required = ', ' + self.tshark.output_path if self.isTshark() else ''
        print('\rPuede encontrar los logs del experimento en: ' + self.server.output_path + ', ' + \
              self.client.output_path + tshark_path_if_is_required)

        if self.isTshark():
            time.sleep(2)
            self.print_and_save_results(self.tshark.output_path)

        print('\r')

    def print_and_save_results(self, tshark_path):
        file_in = open(tshark_path, 'r')
        results_arr = [line.split('\t') for line in file_in.read().split('\n')][:-1]
        
        self.results['json_packets'] = []
        client_lengths = []
        server_lengths = []
        for line_arr in results_arr:
            data = {
                'number': int(line_arr[0]),
                'time': float(line_arr[1]),
                'source': line_arr[2].strip(),
                'destination': line_arr[4].strip(),
                'protocol': line_arr[5],
                'length': int(line_arr[6]),
                'info': line_arr[7]
            }
            self.results['json_packets'].append(data)
            is_all_data = all(['Application Data' == x for x in data['info'].split(', ')])

            if not is_all_data:
                if data['source'] == '172.18.0.3':
                    client_lengths.append(data['length'])
                elif data['source'] == '172.18.0.2':
                    server_lengths.append(data['length'])
        
        self.results['client_packets'] = len(client_lengths)
        self.results['client_bytes'] = sum(client_lengths)
        self.results['server_packets'] = len(server_lengths)
        self.results['server_bytes'] = sum(server_lengths)
        print('\r\nCantidad total de paquetes enviados por el Ciente:', self.results['client_packets'])
        print('\rCantidad total de bytes enviados del Cliente:', self.results['client_bytes'])
        print('\r\nCantidad total de paquetes enviados por el Servidor:', self.results['server_packets'])
        print('\rCantidad total de bytes enviados del Servidor:', self.results['client_bytes'])

        json_path = 'output/tshark.json'
        with open(json_path, 'w', encoding='utf-8') as file_out:
            json.dump(self.results['json_packets'], file_out, ensure_ascii=False, indent=2)
        print('\r[&] Más información en', json_path)
