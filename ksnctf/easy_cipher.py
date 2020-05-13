message = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT"

flag = "SYNTFjmtkOWFNZdjkkNH"
key = ord("S") - ord("F")

def rot(s, k):
    ss = ""
    for c in s:
        c_num = ord(c)
        if 65 <= c_num & c_num <= 90:
            if 90 < c_num + k:
                ss += chr(c_num - k)
            else:
                ss += chr(c_num + k)
        elif 97 <= c_num & c_num <= 122:
            if 122 < c_num + k:
                ss += chr(c_num - k)
            else:
                ss += chr(c_num + k)
        else:
            ss += chr(c_num - 25)
    return ss

def solve(s):
    s_lis = s.split()
    decoded = []
    for a in s_lis:
        decoded.append(rot(a, key))
    ans = ""
    for a in decoded:
        ans += a
        ans += " "
    print(ans)

def main():
    solve(message)

if __name__ == "__main__":
    main()

