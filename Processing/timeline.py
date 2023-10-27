from non_rumours import data

def get_timeline(info):
    tids = []
    timeline = []
    texts = []
    tid_time = {}

    for tid, item in info.items():
        nt = item['time']
        if nt not in tid_time:
            tid_time[nt] = [tid]
        else:
            tid_time[nt].append(tid)
            tid_time[nt] = sorted(tid_time[nt])
    time_s = sorted(tid_time.keys())

    for nt in time_s:
        ids = tid_time[nt]
        for tid in ids:
            tids.append(tid)
            timeline.append(info[tid]['time'])
            texts.append(info[tid]['text'])

    return tids, timeline, texts

for claim in data:
    tids, timeline, texts = get_timeline(data[claim]['info'])
    data[claim]['timeline'] = timeline
    data[claim]['tids'] = tids
    data[claim]['texts'] = texts