###### 最大公约数

```c++
int gcd(int a, int b) {
    // a < b
    int r;
    while (b % a) {
        r = b % a;
    	b = a;
        a = r;
    }
    return a;
}
```

###### 快速幂

```c++

```

###### 素数

```c++
bool isPrime(int n) {
    if (n <= 1) return false;
    int sqr = (int)sqrt(1.0 * n);
    for (int i = 2; i <= n; i++)
        if (n % i == 0)
            return false;
    return true;
}
bool find_price() {
    for (int i = 1; i < maxn; i++) {
        if (isPrime(i)) {
            ...
        }
    }
}
```

