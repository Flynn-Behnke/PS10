#1
lastname = ["Smith", "Steve", "John", "Garza", "Bob", "Maya", "Bill", "Trevor", "Troy", "Lilly"]

def displayname(lastname):
  l = len(lastname)
  for i in range (0, l, 1):
    print(lastname[i])
displayname(lastname)
print()
def reversename(lastname):
  l = len(lastname)
  lastname.reverse()
  for i in range (0, l, 1):
    print(lastname[i])
reversename(lastname)

#2
grade = [80, 65, 73, 79, 20, 98, 65, 87, 76, 92]
def printnamegrade(lastname, grade):
  l = len(grade)
  for i in range (0, l, 1):
    print(lastname[i], grade[i])

print()
printnamegrade(lastname, grade)

#3
print()
f=open("lnames.txt", "r")
lastname = f.readline()

lastn = []
score = []

while lastname != "":
  lastn.append(str(lastname).rstrip("\n")) 
  score.append(float(f.readline()))
  lastname = f.readline()
f.close()
 
def hilow(score):
  
  hscore = 0
  lscore = 999999999
  l = len(score)
  for y in range(0, l, 1):
    if float(score[y]) > float(hscore):
      hscore = score[y]
      hindex = y
  for x in range(0, l, 1):
    if float(score[x]) < float(lscore):
      lscore = score[x]
      lindex = x

  print("Lowest score:", lastn[lindex], score[lindex])
  print("Highest score:", lastn[hindex], score[hindex])

hilow(score)

#4/5
t = open("batter.txt", "r")
batname = t.readline()
batn = []
batav = []

while batname != "":
  batn.append(str(batname).rstrip("\n"))
  batav.append(float(t.readline()))
  batname = t.readline()
t.close

print()
def displaybat(batn, batav):
  p = len(batn)
  for i in range (0, p, 1):
    print(batn[i], "batting average:", batav[i])

displaybat(batn, batav)
print()

def batsearch(batn, batav):
  p = len(batn)
  sindex = -1
  for s in range (0, p, 1):
    if batn[s] == sname:
      sindex = s
  return sindex

gate = str(input("Would you like to run this program? Yes or No?: "))
while gate == "Yes":
  sname = str(input("Enter batter name to search: "))
  sindex = batsearch(batn, batav)
  if sindex == -1:
    print("Batter not found")
  else:
    print(batn[sindex], "batting average:", batav[sindex])
    
  gate = str(input("Would you like to run this program again? Yes or No?: "))

print("Have a good day :)")
