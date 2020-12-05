'''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm
'''
gg = open("passports").read().split('\n\n')
print ("passports to consider",len(gg))

fields = set("ecl pid eyr hcl byr iyr hgt".split()) # cid

ok = 0
for pass1 in gg[0:]:
  pass2 = pass1.split()
  pass3 = {}
  for p in pass2:
    key,val = p.split(':')
    pass3[key] = val
  numkeys = len(fields.intersection(pass3.keys()))
  if numkeys != 7: # have all of the required fields
    continue

  v = int(pass3['byr'])
  if v < 1920 or v > 2002: continue

  v = int(pass3['iyr'])
  if v < 2010 or v > 2020: continue

  v = int(pass3['eyr'])
  if v < 2020 or v > 2030: continue

  ht = pass3['hgt']
  if ht[-2:] not in ['cm','in']:
    continue

  # height
  if 'cm' in ht:
    ht = ht.strip('cm')
    if int(ht) < 150 or int(ht) > 193:
      continue 
  if 'in' in ht:
    ht = ht.strip('in')
    if int(ht) < 59 or int(ht) > 76:
      continue 

  # hair color
  hcl = pass3['hcl']
  if hcl[0] != '#':
    continue
  hcl = hcl[1:]
  if len(hcl) != 6:
    continue
  for a in '1234567890abcdef':
    hcl = hcl.replace(a,'')
  if len(hcl) != 0:
    continue

  # eye color
  ecl_ok = set("amb blu brn gry grn hzl oth".split())
  e = pass3['ecl']
  if e not in ecl_ok:
    continue

  # passport id
  pid = pass3['pid']
  if len(pid) != 9 or not pid.isnumeric():
    continue

  ok += 1
print ( "number ok", ok)