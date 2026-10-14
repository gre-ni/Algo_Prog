# Ukol: Casova slozitost

_Nikol Greplova_

## 1. Vypocet slozitosti

#### (1)

```
n = int(input())    # 2
if n % 2 == 0:      # 2 operace + truth check
    print('even')   # 1
else:
    print('odd')
```

**-> $O(1)$** v konstantnim case. Pro jakykoli vstup je stejny pocet kroku + u obou vetvi je stejna operace, takze nejhorsi i nejlepsi pripad by mel vychazet stejne.

#### (2)

```
n = int(input())
x = 1
for i in range(n): # n + 1
    for j in range(i): # triangular, loops n(n - 1) / 2
        x = 1 - x # same as above minus one truth check
print(x)
```

-> $O(n^2)$

- Vnejsi cyklus je n kroku
- Vnoreny cyklus se opakuje 1x,2x,3x... tzn. celkova suma kroku bude $n(n - 1) / 2$

#### (3)

```
n = int(input())
i = 1
while i < n: # exponential
    print('hello')
    i *= 3 # 3^0, 3^1, 3^3 etc...
```

-> $O(\log{n})$

- i bude rust mnohem rychleji nez n, prvni loop 3, pak 3\*3, ...potka n v nejake hodnote $3^k$
- Aby se cyklus zastavil, $n \geq 3^k$, z toho vyvodime hranicni k hodnotu $\log_3{n}$, po odebrani konstanty log n

#### (4)

```
n = int(input())
s = 1
for i in range(n):
    for j in range(n):
        for k in range(n):
            s += 1 # n * n * n
        s *= 2 # n * n
    for l in range(n):
        s -= 1 # n * n
    s //= 10 # n
print(s)
```

-> $O(n^3)$

- Celkovy pocet polynomu (cca) je $n^3 + 2n^2 + n$, nejvyssi clen je $n^3$

#### (5)

```
n = int(input())
w = 1
while n > 0: # ekvivalent i = n; i > 0; i=i/2
    for x in range(n):
        w = (w * 31) % 2**16
    n //= 2 # log n
```

-> $O(n)$

- Vnejsi loop: od n do 0, po krocich n = n // 2 -> v podstate totez jako pocitat smerem nahoru a nasobit \* 2, tj. exponencialni, log n
- Aby se potkala stop condition: $\frac{n}{2^k} = 0$ -> $n = 2^k$ -> $\log_2{n}$
- Vnitrni cyklus je zavisly na menicim se n taky, kde reprezentuje pocet operaci kazdeho pruchodu, tj. $n + \frac{n}{2} + \frac{n}{4} + ... + \frac{n}{2^k}$ -> suma tohoto bude mene nez 2n
- Mezi log n a n je vyssiho radu n

## 2. Serazeni

Od nejpomaleji k nerychleji rostouci:

1. O(1)
2. O(log n)
3. O(n)
4. O(n^2)
5. O(n^3)

### O(1) roste ostre pomaleji nez O(log n)

$1 \in O(\log{n})$

- _Existuji c, $n_0$ takova, ze **1 $\leq$ c \* log n**, pro vsechna $n \geq n_0$._
- (Pouzijeme $log_2$)
- Zvolime: c = 1, $n_0$ = 2 --> $1 \leq 1 * \log_2{}2 = 1$
- Pro $n \geq 2$: 1 = $\log_2{}2 \leq 1 * \log_2{n}$
- $\log_2{n}$ bude pro vyssi n rostouci, tj. nerovnost plati

$\log{n} \notin O(1)$

- _Pro vsechna c, $n_0$, existuje n > $n_0$, pro ktere plati **log n > c \* 1**._
- Aby platil $\log_2{n}$ > c, muzeme vybrat n = $2^{c + 1}$ (--> c + 1 > c)
- $2^{c + 1}$ ale muze teoreticky byt mensi nez $n_0$
- Proto n = max($2^{c + 1}$, $n_0$), aby bylo zaruceno ze n je minimalne $n_0$
- Pro $n \geq 2^{c + 1}$ muzeme vzhledem k rostouci vlastnosti logaritmu rict, ze $\log_2{n}$ > c

### O(log n) roste ostre pomaleji nez O(n)

$\log{n} \in O(n)$

- blabla

$n \notin O(\log{n})$

- blabla

### O(n) roste ostre pomaleji nez O($n^2$)

$n \in O(n^2)$

- blabla

$n^2 \notin O(n)$

- blabla

### O($n^2$) roste ostre pomaleji nez O($n^3$)

$n^2 \in O(n^3)$

- blabla

$n^3 \notin O(n^2)$

- blabla
