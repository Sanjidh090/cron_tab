import matplotlib.pyplot as plt
import numpy as np
import schemdraw
import schemdraw.elements as elm

def bjt_thermal_runaway_simulation(temp_range, initial_Ic, thermal_coefficient):
    """
    Simulates the effect of temperature increase on collector current (Ic) due to thermal runaway.
    
    temp_range: Array of temperature values (°C)
    initial_Ic: Initial collector current at room temperature (A)
    thermal_coefficient: Change in Ic per degree Celsius
    """
    
    # Simulating increase in Ic with temperature
    Ic_values = initial_Ic * np.exp(thermal_coefficient * (temp_range - 25))
    
    plt.figure(figsize=(8, 5))
    plt.plot(temp_range, Ic_values, label='Collector Current (Ic)', color='red')
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Collector Current (A)")
    plt.title("Thermal Runaway in BJT")
    plt.axhline(y=initial_Ic, linestyle='--', color='blue', label='Initial Ic')
    plt.legend()
    plt.grid(True)
    plt.show()
    
# Parameters for simulation
temp_range = np.linspace(25, 150, 100)  # Temperature from 25°C to 150°C
initial_Ic = 0.01  # Initial collector current (10mA)
thermal_coefficient = 0.01  # Example coefficient for Ic increase per °C

# Run simulation
bjt_thermal_runaway_simulation(temp_range, initial_Ic, thermal_coefficient)

# Draw Realistic Circuit Diagram
d = schemdraw.Drawing()
d.add(elm.BatteryCell().label('Vcc'))
d.add(elm.Line().down().length(0.5))
d.add(elm.Resistor().down().label('Rc'))
d.add(elm.Line().down().length(0.5))
transistor = d.add(elm.BjtNpn().right().label('Q1'))  # Corrected transistor component
d.add(elm.Line().down().length(0.5))
d.add(elm.Resistor().down().label('Re'))
d.add(elm.Ground())

d.add(elm.Line().left().at(transistor.collector).length(0.5))  # Corrected connection point
d.add(elm.Resistor().left().label('Rb1'))
d.add(elm.Line().down().length(0.5))
d.add(elm.Resistor().down().label('Rb2'))
d.add(elm.Ground())

d.draw()
