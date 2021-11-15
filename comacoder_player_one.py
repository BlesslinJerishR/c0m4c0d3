def comacoder(lister):
    out = ", "
    out = out.join(lister[0:-1])
    out += f" and {lister[-1]}"
    print(out)


spam = list()
n = int(input("Yo got how many items ? "))
for n in range(n):
    li = str(input(f"Yo Give me the {n+1} name : "))
    spam.append(li)

# Player Driver Code
comacoder(spam)
