# Benchmark

This is a pretty simple benchmark. From root directory, run: `python3 benchmark/run.py [number_circles]`. Default number of circles is 1000.

Some (non-rigorous) results:

|   Number  |  Time (s) |
|-----------|-----------|
| 10        | 0.0090    |
| 100       | 0.018     |
| 1,000     | 0.32      |
| 10,000    | 9.95      |
| 100,000   | 318       |

Some (non-rigorous) results from D3:
|   Number    |  Time (s) |
|-------------|-----------|
| 10          | 0.001     |
| 100         | 0.004     |
| 1,000       | 0.009     |
| 10,000      | 0.24      |
| 100,000     | 7.21      |

D3 is clearly much faster! So why do I use `npcirclepack`? Because I only have to run it once in the backend, where I don't care nearly so much about the speed, since I don't have to build a responsive application off this code. Still, there is clearly room for improvement in this library.