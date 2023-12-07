# process-thread-benchmark


To run thread benchmark:

1. Start `python3 service.py`
2. Start `python3 api.py` (in another terminal)
3. Run `time python3 threadexploit.py` (in another terminal)

To run process benchmark:

1. Start `python3 service.py`
2. Run `time python3 procexploit.py` (in another terminal)


## Results

### Network-bound tasks

| Targets | Single-process multi-threaded (s) | Multi-process single-threaded (s) | Multi-process multi-threaded (s) |
|---------|-----------------------------------|-----------------------------------|----------------------------------|
| 10      | 1.238                             | 1.456                             | 1.461                            |
| 100     | 1.388                             | 3.619                             | 1.522                            |
| 500     | 2.564                             | 12.912                            | 1.685                            |
| 1000    | 2.623                             | 26.605                            | 1.890                            |

### CPU-bound tasks

| Targets | Single-process multi-threaded (s) | Multi-process single-threaded (s) | Multi-process multi-threaded (s) |
|---------|-----------------------------------|-----------------------------------|----------------------------------|
| 10      | 0.462                             | 0.254                             | 0.280                            |
| 100     | 2.177                             | 1.320                             | 0.610                            |
| 500     | 10.147                            | 5.860                             | 2.108                            |
| 1000    | 29.911                            | 10.308                            | 3.834                            |

## Limitations

OS can only create so many processes or threads (check `ulimit -n`):
```
Traceback (most recent call last):
  File "/usr/lib/python3.10/multiprocessing/process.py", line 314, in _bootstrap
    self.run()
  File "/usr/lib/python3.10/multiprocessing/process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "/mnt/c/Users/salahabbas/Downloads/process-thread-benchmark/multiprocess-singlethread/thrower.py", line 6, in throw
    output = subprocess.check_output(['python3', exploit_fn, str(i)])
  File "/usr/lib/python3.10/subprocess.py", line 421, in check_output
    return run(*popenargs, stdout=PIPE, timeout=timeout, check=True,
  File "/usr/lib/python3.10/subprocess.py", line 503, in run
    with Popen(*popenargs, **kwargs) as process:
  File "/usr/lib/python3.10/subprocess.py", line 971, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/usr/lib/python3.10/subprocess.py", line 1762, in _execute_child
    errpipe_read, errpipe_write = os.pipe()
OSError: [Errno 24] Too many open files
```