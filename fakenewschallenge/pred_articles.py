from pred import pred
import numpy as np
from pred import pred
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
    writeCSV(headlines, bodyTexts)
    test_pred = pred()

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

if __name__ == "__main__":
    # arr1 = ['a', 'b', 'c', 'd', 'e']
    # arr2 = ['1', '2', '3', '4', '5']
    arr1 = ['What First Responders Don’t Know About Fiery Electric Vehicles',]
    arr2 = ['After an out-of-control Tesla Model S plowed into a stand of palm trees on a highway median outside Fort Lauderdale last month, police rushed to put out the ensuing blaze using a department-issued fire extinguisher. It was a wasted effort. The car kept on burning after the crash, which killed the driver.The police may not have known lithium-ion batteries inside electric vehicles, once ignited, can’t be put out with chemicals from a conventional extinguisher. The battery fires are susceptible to a self-destructive chain reaction known as thermal runaway, causing a feedback loop of rising temperatures. The Tesla fire stumped a series of first responders in Florida. Firefighters eventually doused the flames with water, which seemed to work, but the wrecked car reignited twice more after being towed away. That prompted what a police report later termed “extraordinary measures,” including a call to Broward County’s hazmat unit for advice on stamping out the fire once and for all.',]
    print(predictionOnArticles(arr1, arr2))
