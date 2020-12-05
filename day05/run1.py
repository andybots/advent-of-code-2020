
seats = open("seats").read().split()
#seats = ['FBFBBFFRLR'] # test, MSB to LSB
#seats = ['BBBBBBBRRR'] # B and R are '1', this value is 2^10-1 = 1023

ids = set()
for seat in seats:
  number = 0
  for i in range(10):
    if seat[i] in ["B","R"]:
      number += (2**(10-1-i))
  ids.add(number)
print ("max:", max(ids))

ss = sorted(list(ids))
for i in range(len(ss)-1):
  if ss[i] + 1 != ss[i+1]:
    print ('missing value:',ss[i]+1)
