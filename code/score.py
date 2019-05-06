import numpy as np
import sys
from nltk.metrics import edit_distance

def accuracy(filepath, num_preds=1, edit_dist=0):
    num_preds = int(num_preds)
    edit_dist = int(edit_dist)
    curr_line = []
    with open(filepath) as f:
        for line in f:
            curr_line.append(line[:-1].split(" "))
    
    #flags = np.array([row[1]==row[2] for row in curr_line])
    flags = [False] * len(curr_line)
    for j, row in enumerate(curr_line):
        for i in range(2, 2+num_preds):
            if row[1] == row[i] or edit_distance(row[1], row[i]) <= edit_dist:
                flags[j] = True
                break

    correct = len(np.where(np.array(flags) == True)[0])
    total = len(flags)
    return (correct/total)

def main(argv):
    args = argv[1:]

    print("Accuracy:", accuracy(args[0], args[1], args[2]))

if __name__ == '__main__':
    sys.exit(main(sys.argv))