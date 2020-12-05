'''
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
'''


ff = open("passports").read()

gg = ff.split('\n\n')
print (len(gg))

fields = "ecl: pid: eyr: hcl: byr: iyr: cid: hgt:".split()

ok = 0
for g in gg:
  num = 0
  for f in fields:
    if f in g:
      num += 1
  if num == 8 or (num == 7 and "cid" not in g):
    ok += 1
print ("ok passports", ok)