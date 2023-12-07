from threading import Thread
import sys
import requests

def exploit_network(i):
    url = "http://localhost:9000/exploit/" + str(i)
    response = requests.get(url)
    print(response.text)

def exploit_crypto(n):
    fib = [0, 1]
    for i in range(2, 25000):
        fib.append(fib[i-1] + fib[i-2])
    print("Fibonacci", i, "done at", n)

def main():
    threads = []
    exploit_cnt = int(sys.argv[1]) if len(sys.argv) > 0 else 100
    exploit = exploit_crypto if len(sys.argv) >= 3 and sys.argv[2] == "crypto" else exploit_network
    for i in range(0, exploit_cnt):
        t = Thread(target=exploit, args=(i + 1,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()