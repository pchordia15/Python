#map
def word_lengths(phrase):
    print list(map(len, phrase.split()))

word_lengths('How long are the words in this phrase')

print("*"*20)

#reduce
def digits_to_num(digits):
    print reduce(lambda x,y: x+10 + y,digits)

digits_to_num([3,4,3,2,1])

print("*"*20)

#filter
def filter_words(word_list, letter):
    print filter(lambda word: word[0]==letter,word_list)

l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')

#zip
def concatenate(L1, L2, connector):
    print [word1+connector+word2 for (word1,word2) in zip(L1,L2)]

concatenate(['A','B'],['a','b'],'-')

print("*"*20)

#enumerate
def d_list(L):   
    print {key:value for value,key in enumerate(L)}

d_list(['a','b','c'])

print("*"*20)

#enumerate
def count_match_index(L):   
    print len([num for count,num in enumerate(L) if num == count])

count_match_index([0,2,2,1,5,5,6,10])