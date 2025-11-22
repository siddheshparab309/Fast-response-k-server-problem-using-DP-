import random
import time
import matplotlib.pyplot as plt

def compute_costs(w):
    n = len(w)
    cost = [[0] * n for _ in range(n)]

    prefix_w = [0] * (n + 1)
    prefix_wi = [0] * (n + 1)

    for i in range(1, n + 1):
        prefix_w[i] = prefix_w[i - 1] + w[i - 1]
        prefix_wi[i] = prefix_wi[i - 1] + w[i - 1] * i

    for l in range(1, n + 1):
        for r in range(l, n + 1):
            mid = (l + r) // 2

            wl = prefix_w[mid] - prefix_w[l - 1]
            wr = prefix_w[r]   - prefix_w[mid]
            cl = wl * mid - (prefix_wi[mid] - prefix_wi[l - 1])
            cr = (prefix_wi[r] - prefix_wi[mid]) - wr * mid

            cost[l - 1][r - 1] = cl + cr

    return cost

def k_server_dp(w, k):
    n = len(w)
    cost = compute_costs(w)

    INF = 10**18
    DP = [[INF] * (k + 1) for _ in range(n + 1)]
    DP[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for t in range(i):
                DP[i][j] = min(DP[i][j], DP[t][j - 1] + cost[t][i - 1])

    return DP[n][k]

def run_experiments(k):
    n_values = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
    results = []

    for n in n_values:
        w = [random.randint(1, 10) for _ in range(n)]

        start = time.time()
        opt_cost = k_server_dp(w, k)
        end = time.time()

        runtime_ms = (end - start) * 1000.0
        total_traffic = sum(w)
        normalized_cost = opt_cost / total_traffic

        print(f"n = {n:3d} | Normalized Cost = {normalized_cost:.4f} | Runtime = {runtime_ms:.3f} ms")

        results.append((n, normalized_cost, runtime_ms))

    return results

def plot_time(results, k):
    ns = [r[0] for r in results]
    exp_times = [r[2] for r in results]   # runtime_ms

    theo_raw = [n**2 for n in ns]
    scale = exp_times[0] / theo_raw[0]
    theo_times = [scale * t for t in theo_raw]

    plt.figure(figsize=(9, 5))
    plt.plot(ns, exp_times, marker='o', label='Experimental Time')
    plt.plot(ns, theo_times, marker='s', linestyle='--', label='Theoretical Time (scaled n²)')

    plt.title(f"Clients vs Runtime for Fast Response k-Server (k = {k})")
    plt.xlabel("Number of Clients (n)")
    plt.ylabel("Time (ms)")
    plt.grid(True, linestyle='--', alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    k = 3
    results = run_experiments(k)   # prints n, normalized cost, runtime
    plot_time(results, k)          # shows clients vs time graph
