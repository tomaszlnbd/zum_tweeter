import regex as re

if __name__ == '__main__':
    path = "alltweetsPL.txt"
    data = ""
    with open(path, 'r') as file:
        data = file.read().replace('\n', '')

    tweets = re.findall("text=(.*?)>", data)

    with open('tweets.csv', 'w') as file:
        for x in tweets:
            file.write(x + '\n')
    file = open("tweets.csv")
    numline = len(file.readlines())
    print(numline)