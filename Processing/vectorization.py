from merge_time import converted_data
from functions import *

def compute_tfidf(data):

    vec_data = {}
    corpus = []
    vecs = {}
    for eid,info in data.items():
        merge_seqs = info['merge_seqs']
        merge_texts = merge_seqs['merge_texts']

        vecs[eid] = [0]*len(merge_texts)
        for ti,text in enumerate(merge_texts):
            f_text = ' '.join(text).lower()
            # raw text should be pre-processed before that, the unit could be either single text or merged texts
            corpus.append(f_text)
            vecs[eid][ti] = len(corpus)-1

    vectorizer = TfidfVectorizer(analyzer='word',stop_words= 'english',max_features=1000)
    X = vectorizer.fit_transform(corpus)

    for _,(eid,_) in enumerate(data.items()):
        X_index = vecs[eid]
        f_vecs = []
        for index in X_index:
            f_vecs.append(X[index])
        tmp = [x.toarray().tolist()[0] for x in f_vecs]
        vec_data[eid] = tmp
        data[eid]['merge_seqs']['merge_vecs'] = tmp
        data[eid].pop('info')
        data[eid].pop('timeline')
    return data

processed_data = compute_tfidf(converted_data)