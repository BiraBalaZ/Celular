from lib.devices import Smartwatch

smartwatch = Smartwatch()

# Initial state: off and without battery
assert smartwatch.is_powered() == False
assert smartwatch.get_charge() == 0

# Try to turn on the smartwatch with insufficient battery
assert smartwatch.power_on() == 'Not enough charge'

# Charging battery
assert smartwatch.charge_battery() == 'Charging'
assert smartwatch.get_charge() == 1

# Try to turn on the smartwatch with insufficient battery
assert smartwatch.power_on() == 'Not enough charge'

# Charge the smartwatch until 100%
assert smartwatch.charge_battery(99) == 'Charging'
assert smartwatch.get_charge() == 100

# Try to charge the smartwatch with full battery
assert smartwatch.charge_battery() == 'Already charged'

# Try to turn on the smartwatch with full battery
assert smartwatch.power_on() == 'Powered on'
assert smartwatch.is_powered() == True

# Try to turn on a smartwatch that is already on
assert smartwatch.power_on() == 'Already powered on'

# Try to turn off a smartwatch that is on
assert smartwatch.power_off() == 'Powered off'
assert smartwatch.is_powered() == False

# Play a game called 'Snake', which consumes 3% of the battery
assert smartwatch.play_game('Snake') == 'Playing game: Snake'
assert smartwatch.get_charge() == 97

# It consumes 1% of the battery
assert smartwatch.discharge_battery() == 'Discharging'
assert smartwatch.get_charge() == 96

# Discharge the smartwatch until it reaches 7%
assert smartwatch.discharge_battery(89) == 'Discharging'
assert smartwatch.get_charge() == 7

# Play Snake again and the smartwatch turns off because it is below 5%
assert smartwatch.play_game('Snake') == 'Powering off'
assert smartwatch.is_powered() == False
assert smartwatch.get_charge() == 4

# Try to turn off the smartwatch, but it is already off
assert smartwatch.power_off() == 'Already powered off'

# Try to turn on the smartwatch with insufficient battery
assert smartwatch.power_on() == 'Not enough charge'

# Charge just enough to turn on the smartwatch
assert smartwatch.charge_battery(1) == 'Charging'
assert smartwatch.get_charge() == 5

# Try to turn on with minimal charge
assert smartwatch.power_on() == 'Powered on'

# Let the smartwatch consume 1% of battery, triggering the power off
assert smartwatch.discharge_battery() == 'Powering off'

print("Smartphone passed all tests! :)")