#import
import requests
import json


#scrape the entire subreddit.
#subreddit = name of the subreddit, start = start time, end = end time
#optionals: delta = time between each scrape, size = number of posts in each scrape
def scrape_entire_subreddit(subreddit, scrape_start, scrape_end, delta = 86400, size = 100):
    #raw data
    raw_data = []

    #time
    delta = 86400
    startTime=scrape_start
    endTime=scrape_start + delta

    day = 1

    while endTime<=scrape_end:
        #scrape
        url = "https://api.pushshift.io/reddit/search/submission/?subreddit="+subreddit+"&sort=asc&sort_type=created_utc&after=" + str(startTime) + "&before="+str(endTime)+"&size="+str(size)
        r = requests.get(url)

        try:
            all_post = r.json().get('data', -1)

            #store to raw data
            for post in all_post:
                raw_data.append(post['title']+" "+post['selftext'])
        except:
            print("failed at day "+str(day))

        #update time
        startTime = endTime
        endTime = endTime + delta
        day +=1

    return raw_data