def invert(x):
  return x[::-1]

sec = str(input("vertical: "))
pri = str(input("horizontal: "))
gap = int(input("GAP:"))
mis_match = int(input("Mismatch: "))
match = int(input("Match: "))

matriz = [[[0, ""] for i in range(len(pri) + 1)] for a in range(len(sec)+1)]

conuter = 0
for al in range(len(pri) + 1):
    matriz[0][al][0] = conuter
    matriz[0][al][1] = "2"*al
    conuter -= 2

conuter = 0
for ali in range(len(sec)+1):
    matriz[ali][0][0] = conuter
    matriz[ali][0][1] = "3" * ali
    conuter -= 2

indicex = 1
indicey = 1

for alinha in range(((len(sec)+1) * (len(pri) + 1)) - ((len(sec)+1) + len(pri))):
    if indicex == len(pri) + 1:
        indicex = 1
        indicey += 1

    localizacao = matriz[indicey - 1][indicex - 1][1]
    code = ""
    private = 0
    if pri[indicex-1] == sec[indicey-1]:
        maior = matriz[indicey - 1][indicex - 1][0] + match
        code = matriz[indicey - 1][indicex - 1][1] + "1"
        private = 1

    else:
        maior = matriz[indicey - 1][indicex - 1][0] + mis_match
        code = matriz[indicey - 1][indicex - 1][1] + "0"

    if matriz[indicey][indicex - 1][0] + gap >= maior and private==0:
        maior = matriz[indicey][indicex - 1][0] + gap
        code = matriz[indicey][indicex - 1][1] + "2"
    if matriz[indicey - 1][indicex][0] + gap >= maior and private==0:
        maior = matriz[indicey - 1][indicex][0] + gap
        code = matriz[indicey-1][indicex][1] + "3"
    matriz[indicey][indicex][0] = maior
    matriz[indicey][indicex][1] = code

    indicex += 1

print("--------------------------------------------------------------------------------")
print("** valores de score **")
print("================================================================================")
a = len(sec)+1

for imp in range(0,len(sec)+1):
    if a-2 < 0:
        print("- " ,end="")
    else:
        print(F"{sec[a-2]} " ,end="")
    for element in range(0, len(pri)+1):
        print(f"{matriz[a-1][element][0]} " ,end="")
    print("")
    a -= 1

print("x -", end=" ")
for a in pri:
    print(a, end=" ")

backtrace = matriz[-1][-1][1]
score = -99
for al in range(len(pri) + 1):
    if matriz[-1][al][0] >= score:
        score = matriz[-1][al][0]

for ali in range(len(sec)+1):
    if matriz[ali][-1][0] >= score:
        score = matriz[ali][-1][0]

print("\n================================================================================")
print("------------------------------------------------------------------")
print("Maior score :" + str(score))
print(f"Alinhamento: ** Score:{matriz[-1][-1][0]}; Match:{match}; Mismatch:{mis_match}; Gap:{gap}")
print("------------------------------------------------------------------")

segundo = ""
primeiro = ""
s= len(sec) -1
p=len(pri) -1
for back in invert(backtrace).strip():
    match back:
        case "1":
            segundo = sec[s] + segundo
            s-=1
            primeiro = pri[p] + primeiro
            p-=1
        case "0":
            segundo =sec[s] + segundo
            segundo ="-" + segundo
            s-=1
            primeiro ="-" + primeiro
            primeiro =pri[p] + primeiro
            p-=1

        case "3":
            segundo = sec[s] + segundo
            s -= 1
            primeiro ="-" + primeiro

        case "2":
            primeiro = pri[p] + primeiro
            p -= 1
            segundo = "-" + segundo


print(segundo)
print(primeiro+"\n")