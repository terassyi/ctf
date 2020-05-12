
def solve():
    x = 1
    while True:
        ans = x * 1584891 + 32134 
        if ans % 3438478 == 193127:
            print(ans)
            return
        x += 1

def main():
    solve()

if __name__ == '__main__':
    main()
