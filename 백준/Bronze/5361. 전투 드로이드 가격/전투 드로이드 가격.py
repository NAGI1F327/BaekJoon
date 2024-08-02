prices = {
    'Blaster_Rifle': 350.34, 'Visual_Sensor': 230.90, 'Audio_Sensor': 190.55, 'Arms': 125.30, 'Legs': 180.90
}

num_cases = int(input())

for _ in range(num_cases):
    A, B, C, D, E = map(int, input().split())
    
    total_cost = (
        A * prices['Blaster_Rifle'] + B * prices['Visual_Sensor'] + C * prices['Audio_Sensor'] + D * prices['Arms'] + E * prices['Legs']
    )
    
    print(f"${total_cost:.2f}")