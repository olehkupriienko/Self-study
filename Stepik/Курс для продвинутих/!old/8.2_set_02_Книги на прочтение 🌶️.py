n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), \
                         int(input()), int(input()), int(input()), int(input()),

mn = m + n - x - t
mk = m + k - y - t
nk = n + k - z - t

only_n = n - mn - nk - t
only_m = m - mn - mk - t
only_k = k - mk - nk - t

print(only_n + only_m + only_k)

print(mn + mk + nk)

print(a - only_n - only_k - only_m - t - mn - mk - nk)