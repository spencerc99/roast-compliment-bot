import re
import nltk
pos_adjs = set([])
neg_adjs = set([])

def preprocess(word):
    return re.sub(r'[0-9]|#', '', word)

with open('./data/inqdict.txt', 'r') as f:
    lines = f.readlines()
    for i in range(1, len(lines)):
        line = lines[i].split()
        # if "Modif" in line and 'JJ' in nltk.pos_tag([line[0]])[0][1]:
        if "Modif" in line:
            if "Pstv" in line or "Pos" in line:
                pos_adjs.add(preprocess(line[0]))
            elif "Ngtv" in line or "Neg" in line:
                neg_adjs.add(preprocess(line[0]))


with open('./data/positive_adjectives.txt', 'w') as f:
    f.writelines(["{}\n".format(pos_adj) for pos_adj in sorted(pos_adjs)])

with open('./data/negative_adjectives.txt', 'w') as f:
    f.writelines(["{}\n".format(neg_adj) for neg_adj in sorted(neg_adjs)])
