import math

mb = input()
bc = input()

hyp= math.sqrt(mb**2 + bc**2)
hyp = hyp/ 2.0
adj = bc / 2.0
print str(int(round(math.degrees(math.acos(adj/hyp))))) + "°"