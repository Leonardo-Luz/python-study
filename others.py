

# NOTE: Verifies if the code isnt running as an library
def isRunning():
    return __name__ == '__main__'

val1 = 5
val2 = 'teste'

print(f'Val1 -> {val1} Val2 -> {val2}')
