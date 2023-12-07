import subprocess
import multiprocessing
import sys

def throw(exploit_fn, i_start, i_end, n_threads):
    output = subprocess.check_output(['python3', exploit_fn, str(i_start), str(i_end), str(n_threads)])
    print(output)

def main():
    pool = []
    exploit_cnt = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    exploit_fn = "procexploit_crypto.py" if len(sys.argv) > 2 and sys.argv[2] == "crypto" else "procexploit_network.py"
    N_PROCESSES = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    N_THREADS = exploit_cnt // N_PROCESSES
    for i in range(0, exploit_cnt, N_THREADS):
        p = multiprocessing.Process(target=throw, args=(exploit_fn, i, i + N_THREADS, N_THREADS))
        p.start()
        pool.append(p)
    for p in pool:
        p.join()

if __name__ == '__main__':
    main()