n = int(input())
office = set()

for _ in range(n):
    name, action = input().split()
    if action == "enter":
        office.add(name)
    elif action == "leave":
        office.discard(name)
        
for name in sorted(office)[::-1]:
    print(name)