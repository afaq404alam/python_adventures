def movetower(height, from_pole, to_pole, with_pole):
	if height >= 1:
		movetower(height-1, from_pole, with_pole, to_pole)
		movedisk(from_pole, to_pole)
		movetower(height-1, with_pole, to_pole, from_pole)

def movedisk(fp, tp):
	print('moving disk from ', fp, 'to ', tp)

def main():
	movetower(3, 'A', 'B', 'C')

if __name__ == '__main__':
	main()