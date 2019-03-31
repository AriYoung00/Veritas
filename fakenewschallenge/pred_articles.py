# from pred import pred
import numpy as np
file_train_instances = "train_stances.csv"
file_train_bodies = "train_bodies.csv"
file_predictions = 'predictions_test.csv'

label_ref_rev = {0: 'agree', 1: 'disagree', 2: 'discuss', 3: 'unrelated'}
label_scores = [1, -1, 0.5, 0]
def predictionOnArticles(headlines, bodyTexts):
    generateCSVs(headlines, bodyTexts)
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
        print(tmp_ct, tmp_sum)
        if(tmp_ct == 0):
            raw_scores = np.append(raw_scores, 0)
        else:
            raw_scores = np.append(raw_scores, tmp_sum/tmp_ct)
                
    norm_scores = (raw_scores-min(raw_scores))/(max(raw_scores)-min(raw_scores)) * 10  
    return norm_scores

if __name__ == "__main__":
    predictionOnArticles([], [])