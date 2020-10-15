# python3


def prefix(pattern):
	table = [0]
	j, i = 0, 1
	while i < len(pattern):
		if pattern[j] == pattern[i]:
			table.append(j + 1)
			j += 1
			i += 1
		elif j == 0:
			table.append(0)
			i += 1
		else:
			j = table[j - 1]
	return table


def kmp(text, pattern):
	if len(pattern) > len(text):
		return []
	pre_table = prefix(pattern)
	i, j = 0, 0
	out = []
	while i < len(text):
		if pattern[j] == text[i]:
			i += 1
			j += 1
		elif j > 0 and pattern[j] != text[i]:
			j = pre_table[j - 1]
		else:
			i += 1
		if j > len(pattern) - 1:
			out.append(i - len(pattern))
			j = pre_table[-1]
	return out


if __name__ == '__main__':
	pattern = input()
	text = input()
	print(*kmp(text, pattern))