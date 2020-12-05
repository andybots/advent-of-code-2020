

'''
5-7 s: bwkbdlwns
14-17 v: vvvvvvvvvvvvvpvvxv
4-5 v: mvkvvn
2-5 h: lcwghhkpkxvzkvrmxrv
'''
valid1, valid2 = 0, 0
for ff in open("passwords"):
  gg = ff.replace('-',' ').replace(':','').split()
  lo, hi, let, pw = int(gg[0]), int(gg[1]), gg[2], gg[3]

  # Part 1
  filter_pw = gg[3].replace(let,'')
  delta = len(pw) - len(filter_pw)
  if delta >= lo and delta <= hi:
    valid1 += 1

  # Part 2
  if pw[lo-1:lo] == let and pw[hi-1:hi] != let:
    valid2 += 1
  if pw[lo-1:lo] != let and pw[hi-1:hi] == let:
    valid2 += 1
    
print "Part 1 valid:", valid1
print "Part 2 valid:", valid2
