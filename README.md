# Welcome to the Tests training  
## Demos  
### Unit performance tests using timeit  
For the purpose of this demo we will compare several sort algorithms using timeit
#### Prerequisites:
* Python installed
#### Timeit
timeit will measure the time spent to execute some statements.
We will use repeat method from timeit
```
times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=1)
```
Timeit measure the time spent to run `stmt` executed `number` times.  
repeat method runs it `repeat` times and return an array of measured time.

#### Measuring performances
`perfo/perfo.py` contains the code to run and measure the sorting algorithm.  
The sorting algorithm are defined in `simple/sort.py`. You can define your own and test it

#### Work to do
- Define some test cases
  - array is already sorted (1, 3, 5, 9, 11)
  - array is already sorted but the min value is at the end (3, 5, 9, 11, 1)
  - array is sorted but in reversed order (11, 9, 5, 3, 1)
- For each of those determine which algorithm is the better for 10 000 values

