import piexif
from os import listdir
from os.path import isfile, isdir, join, splitext
import cv2
import matplotlib
import numpy as np
import pickle
from random import shuffle

def process_files (filename, training_data, labels, names):
    name = 'train/' + d + "/" +filename
    names.append(name)
    im = cv2.imread(name)
    im = cv2.resize(im, (128,128))
    training_data.append(im)
    labels.append(d)


sub_dirs = [f for f in listdir('train') if isdir(join('train', f))]

tr_data = []
tr_labels = []
tr_names = []

val_data = []
val_labels = []
val_names = []

for d in sub_dirs:
    all_files = [f for f in listdir('train/' + d) if isfile(join('train', d, f))]
    print(all_files)
    shuffle(all_files)

    ind1 = len(all_files)/10

    for filename in all_files[ : ind1]:
        process_files(filename, val_data, val_labels, val_names)
    for filename in all_files[ind1 : ]:
        if not filename[0].isdigit():
            continue
        if d == 'Type_1':
            process_files(filename, tr_data, tr_labels, tr_names)
            process_files(filename, tr_data, tr_labels, tr_names)
            process_files(filename, tr_data, tr_labels, tr_names)
        elif d == 'Type_2':
            process_files(filename, tr_data, tr_labels, tr_names)
        else: # Type_3
            process_files(filename, tr_data, tr_labels, tr_names)
            process_files(filename, tr_data, tr_labels, tr_names)

    # we will have 3 copy of every samples of Type_1, 1 copy of Type_2,
    #  and 2 copy of Type_3 in the training set.
    # The images in the validation and testing set are unique.


tr = {'data': tr_data, 'labels': tr_labels, 'filename': tr_names}
with open('training_128_dublicated_data.pickle', 'wb') as handle:
    pickle.dump(tr, handle)

val = {'data': val_data, 'labels': val_labels, 'filename': val_names}
with open('validation_128.pickle', 'wb') as handle:
    pickle.dump(val, handle)
