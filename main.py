
import random


def gameloop(word):

    tobetrue = True

    mistakes = 10

    correct = []

    wrong = []

    wordLength = int(len(word) - 1)

    print(word)

    print("Word length:", wordLength)

    while mistakes > 0 and tobetrue:
        print("")
        if len(correct) == wordLength:
            print("")
            print("You won")
            tobetrue = False

        else:
            for l in word:
                if l in correct:
                    print(l, end="")
                else:
                    print("_", end="_")

            print("wrong:", len(wrong), wrong, "  Mstakes remaining:", mistakes)

            letter = str(input("Give a letter: "))

            if letter in wrong or letter in correct:
                print("You already used that letter")

            elif letter in word:
                for lt in word:
                    if lt == letter:
                        correct.append(letter)

            else:
                wrong.append(letter)
                mistakes -= 1

        if mistakes <= 0:
            print("")
            print("You lost")


# ----INITIALIZE_WORDLIST---- #
wordlist = []

with open("wordlist.txt", 'r') as f:
    for line in f:
        wordlist.append(line)

worldlistLength = int(len(wordlist))

# ----WORD_PICKER--- #

word = str(random.choice(wordlist))

if __name__ == '__main__':
    gameloop(word)
