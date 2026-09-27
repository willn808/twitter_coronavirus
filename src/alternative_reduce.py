#!/usr/bin/env python3
import os, sys, json
import matplotlib.pyplot as plt

hashtags = sys.argv[1:]

# scan: load every 2020 day's counts, in date order
files = sorted(f for f in os.listdir('outputs') if f.startswith('geoTwitter20-') and f.endswith('.lang'))
days = []
for f in files:
    with open(os.path.join('outputs', f)) as fp:
        days.append(json.load(fp))

# plot: one line per hashtag
for hashtag in hashtags:
    totals = [sum(day.get(hashtag, {}).values()) for day in days]
    plt.plot(range(1, len(days)+1), totals, label=hashtag)
plt.xlabel('day of year (2020)')
plt.ylabel('number of tweets')
plt.legend()
plt.tight_layout()
output_file = 'alternative_reduce_' + '_'.join(h.lstrip('#') for h in hashtags) + '.png'
plt.savefig(output_file)
print('saved', output_file)
