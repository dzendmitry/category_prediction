
inFile="/Users/dzendmitry/dev/lab/liblinear-multicore-2.20/osx_amd64_openmp_bin/1000000_train.svm"
outFile="1000000_train.catboost"

with open(outFile, 'w') as wfile:
    with open(inFile) as rfile:
        i = 0
        for line in rfile:
            l = line.split(" ")
            c = int(l[0])-1
            attrs = [elem.split(":")[1].strip() for elem in l[1:]]
            attrs_line = "\t".join(attrs)
            wfile.write("{}\t{}\n".format(c, attrs_line))
            if i % 100000 == 0:
                print(i)
            i += 1
