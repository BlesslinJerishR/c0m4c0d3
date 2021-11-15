def comacoder(lister):
    out = ", "
    out = out.join(lister[0:-1])
    out += f" and {lister[-1]}"
    print(out)


spam = ['apple', 'orange', 'banana', 'grapes']
comacoder(spam)
