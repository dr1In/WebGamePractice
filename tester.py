asks = {
    'dr1In': [2, 1000],
    'ave': [1, 900]
}

asks = sorted(asks.items(), key=lambda x: x[-1][-1], reverse=True)
asks = {k: v for k, v in asks}

print(asks.keys())