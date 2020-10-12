# python3

def InverseBWT(bwt):
    end_order = [i for i in range(len(bwt))]
    start_order = sorted(end_order, key=lambda i: bwt[i])
    d = {}
    for start, end in zip(start_order, end_order):
        d[start] = end
    out = ''
    start, end = start_order[0], end_order[0]
    while len(out) < len(bwt):
        out += bwt[start]
        start = end
        end = d[start]
    return out[::-1]


if __name__ == '__main__':
    bwt = input().strip()
    print(InverseBWT(bwt))