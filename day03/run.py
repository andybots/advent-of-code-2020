
ff = open("trees").read().strip().split()

w = len(ff[0])
print (w)

print ff[0][2]

cases = [[1,1],[3,1],[5,1],[7,1],[1,2]]

mult = 1

for case in cases:
  xstep, ystep = case
  trees = 0
  loc = 0
  for i in range(0,len(ff),ystep):
    if ff[i][loc] == "#":
      trees += 1
    loc = (loc + xstep) % w

  print "trees:",trees, "for case", case
  mult *= trees
print "total mult", mult