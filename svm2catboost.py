
inFile="TRAIN_data_out_model_full_cbow_v1.svm"
outFile="TRAIN_data_out_model_full_cbow_v1.catboost"

with open(outFile, 'w') as wfile:
    with open(inFile) as rfile:
        i = 0
        for line in rfile:
            l = line.split(" ")
            c = l[0]
            attrs = [elem.split(":")[1].strip() for elem in l[1:]]
            attrs_line = "\t".join(attrs)
            wfile.write("{}\t{}\n".format(c, attrs_line))
            if i % 100000 == 0:
                print(i)
            i += 1