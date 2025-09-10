import socket

HOST = 'alamat_ip_server'  # Ganti dengan IP server
PORT = 9999

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    try:
        while True:
            cmd = input("Masukkan perintah (screenshot/move x y/exit): ")
            client.sendall(cmd.encode())
            if cmd == 'exit':
                break
            data = client.recv(4096)
            if cmd == 'screenshot':
                with open('received_screenshot.png', 'wb') as f:
                    f.write(data)
                print("Screenshot diterima dan disimpan sebagai received_screenshot.png")
            else:
                print(data.decode())
    finally:
        client.close()

if __name__ == "__main__":
    main()
