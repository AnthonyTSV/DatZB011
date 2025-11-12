class Pacients():
    def __init__(self, vards, vecums, temperatura):
        self.vards = vards
        self.vecums = vecums
        self.temperatura = temperatura
        self.temperatura_pedeja = temperatura[-1]
           
    def __str__(self):
        report = "Ziņojums par pacientu: {}\n" \
        "Pacienta vecums: {}\n" \
        "Pēdējā mērītā temp.: {} C\n".format(
            self.vards,
            self.vecums,
            self.temperatura_pedeja
            )
        
        return report
       
    def vai_vesels(self):
        for temp in self.temperatura:
            if temp > 38:
                return False
        return True

class MaksasPacients(Pacients):
    def __init__(self, vards, vecums, temperatura, rekins, samaksats):
        super().__init__(vards, vecums, temperatura)
        self.rekins = rekins
        self.samaksats = samaksats
