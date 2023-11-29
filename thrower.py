import subprocess
import multiprocessing

def throw(i):
    output = subprocess.check_output(['python3', 'procexploit.py', str(i)])
    print(output)



def main():
    pool = []
    for i in range(0, 1000):
        p = multiprocessing.Process(target=throw, args=(i,))
        p.daemon = True
        p.start()
        pool.append(p)
    for p in pool:
        p.join()

if __name__ == '__main__':
    main()