class MyHome:
    doorColor = 'red'
    doorState = 'closed'

    def changDoorColor(self, color):
        self.doorColor = color
    def changeDoorState(self, state):
        self.doorState = state
    def showDoor(self):
        print('Door is ', self.doorColor, ' and ', self.doorState)

myhome = MyHome()
myhome.changDoorColor('red')
myhome.changeDoorState('opened')
myhome.showDoor()
