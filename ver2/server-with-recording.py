import socket
with socket.socket() as s:
    s.bind(('',8000))
    s.listen(1)
    with s.accept()[0] as c:
        chunks = []
        while True:
            chunk = c.recv(4096)
            if not chunk: break
            chunks.append(chunk)
    with open('server-out.wav','wb') as f:
        f.write(b''.join(chunks))
