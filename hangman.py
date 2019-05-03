import random
print("Hello Player....")
print("Welocme to Hangman Game...")
while True:
    x = input("Enter the total to which you want to play [Make sure it is a integer > 0]: ")
    try:
        tot = int(x)
        if tot <= 0 :
             raise Exception
        break
    except:
        pass
while True:
    tot_words = input("Enter the number of words you want to guess [Make sure it is a number and is <= {} and > 0]: ".format(tot//3))
    try:
        tot_words = int(tot_words)
        if tot_words <= 0 or tot // tot_words< 3:
            raise Exception
        break
    except:
        pass
f = open('words.txt','rt')
words = []
for p in f:
    gg = p.replace(" ","")
    gg = gg.replace("\n","")
    words.append(gg)
print("Let the guessing start...")
tot_score = 0
no_of_words = 0
while True:
    if tot <= tot_score:
        print("Congrats you won...")
        print("You have taken {} words to acheive the maximum score of {}".format(no_of_words,tot_score))
        print("Your K/D is {}".format(tot_score/no_of_words))
        break
    elif no_of_words >= tot_words:
        print("Max word limit is reached...")
        print("Your score is {}".format(tot_score))
        print("Percentage of maxscore you acheived is {}%".format(tot_score/tot * 100))
        print("Better luck next time...")
        break
    else:
        word = words[random.randint(0, len(words))]
        no_of_words = no_of_words + 1
        score_per_letter = len(word)-1 / 5
        print("Guess the word: {}".format('*'*(len(word))))
        guessed_letters = []
        chances = 0
        temp_word = []
        flag = 0
        while True:
            if chances > 25 :
                print("You have used maximum number of chances per word...")
                break
            else:
                print("You have already guessed the letters: ",end = '')
                for let in guessed_letters:
                    print(let,end='')
                print("")
                let = input("Guess a new letter: ")
                guessed_letters.append(let+" ")
                chances = chances + 1
                new_word = []
                for l in word:
                    if let == l:
                        new_word.append(let)
                        tot_score = tot_score + (score_per_letter / (2**(chances-1)))
                    else:
                        new_word.append('*')
                if flag == 0:
                    for k in range(len(new_word)):
                        temp_word.append(new_word[k])
                    flag = 1
                else:
                    for k in range(len(new_word)):
                        if temp_word[k] == '*' and new_word[k]!='*':
                            temp_word[k] = new_word[k]
                org_word = ""
                for j in temp_word:
                    org_word = org_word + j
                if word == org_word:
                    print("You have guessed it...")
                    print("The word is {}".format(word))
                    break
                else:
                    print("Guess the word: {}".format(str(org_word)))
