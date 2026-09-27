# Tracking COVID-19 Hashtags on Twitter in 2020

This project measures how coronavirus-related hashtags were spread across languages and countries during 2020. The dataset used is every geotagged tweet sent in 2020 which is about 1.1 billion tweets that are stored as 366 daily zip files (leap year).

# How it Works

I used a MapReduce approach to process this data in parallel. 'src/map.py' reads one day of tweets and then counts how each of the 17 hashtags appears, broken down by language and country. For the tweets that do not have a country code (can be tweeted from international water), the mapper labelled them as 'unknown' to prevent crashes. 'run_map.py' runs the mapper on all 366 zip files at once in the background using 'nohup', this allows the jobs to be ran simulatenously instead of one day after another.  'src/reduce.py' combines these results into yearly totals, and then 'src/visualize.py' plots the top10 languages and countries for a given hashtag.

# Results

The US led #coronavirus with about 225,000 tweets, followed by India with 89,00 tweets, and in 3rd place was Great Britain with about 67,000 tweets.

![coronavirus by country](reduced.country_coronavirus.png)

English was the most common language for #coronavirus at about 420,000 tweets, followed by Spanish at about 138,000.

![coronavirus by language](reduced.lang_coronavirus.png)

The Korean hashtag #코로나바이러스 was much rarer in geotagged tweets. Almost all of its roughly 290 uses came from South Korea and were written in Korean.

![korean hashtag by country](reduced.country_코로나바이러스.png)

![korean hashtag by language](reduced.lang_코로나바이러스.png)

# Hashtag usage over time

`src/alternative_reduce.py` keeps each day separate instead of summing them, then plots how many tweets used each hashtag on each day of the year. #coronavirus peaked at about 25,000 tweets a day in mid-March, right after the WHO declared a pandemic on March 11. From around April onward, #covid19 overtook it as the more popular tag, with a short spike in early October. #flu stayed flat all year.

![hashtags over time](alternative_reduce_coronavirus_covid19_flu.png)
