file = open("TopScores.txt","r+")

score_text = file.readlines()
print(score_text)
print(len(score_text))
if len(score_text) < 5:
    file.write("TEST\n")

else:
    score_text.pop(4)
    score_text.append('AA 2\n')
    score_text.sort()
    file.close()
    file = open("TopScores.txt", "w")
    file.writelines(score_text)

file.close()


