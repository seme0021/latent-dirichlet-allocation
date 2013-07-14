import redis
from functions import *
import pandas as pd

rd = redis.StrictRedis(host="localhost", port=6379, db=1)


def get_stories(sbeg, send):
    """
    Reads stories from Redis starting with index sbeg and ending with send
    """
    story = []
    for sid in range(sbeg, send):
        phash = 'content:%s:paragraph_*' % sid
        paragraphs = rd.keys(phash)
        if len(paragraphs) > 0:
            for p in paragraphs:
                story.append(rd.get(p))
    return story



stories = get_stories(1000, 2000)
words = word_count_nrm(stories)
throw_away = most_common(words, 0.05)
df = pd.DataFrame(throw_away, columns=['word', 'percent'])
ma_with_rolling_impute(df, 'percent', 'percent_ma3', 3)
 