-- Use a recursive tree or a tracing tree to find the time complexity.
T(n) = T(n-1) + f(n)
:
:
Decreasing functions
--------------------
T(n) = T(n-1) + 1 ----- O(n)
T(n) = T(n-1) + n ----- O(n^2)
T(n) = T(n-1) + log n --- O(n logn)
:
:
T(n) = T(n-1) + n^2 --- o(n^3)

No coefficients, just multiply f(n) by n for time complexity.
When you have coefficients:
T(n) = 2 * T(n-1) + 1 ---- O(2^n)
T(n) = 3 * T(n-1) + 1 ---- O(3^n)
:
:
T(n) = 2 * T(n-1) + n ---- O(n * 2^n)

Master theorem for decereasing functions
-------------------------------------------
T(n) = a T(n-b) + f(n), a > 0, b > 0 and f(n) = O(n^k) where k >= 0

If a = 1, T(n) = O(n * f(n))
If a > 1, T(n) = O(f(n) * a^(n/b))
If a < 1, T(n) = O(f(n))

Dividing functions
------------------
T(n) = T(n/2) + 1 --- O(log n)
T(n) = T(n / 2) + n --- O(n)
T(n) = 2 T(n / 2) + n --- O(n log n)

Masters theorem for dividing functions
--------------------------------------
T(n) = a T(n / b) + f(n) a >= 1, b > 1, f(n) = O(n^k log^p n)

Root functions
--------------
T(n)