import random
from Processing.vectorization import processed_data

eids = list(processed_data.keys())
random.shuffle(eids)

val = eids[0 : 20*len(eids)//100]
fold = eids[20*len(eids)//100 : -1]

def fold_creator():
    random.shuffle(fold)

    train = fold[0: len(fold) * 3 // 4]
    test = fold[len(fold) * 3 // 4: -1]

    output = {
        'train': train,
        'test': test
    }

    return output

fold0 = fold_creator()
fold1 = fold_creator()
fold2 = fold_creator()
fold3 = fold_creator()
fold4 = fold_creator()

data_ids_real = {
    'val': val,
    'fold0': fold0,
    'fold1': fold1,
    'fold2': fold2,
    'fold3': fold3,
    'fold4': fold4,
}