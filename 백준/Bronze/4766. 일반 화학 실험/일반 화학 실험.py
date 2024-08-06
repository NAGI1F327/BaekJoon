previous_temperature = None

while True:
    temperature = float(input())
    
    if temperature == 999:
        break
    
    if previous_temperature is not None:
        temperature_change = temperature - previous_temperature
        print(f"{temperature_change:.2f}")
        
    previous_temperature = temperature