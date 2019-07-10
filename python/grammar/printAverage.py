def main():
    print('Hello world')
    print('This computes the average of two scores.')

    score1, score2 = input("Write two numbers separated by a comma: ").split(",")
    average = (int(score1)+int(score2)) / 2.0

    print('The average is : ', average)

main()
