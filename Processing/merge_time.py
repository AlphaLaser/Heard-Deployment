from timeline import data

def timeline_convert_merge_time(data, interval):
    for eid, info in data.items():
        timeLine = data[eid]['timeline']
        texts = data[eid]['texts']
        tids = data[eid]['tids']

        merge_index = []
        anchor = timeLine[0]
        merge_index.append(0)

        for ti, t in enumerate(timeLine):
            if t - anchor != interval:
                merge_index.append(ti)
            anchor = t
        merge_texts, merge_tids, merge_times, = [], [], []

        for i, index in enumerate(merge_index):
            try:
                next_index = merge_index[i + 1]
            except:
                next_index = index + len(timeLine) + 2

            assert next_index != index
            merge_text = [x for x in texts[index:next_index]]
            merge_tid = [x for x in tids[index:next_index]]
            merge_time = [x for x in timeLine[index:next_index]]
            assert len(merge_time) != 0 and len(merge_text) != 0 and len(merge_tid) != 0

            merge_texts.append(merge_text)
            merge_tids.append(merge_tid)
            merge_times.append(merge_time)

        data[eid]['merge_seqs'] = {'merge_tids': merge_tids, 'merge_times': merge_times, 'merge_texts': merge_texts}

    return data

converted_data = timeline_convert_merge_time(data, interval=0)