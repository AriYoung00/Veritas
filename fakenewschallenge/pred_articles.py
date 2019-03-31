# from pred import pred
import numpy as np
import tensorflow as tf
# Import relevant packages and modules
from util import *
import random
import tensorflow as tf
import pickle
import sys

# Prompt for mode
mode = 'load'


# Set file names
file_train_instances = "train_stances.csv"
file_train_bodies = "train_bodies.csv"
file_test_instances = "test_stances_unlabeled.csv"
file_test_bodies = "test_bodies.csv"
file_predictions = 'predictions_test.csv'


# Initialise hyperparameters
r = random.Random()
lim_unigram = 5000
target_size = 4
hidden_size = 100
train_keep_prob = 0.6
l2_alpha = 0.00001
learn_rate = 0.01
clip_ratio = 5
batch_size_train = 500
epochs = 90

sess = tf.Session()

file_test_instances = "test_stances_unlabeled.csv"
file_test_bodies = "test_bodies.csv"

label_ref_rev = {0: 'agree', 1: 'disagree', 2: 'discuss', 3: 'unrelated'}
label_scores = [1, -1, 0.5, 0]
# -*- coding: utf-8 -*-

def writeCSV(headlines, bodyTexts):
	import csv
	headSize = len(headlines)
	bodySize = len(bodyTexts)

	if headSize != bodySize:
		print('headlines and body texts are unequal')
		return 1

	with open(file_test_instances, mode= 'w') as stances:
		stance_writer = csv.writer(stances, delimiter= ',')
		stance_writer.writerow(['Headline', 'Body ID'])
		for i in range(headSize):
			for j in range(bodySize):
				stance_writer.writerow([headlines[i], str(j)])

	with open(file_test_bodies, mode= 'w') as bodies:
		bodies_writer = csv.writer(bodies, delimiter= ',')
		bodies_writer.writerow(['Body ID', 'articleBody'])
		for i in range(bodySize):
			bodies_writer.writerow([str(i), bodyTexts[i]])
	return 0

def predictionOnArticles(headlines, bodyTexts):
    global sess

    writeCSV(headlines, bodyTexts)

    test_pred = []
    
    test_pred = pred(sess)
    test_pred = np.reshape(test_pred, (-1, len(headlines)))

    # test_pred = np.array([[1, 2, 3], [2, 3, 3], [3, 3, 3]])
    raw_scores = np.zeros((0,))
    for i in range(0, test_pred.shape[0]):
        tmp_ct = 0
        tmp_sum = 0
        for j in range(0, test_pred[i].shape[0]):
            cur_val = test_pred[i][j]
            if(cur_val != 3):
                tmp_ct += 1
            tmp_sum += label_scores[cur_val]
#        print(tmp_ct, tmp_sum)
        if(tmp_ct == 0):
            raw_scores = np.append(raw_scores, 0)
        else:
            raw_scores = np.append(raw_scores, tmp_sum/tmp_ct)
    if(max(raw_scores) - min(raw_scores) == 0):
        return raw_scores
    norm_scores = (raw_scores-min(raw_scores))/(max(raw_scores)-min(raw_scores)) * 10  
    return norm_scores

def pred(sess):
    global sess
    # Load data sets
    raw_train = FNCData(file_train_instances, file_train_bodies)
    raw_test = FNCData(file_test_instances, file_test_bodies)
    n_train = len(raw_train.instances)


    # Process data sets
    train_set, train_stances, bow_vectorizer, tfreq_vectorizer, tfidf_vectorizer = \
        pipeline_train(raw_train, raw_test, lim_unigram=lim_unigram)
    feature_size = len(train_set[0])
    test_set = pipeline_test(raw_test, bow_vectorizer, tfreq_vectorizer, tfidf_vectorizer)


    # Define model

    # Create placeholders
    features_pl = tf.placeholder(tf.float32, [None, feature_size], 'features')
    stances_pl = tf.placeholder(tf.int64, [None], 'stances')
    keep_prob_pl = tf.placeholder(tf.float32)

    # Infer batch size
    batch_size = tf.shape(features_pl)[0]

    # Define multi-layer perceptron
    hidden_layer = tf.nn.dropout(tf.nn.relu(tf.contrib.layers.linear(features_pl, hidden_size)), keep_prob=keep_prob_pl)
    logits_flat = tf.nn.dropout(tf.contrib.layers.linear(hidden_layer, target_size), keep_prob=keep_prob_pl)
    logits = tf.reshape(logits_flat, [batch_size, target_size])

    # Define L2 loss
    tf_vars = tf.trainable_variables()
    l2_loss = tf.add_n([tf.nn.l2_loss(v) for v in tf_vars if 'bias' not in v.name]) * l2_alpha

    # Define overall loss
    loss = tf.reduce_sum(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=stances_pl) + l2_loss)

    # Define prediction
    softmaxed_logits = tf.nn.softmax(logits)
    predict = tf.arg_max(softmaxed_logits, 1)

    # Predict
    load_model(sess)
    test_feed_dict = {features_pl: test_set, keep_prob_pl: 1.0}
    test_pred = sess.run(predict, feed_dict=test_feed_dict)

    return test_pred
    # return save_predictions(test_pred, file_predictions)

if __name__ == "__main__":
    # arr1 = ['a', 'b', 'c', 'd', 'e']
    # arr2 = ['1', '2', '3', '4', '5']
    arr1 = pickle.loads(sys.argv[1])
    arr2 = pickle.loads(sys.argv[2])
    res = predictionOnArticles(arr1, arr2)
    print(pickle.dumps(res))

    
