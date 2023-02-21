import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# I found it interesting that spacy could make the link between a monkey and a banana

# my example:
word4 = nlp("dog")
word5 = nlp("walk")

print(word4.similarity(word5))


sentence_to_compare ="Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence +" - ",similarity)





''' What I noticed from running "example.py" with a simpler language model:
I noticed that generally the sm model always gave lower results also the small 
model doesn't use word vectors so it won't be as accurate as the larger model
'''