import socket
import threading
import json

HEADER = 64
PORT = 5051
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
sorted_marks = []
send_arr = []
best_four = []
fail_count = 0


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()

def sortRowWise(m):
    
    for i in range(len(m)):
         
        for j in range(len(m[i])):
             
            for k in range(len(m[i]) - j - 1):
                 
                if (m[i][k] > m[i][k + 1]):
                     
                    t = m[i][k]
                    m[i][k] = m[i][k + 1]
                    m[i][k + 1] = t
                    
    for i in range(len(m)):
        for j in range(len(m[i])):
            #print(m[i][j], end=" ")
            if j == 2:
                sorted_marks.insert(i, m[i][j])
        #print("\n")
    return sorted_marks


def checkPF():
    total_avg = sum(sorted_marks) / len(sorted_marks)
    for i in sorted_marks:
        if i < 50:
            global fail_count
            fail_count += 1
            if fail_count >= 6:
                send_arr.insert(0, total_avg)
                send_arr.insert(1, "with 6 or more Fails! DOES NOT QUALIFY FOR HONORS STUDY!")
                conn.send(json.dumps(send_arr).encode())

def Average():
    avg_best_eight = 0
    sorted_marks.sort(reverse=True)
    best_four = sorted_marks[:8]
    avg_best_eight = sum(best_four) / len(best_four)
    total_avg = sum(sorted_marks) / len(sorted_marks)

    if avg_best_eight >= 70:
        send_arr.insert(0, avg_best_eight)
        send_arr.insert(1, "QUALIFIED FOR HONOURS STUDY!")
        print(*send_arr)
        conn.send(json.dumps(send_arr).encode())
    elif avg_best_eight < 70 and avg_best_eight >= 65 and total_avg > 80:
        send_arr.insert(0, avg_best_eight)
        send_arr.insert(1, "MAY HAVE GOOD CHANCE! Need further assessment!")
        print(*send_arr)
        conn.send(json.dumps(send_arr).encode())
    elif avg_best_eight < 65 and avg_best_eight >= 60 and total_avg > 80:
        send_arr.insert(0, avg_best_eight)
        send_arr.insert(1, "MAY HAVE A CHANCE! Must be carefully reassessed and get the coordinator’s permission!")
        print(*send_arr)
        conn.send(json.dumps(send_arr).encode())
    else:
        send_arr.insert(0, avg_best_eight)
        send_arr.insert(1, "DOES NOT QUALIFY FOR HONORS STUDY!")
        print(*send_arr)
        conn.send(json.dumps(send_arr).encode())
        

print(f"[SERVER STARTED] Local IP address of this server is : {SERVER}")
while True:
    conn, addr = server.accept()
    print(f"[NEW CONNECTION] {addr} connected.")

    json_marks_arr = conn.recv(1024).decode()
    marks_arr = json.loads(json_marks_arr)

    sortRowWise(marks_arr)
    print("\n")
    checkPF()
    Average()
    print("\n")
    print(f"[SERVER] Results were sent back to {addr}.")
    
    conn.close()
    
