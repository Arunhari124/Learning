class Motherboard:
    def __init__(self,motherboard):
        self.motherboard=motherboard

class Cpu:
    def __init__(self,processor):
        self.processor=processor
class Ram:
    def __init__(self,ram):
        self.ram=ram

class Pc:
    def __init__(self,gpu,storage,board,cpu,memory):
        self.gpu=gpu
        self.storage=storage
        self.board=Motherboard(board)
        self.cpu=Cpu(cpu)
        self.memory=[Ram(memory)for mem in range(4)]
    def pc_display(self):
        return f"{self.gpu} {self.storage} {self.board.motherboard} {self.cpu.processor} {self.memory[0].ram}"
        
        
pc1=Pc("rx 580","hdd","H61","i5",12)
print(pc1.pc_display())
        
