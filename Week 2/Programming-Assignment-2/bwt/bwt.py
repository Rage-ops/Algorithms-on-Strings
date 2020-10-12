# python3

def BWT(text):
    m = [text]
    for i in range(len(text) - 1, 0, -1):
        m.append(text[i:] + text[:i])
    m.sort()
    out = ''
    for rotation in m:
        out += rotation[-1]
    return out


if __name__ == '__main__':
    text = input().strip()
    print(BWT(text))