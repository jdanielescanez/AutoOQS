
import matplotlib.pyplot as plt
from statistics import mean
from numpy import std
import json

json_path = 'output/total_results.json'
with open(json_path, 'r', encoding='utf-8') as results_file:
    results = json.load(results_file)

total_tags = list(results.keys())
algorithms = {'kyber': [], 'bike': [], 'frodo': [], 'hqc': []}
for algorithm_tag in algorithms.keys():
    algorithms[algorithm_tag] = [x for x in total_tags if algorithm_tag in x]

for algorithm_tag in algorithms.keys():
    counts = {}
    for algorithm in algorithms[algorithm_tag]:
        for value_tag in results[algorithm]:
            value = results[algorithm][value_tag]
            if not value_tag in counts.keys():
                counts[value_tag] = [value]
            else:
                counts[value_tag].append(value)

    for value_tag in counts.keys():
        std_x = [std(x) for x in counts[value_tag]]
        means = [mean(x) for x in counts[value_tag]]
        fig, ax = plt.subplots(figsize=(2 * len(algorithms[algorithm_tag]), 4))
        ax.errorbar(
            [''.join(x.split(algorithm_tag)) for x in algorithms[algorithm_tag]],
            means,
            yerr=[std_x, std_x]
        )

        y1, y2 = [[min(z) for z in counts[value_tag]], [max(z) for z in counts[value_tag]]]
        x = [''.join(tag.split(algorithm_tag)) for tag in algorithms[algorithm_tag]]
        ax.scatter(x, means, label='Media')
        ax.scatter(x, y1, color='r', label='Mínimo')
        ax.scatter(x, y2, color='g', label='Máximo')

        ax.set_ylabel(value_tag)
        ax.set_title('Gráfico de ' + value_tag + ' en ' + algorithm_tag)
        ax.legend(loc='upper left')

        # plt.show()
        plt.savefig('output/img/' + value_tag + '-' + algorithm_tag + '.png')
