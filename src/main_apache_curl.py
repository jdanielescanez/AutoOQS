
from experiment import Experiment
from curves import CURVES
from apache import Apache
from curl import Curl
import argparse
from argparse import RawTextHelpFormatter

epilog = 'Lista de protocolos postcuánticos permitidos:\n'
for curve in CURVES:
    curve_arr = curve.split('_')
    if len(curve_arr) == 1:
        help_msg = 'Puro: ' + curve_arr[0]
    else:
        help_msg = 'Híbrido: ' + curve_arr[1] + \
                   ' + ECDH con curva ' + curve_arr[0]
    epilog += ' ' * 2 + curve + ' ' * (len('p521_frodo1344shake') - len(curve)) + \
              '\t\t' + help_msg + '\n'

parser = argparse.ArgumentParser(prog='AutoOQS', description='Experimentos automatizados de Open Quantum Safe', epilog=epilog, formatter_class=RawTextHelpFormatter)
parser.add_argument('-t', '--tshark', dest='isTshark', action='store_true', help='Captura el tráfico con la herramienta tshark')
parser.add_argument('-p', '--protocol', metavar='protocol', choices=CURVES, help='Protocolo que se desea utilizar', required=True)

args = parser.parse_args()

experiment = Experiment(Apache(), Curl(args.protocol), isTshark=args.isTshark)
experiment.run()
