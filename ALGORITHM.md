# Algorithm for any amount of cats explanation

As far as we need just the result of n loops (n = amount of cats)
of iterating through every first, second, third... up to n-th cat
finding the way to calculate state (presence of hat) of every cat without actually iterating
should be enough and may be more efficient than O(n * log(n)) complexity of brute iterating

I state complexity as O(n * log(n)) assuming that switching operation has complexity O(1) 
asn brute iterating requies n loops with number of iterations in all loops 
equal to n multiplied by sum of first n elements
of harmonic series or 1/1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Pseudocode example:
```python
  for i in range(1, n + 1):     <- n loops
    j = 1
    while j * i <= n:           <- n / i iterations
      switch_hat_on_cat(j * i)  
      j += 1
```

By using the Eulers aproximation of harmonic series we may calculate
approximate total number of iterations is gonna be close to n * (log(n) + γ)
Therefore algorithm's is O(n * log(n))
Where 'γ' is Euler-Mascheroni constant


We know that for every j-th cat it's state is switched on any k-th loop, where k divisor of j
And we know that if there is even number of k's (divisors) for j-th cat
then j-th cat is gonna have no hat in the end because even number of switches will result in preserving initial state (without hat)
If there is odd number of divisors then cat is gonna have a hat after all
For every natural number bigger than 1 there is a set of divisors
every one of which upon dividing the number by it will give us another divisor 
It means that number of such divisors is gonna be always even, unless there is a divisor of the number
which will give itself as a result of division of the number by it
Only one such divisor is possible for any natural number and it exists only if the number is a square of some natural number
Example:
For 32 pairs of divisors are 1 and 32, 2 and 16, 4 and 8
For 36 pairs of divisors are 1 and 36, 2 and 18, 3 and 12, 4 and 9, 6 and 6
Therefore we may calculate and return just №'s of cats which are equal to squares of natural numbers within range from 1 to n
  x = 1
  while x^2 <= n:
    add_cat_number_to_list(x^2)
    x += 1

That algorithm is gonna a number of iterations equal to amount of squares between 2 and n
We may approximate amount of squares in range from a to b using formula:
squares_amount = square_root(b) - square_root(a - 1)
square root of 2 - 1 = 1
So in best case (1 <= n < 4, because there will always be one square - 1) algorithm wil have ony one iteration
O(1)
And in worst case algorithm will do approximately  n^(1/2) - 1 more iterations
O(n^1/2)
