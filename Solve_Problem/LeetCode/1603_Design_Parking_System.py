class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.options = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        # inputs are 1 or 2 or 3
        if self.options[carType-1] > 0:
            self.options[carType-1] -= 1
            return True
        else:
            return False

# class ParkingSystem:
#     def __init__(self, big: int, medium: int, small: int):
#         self.big_space = big
#         self.med_space = medium
#         self.sma_space = small
#
#     def addCar(self, carType: int) -> bool:
#         if carType == 1:
#             if self.big_space < 1:
#                 return False
#             self.big_space -= 1
#         elif carType == 2:
#             if self.med_space < 1:
#                 return False
#             self.med_space -= 1
#         else:
#             if self.sma_space < 1:
#                 return False
#             self.sma_space -= 1
#         return True

obj = ParkingSystem(1, 1, 1)
param_1 = obj.addCar(1)
param_2 = obj.addCar(2)
param_3 = obj.addCar(3)
param_4 = obj.addCar(1)
print([param_1, param_2, param_3, param_4])
