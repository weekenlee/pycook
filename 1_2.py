
def sum(data):
	head, *tail = data
	return head + sum(tail) if tail else head

if __name__ == '__main__':
	result = sum(range(10))
	print(result)
