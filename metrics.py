from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report

def read_test_file(test_file):
    clss = []
    with open(test_file) as rfile:
        i = 0
        for line in rfile:
            c = line.split("\t")[0]
            clss.append(int(c))
            if i+1 % 100000 == 0:
                print(i)
            i += 1
    return clss

def read_predicted_file(predicted_file):
    clss = []
    with open(predicted_file) as rfile:
        i = 0
        for line in rfile:
            if i == 0:
                i += 1
                continue
            clss.append(int(line))
            if i+1 % 100000 == 0:
                print(i)
            i += 1
    return clss

def get_metrics(y_test, y_predicted):
    # true positives / (true positives+false positives)
    precision = precision_score(y_test, y_predicted, pos_label=None,
                                    average='weighted')
    # true positives / (true positives + false negatives)
    recall = recall_score(y_test, y_predicted, pos_label=None,
                              average='weighted')

    # harmonic mean of precision and recall
    f1 = f1_score(y_test, y_predicted, pos_label=None, average='weighted')

    # true positives + true negatives/ total
    accuracy = accuracy_score(y_test, y_predicted)
    return accuracy, precision, recall, f1

test_file = "../catboost/catboost/app/10000_test.catboost"
predicted_file = "../catboost/catboost/app/output.tsv"

y_test = read_test_file(test_file)
y_predicted = read_predicted_file(predicted_file)

accuracy, precision, recall, f1 = get_metrics(y_test, y_predicted)
print("accuracy = %.3f, precision = %.3f, recall = %.3f, f1 = %.3f" % (accuracy, precision, recall, f1))
