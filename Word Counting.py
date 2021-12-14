import string
text = open("/Users/tianencheng/PycharmProjects/pythonProject/venv/word_count.txt", "r")
dic = dict()
for line in text:

    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))
    words = line.split(" ")
    for word in words:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1

for key in list(dic.keys()):
    print(key, ":", dic[key])