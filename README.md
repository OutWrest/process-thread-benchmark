# process-thread-benchmark


To run thread benchmark:

1. Start `python3 service.py`
2. Start `python3 api.py` (in another terminal)
3. Run `time python3 threadexploit.py` (in another terminal)

To run process benchmark:

1. Start `python3 service.py`
2. Run `time python3 procexploit.py` (in another terminal)


## Results

| Targets | Thread (s) | Process (s) |
|---------|------------|-------------|
|  10     |  1.12      | 1.23        |
|  100    |  1.22      | 2.53        |
|  500    |  1.71      | 9.75        |
| 1000    |  2.47      | 18.65       |
