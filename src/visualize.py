#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# get the top 10 keys, then flip them to low-to-high order
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top10 = items[:10]
top10.reverse()

# split into x-axis labels and bar heights
keys = [k for k,v in top10]
values = [v for k,v in top10]

# draw the bar graph and save it as a png
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.bar(keys, values)
plt.xlabel('language' if args.input_path.endswith('.lang') else 'country')
plt.ylabel('number of tweets')
plt.tight_layout()

output_file = os.path.basename(args.input_path) + '_' + args.key.lstrip('#') + '.png'
plt.savefig(output_file)
print('saved', output_file)
