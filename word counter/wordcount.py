total = 1


with open('D:\Code\python projects\word counter\words.txt','r') as f:
    a = f.read()
    for word in a:
        if word == " ":
            total += 1
    print(total)     