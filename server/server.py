import socket
import pyautogui

HOST = '0.0.0.0'  # Dengarkan di semua interface
PORT = 9999

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Menunggu koneksi di {HOST}:{PORT}...")

    conn, addr = server.accept()
    print(f"Terhubung dengan {addr}")

    try:
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print(f"Perintah diterima: {data}")

            if data == 'screenshot':
                screenshot = pyautogui.screenshot()
                screenshot.save('screenshot.png')
                with open('screenshot.png', 'rb') as f:
                    img_data = f.read()
                conn.sendall(img_data)
            elif data.startswith('move'):
                try:
                    _, x, y = data.split()
                    pyautogui.moveTo(int(x), int(y))
                    conn.sendall(b'OK')
                except Exception as e:
                    conn.sendall(f'Error: {e}'.encode())
            elif data == 'exit':
                break
            else:
                conn.sendall(b'Perintah tidak dikenali')
    finally:
        conn.close()
        server.close()

if __name__ == "__main__":
    main()
