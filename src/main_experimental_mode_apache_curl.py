
from experiment import Experiment
from curves import CURVES
from apache import Apache
from curl import Curl
from statistics import mean
from numpy import std
import argparse
import json
from argparse import RawTextHelpFormatter

REPETITIONS = 10
total_results = {}

for curve in CURVES:
    total_results[curve] = {
        'time': [],
        'client_packets': [],
        'client_bytes': [],
        'server_packets': [],
        'server_bytes': []
    }

    i = 0
    while i < REPETITIONS:
        experiment = Experiment(Apache(), Curl(curve), isTshark=True)
        experiment.run()
        if experiment.is_valid and experiment.results['client_bytes'] != 0:
            for key in total_results[curve].keys():
                total_results[curve][key].append(experiment.results[key])
            i += 1

    for key in total_results[curve].keys():
        isDesviated = lambda x: abs(x - mean(total_results[curve][key])) <= 5 * std(total_results[curve][key])
        total_results[curve][key] = list(filter(isDesviated, total_results[curve][key]))

json_path = 'output/total_results.json'
with open(json_path, 'w', encoding='utf-8') as file_out:
    json.dump(total_results, file_out, ensure_ascii=False, indent=2)

print('Results in:', json_path)
