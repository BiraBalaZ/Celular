from datetime import date

class BatteryDevice():
    ligado = False
    charge = 0

    def is_powered(self):
        return self.ligado

    def get_charge(self):
        return self.charge

    def power_on(self):
        if (self.charge < 5):
            return 'Not enough charge'
        elif (self.charge == 5 or (self.charge > 5)):
            if (self.ligado == False):
                self.ligado = True
            elif (self.ligado == True):
                return 'Already powered on'
            return 'Powered on'
                
    def power_off(self):
        if (self.ligado == False):
            return 'Already powered off'
        else:
            self.ligado = False
            return 'Powered off'

    def charge_battery(self, value=1):
        if (self.charge < 100):
            self.charge += value
            return 'Charging'
        elif (self.charge == 100):
            return 'Already charged'

    def discharge_battery(self, value=1):
            self.charge -= value
            if (self.charge < 5):
                self.ligado = False
                return 'Powering off'
            else:
                return 'Discharging'

class Smartphone(BatteryDevice):

    def play_game(self, game):
        self.charge -= 3
        if (self.charge <= 5):
            self.ligado = False
            return 'Powering off'
        else:
            return f'Playing game: {game}'

class Smartwatch(BatteryDevice):
    
    def display_time(self):
        self.charge -= 3
        if (self.charge <= 5):
            self.ligado = False
            return 'Powering off'
        else:
            return f'ALARM'