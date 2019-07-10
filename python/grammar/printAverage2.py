class HelloWorld:
    def __init__(self):
        print('Hello World')
    def __del__(self):
        print('Good bye')
    def getAverage(self,var1,var2):
        average = (var1 + var2) / 2
        print('The average is ', average)

def main():
    c1 = HelloWorld()
    score1, score2 = input("Enter two scores separated by a comma: ").split(",")
    c1.getAverage(int(score1),int(score2))

main()
