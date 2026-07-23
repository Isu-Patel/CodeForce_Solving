months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

current = input().strip()
k = int(input())

idx = months.index(current)
print(months[(idx + k) % 12])