import subprocess
import multiprocessing
import sys

def throw(exploit_fn, i):
    output = subprocess.check_output(['python3', exploit_fn, str(i)])
    print(output)

def main():
    pool = []
    exploit_cnt = int(sys.argv[1]) if len(sys.argv) > 0 else 100
    exploit_fn = "procexploit_crypto.py" if len(sys.argv) >= 3 and sys.argv[2] == "crypto" else "procexploit_network.py"
    for i in range(0, exploit_cnt):
        p = multiprocessing.Process(target=throw, args=(exploit_fn, i,))
        p.start()
        pool.append(p)
    for p in pool:
        p.join()

if __name__ == '__main__':
    main()