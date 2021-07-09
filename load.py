banneord = []
verb = []
pickup= []
global f 
global t
global p
f = open("ordliste_banneord.txt", "r")
for x in f:
  banneord.append(x)
f.close
t = open("ereverb.txt", "r")
for x in t:
  verb.append(x)
t.close
p = open("pickup.txt", "r")
for x in p:
  pickup.append(x)
p.close
print("Load complete")