

# part 1
nnn = open('numbers').read().split()
nn = [int(n) for n in nnn]
nn.sort()
nset = set(nn)
#print (nn)

for n in nn:
  if (2020-n) in nset:
    print (n, "answer for part 1 is --> ", n*(2020-n))


# part 2
for n in nn:
  for m in nn:
    if (2020-n-m) in nset:
      print (n, "answer for part 2 is --> ", n*m*(2020-n-m))
