from abc import ABC, abstractmethod

class Robot(ABC):

    def __init__(self, name, model, power_level):
        self.name = name
        self.model = model
        self.power_level = power_level

    @abstractmethod
    def perform_task(self):
        pass

    def charge(self, tmp):
        if (self.power_level <= 100):
            self.power_level = self.power_level + tmp
        elif (self.power_level <= 0):
            print('Charge the robot!')
        elif(self.power_level > 100):
            print(f"Power level can't be more 100%")
            self.power_level = 100

    def show_info(self):
        print(f'Robot: {self.name}, model: {self.model}, power: {self.power_level}')

class WorkerRobot(Robot):
    def __init__(self, name, model, power_level, tool):
        super().__init__(name, model, power_level)
        self.tool = tool

    def perform_task(self):
        self.power_level = self.power_level - 10
        print(f'Task completed {self.tool}. Power level: {self.power_level}')

    def show_info(self):
        super().show_info()
        print(f'Tool: {self.tool}')

class DefenseRobot(Robot):
    def __init__(self, name, model, power_level, weapon):
        super().__init__(name, model, power_level)
        self.weapon = weapon

    def perform_task(self):
        self.power_level = self.power_level - 15
        print(f'Protection task completed {self.weapon}. Power level: {self.power_level}')

    def show_info(self):
        super().show_info()
        print(f'Tool: {self.weapon}')

class ServiceRobot(Robot):
    def __init__(self, name, model, power_level, service_type):
        super().__init__(name, model, power_level)
        self.service_type = service_type

    def perform_task(self):
        self.power_level = self.power_level - 5
        print(f'Task completed {self.service_type}. Power level: {self.power_level}')

    def show_info(self):
        super().show_info()
        print(f'Tool: {self.service_type}')


objBob = WorkerRobot('Bob', 'X1', 100, 'Wrench')
objDefender = DefenseRobot('Defender', 'Z3', 100, 'Laser')
objHelper = ServiceRobot('Helper', 'S5', 100, 'Cleaning')

objBob.perform_task()
objBob.perform_task()
objBob.perform_task()
objBob.show_info()
tmp = int(input('Введіть рівень заряда: \t'))
objBob.charge(tmp)
objBob.show_info()

objDefender.perform_task()
objDefender.perform_task()
objDefender.perform_task()
objDefender.perform_task()
objDefender.show_info()
tmp = int(input('Введіть рівень заряда: \t'))
objDefender.charge(tmp)
objDefender.show_info()

objHelper.perform_task()
objHelper.perform_task()
objHelper.perform_task()
objHelper.perform_task()
objHelper.perform_task()
objHelper.perform_task()
objHelper.perform_task()
objHelper.perform_task()
objHelper.show_info()
tmp = int(input('Введіть рівень заряда: \t'))
objHelper.charge(tmp)
objHelper.show_info()







