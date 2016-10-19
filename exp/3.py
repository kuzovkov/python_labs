string='-175.4563'
print float(string) + 10
print type(string)

a=['-184.8431', '-207.1685', '-240.8842', '-282.4806', '-335.0023', '-390.5584', '-446.7879', '-502.3442', '-551.2256']


for i in range(len(a)):
    a[i]=float(a[i])
    print a[i]

print "-"*60
for i in range(len(a)):
    print a[i] + 100

