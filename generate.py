import random

with open('./data/nouns.txt', 'r') as f:
    nouns = [line.strip() for line in f.readlines()]
with open('./data/positive_adjectives.txt', 'r') as f:
    positive_adjectives = [line.strip() for line in f.readlines()]
with open('./data/negative_adjectives.txt', 'r') as f:
    negative_adjectives = [line.strip() for line in f.readlines()]

def get_noun(num=1):
    copy = list(nouns)
    choices = []
    for i in range(num):
        choice = random.choice(copy)
        copy.remove(choice)
        choices.append(choice)
    return choices

def get_adjective(num=1, neg=False):
    copy = list(negative_adjectives) if neg else list(positive_adjectives)
    choices = []
    for i in range(num):
        choice = random.choice(copy)
        copy.remove(choice)
        choices.append(choice)
    return choices

def generate_compliment():
    # return "Your {} is {}".format(get_noun(), get_adjective(neg=False))
    curr_nouns = get_noun(num=3)
    curr_adjs = get_adjective(num=3)
    return "I still remember the first time I laid eyes on your {} {}. My heart aches every time I see your {} {}. I wanted to let you know that I'm thinking of you, your family, and your {} {}."\
    .format(
        curr_adjs[0],
        curr_nouns[0],
        curr_adjs[1],
        curr_nouns[1],
        curr_adjs[2],
        curr_nouns[2]
    )

def generate_roast():
    curr_nouns = get_noun(num=3)
    curr_adjs = get_adjective(num=3, neg=True)
    return "I still remember the first time I laid eyes on your {} {}. My heart aches every time I see your {} {}. I wanted to let you know that I'm thinking of you, your family, and your {} {}."\
    .format(
        curr_adjs[0],
        curr_nouns[0],
        curr_adjs[1],
        curr_nouns[1],
        curr_adjs[2],
        curr_nouns[2]
    )

for i in range(2):
    print (generate_compliment())
    print (generate_roast())
