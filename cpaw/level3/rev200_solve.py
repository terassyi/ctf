
def solve():
    var_78h = ['z', 'i', 'x', 'n', 'b', 'o', '|', 'k', 'w', 'x', 't', '8', '8', 'd']
    var_40h = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    var_80h = 0
    ebp_0x78 = 0
    ebp_0x40 = 0
    var_7ch = 25
    while var_80h !=  14:
        eax = var_80h
        eax = var_78h[ebp_0x78 + eax]
        eax = chr(ord(eax) ^ var_7ch)
        edx = eax
        eax = var_80h
        var_40h[ebp_0x40 + eax] = edx
        var_80h += 1
    flag = ""
    for c in var_40h:
        flag += c
    print(flag)

def main():
    solve()


main()
