class Airlane:
    def __init__(self, make, model, year, max_speed):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometr = 0
        self.is_flying = False


    def take_off(self):
        self.is_flying = True
        print('{0} {1} Взлетает'.format(self.make, self.model))


    def fly(self, kilometraj):
        self.kilometraj = kilometraj
        self.odometr += kilometraj

    def land(self):
        self.is_flying = False
        print('{0} Приземлился, вы пролетели {1} км'.format(self.make, self.kilometraj))
    
    def read_obometr(self):
        print('Вы пролетели {0} Км'.format(self.odometr))
    
    # samalet1 = input('Введтите Марку самолета: ')
    # model1 = input('Введите модель: ')

samalet = Airlane('Boeing757', '200', '2004', 2500)
samalet.take_off()
samalet.fly(1500)
# samalet.fly(1500)
# samalet.fly(1500)
samalet.land()
samalet.read_obometr()

        
    
    