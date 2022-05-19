import math
from timeit import default_timer as timer
import matplotlib.pyplot as plt


def f1(n):
    s = 0
    for j in range(1, n):
        s = s + 1 / j
    return s


def f2(n):
    s = 0
    for j in range(1, n):
        for k in range(1, n):
            s = s + k / j
    return s


def f3(n):
    s = 0
    for j in range(1, n):
        for k in range(j, n):
            s = s + k / j
    return s


def f4(n):
    s = 0
    for j in range(1, n):
        k = 2
        while k <= n:
            s = s + k / j
            k = k * 2
    return s


def f5(n):
    s = 0
    k = 2
    while k <= n:
        s = s + 1 / k
        k = k * 2
    return s


nn = [2000, 4000, 8000, 16000, 32000]

for n in nn:
    start = timer()
    f5(n)
    stop = timer()
    Tn = stop - start
    Fn = math.log(n, 2)
    print(n, Tn, Fn / Tn)


# Listy z wynikami czasu dla każdej funkcji dla listy nn

wynikiF1 = [0.0001511929999651329, 0.0002812180000546505,
            0.0005979060001664038, 0.001189012999930128, 0.002387951999935467]
wynikiF2 = [0.15156417299976965, 0.6049707780002791,
            2.386549519000255, 9.544505023000056, 38.02141501699998]
wynikiF3 = [0.07835924200026056, 0.3083287019999261,
            1.2030254100000093, 4.830229494999912, 19.343663134000053]
wynikiF4 = [0.001174343000002409, 0.002657448999798362,
            0.005791040000076464, 0.012872396000148001, 0.027427957999861974]
wynikiF5 = [2.2000000000008124e-06,
            1.6000000000009063e-06, 1.1000000000004062e-06, 1.1000000000004062e-06, 1.1000000000004062e-06]

# Utworzenie wykresu (3 funkcje nachodzą na siebie na wykresie, aby je zobaczyć trzeba przybliżyć)
plt.xlabel("Rozmiar wejścia")
plt.ylabel("Czas wykonywania")
plt.plot(nn, wynikiF1, label="f1")
plt.plot(nn, wynikiF2, label="f2")
plt.plot(nn, wynikiF3, label="f3")
plt.plot(nn, wynikiF4, label="f4")
plt.plot(nn, wynikiF5, label="f5")
plt.legend()
plt.title("Wykres złożoności czasowej")
plt.show()


# Kod funkcji wykonujących pomiary oraz ich wyniki

# Funkcja f1(n)
# Podane n, Czas wykonywania, FN/TN

# for n in nn:
#     start = timer()
#     f1(n)
#     stop = timer()
#     Tn = stop - start
#     Fn = n
#     print(n, Tn, Fn / Tn)

# 2000 0.0001511929999651329 13228125.643787915
# 4000 0.0002812180000546505 14223840.5764306
# 8000 0.0005979060001664038 13380029.633041836
# 16000 0.001189012999930128 13456539.16394542
# 32000 0.002387951999935467 13400604.367619107

# Złożoność czasowa funkcji to Fn(n)

# Funkcja f2
# Podane n, Czas wykonywania, FN/TN

# for n in nn:
#     start = timer()
#     f1(n)
#     stop = timer()
#     Tn = stop - start
#     Fn = n*n
#     print(n, Tn, Fn / Tn)

# 2000 0.15156417299976965 26391461.259159703
# 4000 0.6049707780002791 26447558.430653024
# 8000 2.386549519000255 26816958.747543663
# 16000 9.544505023000056 26821715.676517434
# 32000 38.02141501699998 26932190.7020597


# Funkcja f3
# Podane n, Czas wykonywania, FN/TN

# for n in nn:
#     start = timer()
#     f3(n)
#     stop = timer()
#     Tn = stop - start
#     Fn = (n*n)/2
#     print(n, Tn, Fn / Tn)

# 2000 0.07835924200026056 25523473.031979423
# 4000 0.3083287019999261 25946335.67393903
# 8000 1.2030254100000093 26599604.409020547
# 16000 4.830229494999912 26499776.073269647
# 32000 19.343663134000053 26468616.43801404


# Funkcja f4
# Podane n, Czas wykonywania, FN/TN

# for n in nn:
#     start = timer()
#     f4(n)
#     stop = timer()
#     Tn = stop - start
#     Fn=n*math.log(n,2)
#     print(n, Tn, Fn / Tn)

# 2000 0.001174343000002409 18675607.18570229
# 4000 0.002657448999798362 18010933.471265126
# 8000 0.005791040000076464 17911510.588068314
# 16000 0.012872396000148001 17359048.661338903
# 32000 0.027427957999861974 17460472.161711667


# Funkcja f5
# Podane n, Czas wykonywania, FN/TN

# for n in nn:
#     start = timer()
#     f5(n)
#     stop = timer()
#     Tn = stop - start
#     Fn=math.log(n,2)
#     print(n, Tn, Fn / Tn)

# 2000 2.2000000000008124e-06 4984447.40211729
# 4000 1.6000000000009063e-06 7478615.177909569
# 8000 1.1000000000004062e-06 11787076.622415727
# 16000 1.1000000000004062e-06 12696167.5315063
# 32000 1.1000000000004062e-06 13605258.440596873
