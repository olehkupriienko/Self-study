# здесь пишите программу
class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *memories):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = memories[:self.total_mem_slots]

    def get_config(self):
        result = [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}',
            'Память: ' + ";".join(map(lambda x: f"{x.name} - {x.volume}", self.mem_slots))
        ]
        return result


cpu = CPU('asus', 1333)
mem1, mem2 = Memory('Kingstone', 1000), Memory('Kingstone', 4000)
mb = MotherBoard('Asus', cpu, mem1, mem2)
print(mb.get_config())
