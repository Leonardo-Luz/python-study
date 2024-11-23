import random 

def guessNum(min, max, tries): 
    toGuess = random.randint(min, max);

    def isCorrectGuess():
        try:
            myGuess = int(input('Digite um número entre ' + str(min) + ' e ' + str(max) + ': '))
            if myGuess < toGuess:
                print('O número deve ser maior')
            elif int(myGuess) > toGuess:
                print('O número deve ser menor')

            return toGuess == myGuess
        except:
            print('Input inválido')

    for i in range(tries):
        if isCorrectGuess(): 
            print('Você acertou em ' + str(tries) + ' tentativas!')
            return

    print('Você errou, o número correto era: ' + str(toGuess) + ' :(')

guessNum(1, 10, 5)
