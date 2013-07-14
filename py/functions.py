from collections import defaultdict


def word_count(obj):
    obj = ' '.join(obj)
    n = defaultdict(int)
    for i in obj.split(' '):
        i = i.lower().strip('.,?!"').split("'")[0]
        n[str(i)] += 1
    return n


def word_count_nrm(obj):
    obj = ' '.join(obj)
    n = defaultdict(int)
    for i in obj.split(' '):
        i = i.lower().strip('.,?!"').split("'")[0]
        n[str(i)] += 1
    n_words = sum(n.values())
    for i in n:
        n[i] = float(n[i]) / float(n_words)
    return n


def most_common(words, percentile_keep):
    d = words.items()
    list = sorted(d, key=lambda d: -d[1])
    keep = int(len(list) * percentile_keep)
    list = list[:keep]
    return list



def ma_with_rolling_impute(df, column, ma_column, ma):
    df[ma_column] = pd.rolling_mean(df[column], ma)
    #Impute ma-1 observations
    for i in range(1, ma - 1):
        df['ma_%s' % (i + 1)] = pd.rolling_mean(df[column], (i + 1))
        df[ma_column].fillna(df['ma_%s' % (i + 1)], inplace=True)
        del df['ma_%s' % (i + 1)]
    df[ma_column].fillna(df[column], inplace=True)
    return df



df['percent_wa3'].fillna(df['percent'], inplace=True)
