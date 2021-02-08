# This program will solve a Sudoku Puzzle
# you can change the puzzle in sudoku.csv

import math
import csv
import time
import random

puzzle = []
possibilities = {}
check = [0]  # checks in there was any change
unique = []  # list with all possibilities in a line
unique_elements = []  # list with unique possibilities in a line
check_cycle = [0]
cycle_count = [0]  # counts  how many cycles the program takes to solve
puzzle_backup = []
possibilities_backup = {}


def main():
	get_values()  # gets values from csv file
	print('Puzzle')  # prints the initial puzzle
	for i in range(9):
		print(puzzle[i])
	create_dict()  # creates the dictionarie with possibilities
	start = time.time()  # starts the timer
	if (solve()):
		print('No guess')
	else:
		while (test() == False):
			get_values()
			create_dict()
			#for i in range(9):
			#    print(puzzle[i])
			solve()
			guess()
			solve()
	if (test()):
		print('Solved!')
		print(possibilities)
		print('\nSolution')  # prints the solved puzzle
		for i in range(9):
			print(puzzle[i])
		print()
		print(f'Cycles: {cycle_count[0]}')
	else:
		print('Error')
	end = time.time()  # ends the timer
	print(f'Execution time: {end - start}')


def solve():
	for i in range(40):  # calls the cycle 20 times
		check_cycle[0] = 0  # for the initial part of the cycle
		cycle()  # calls the cycle
		cycle_count[0] += 1
		if possibilities == {}:  # there are no more possibilities
			break
		elif check_cycle[0] == 0:  # no more moves, but it is incomplete
			#print('No solution')
			return False
	return True


def cycle():
	while True:
		line_remove()
		column_remove()
		cube_remove()
		update1()
		if (check_changes()):
			break
		else:
			continue
		print()
		for i in range(9):
			print(puzzle[i])
	line_unique()
	line_unique_possibilities()
	update2()
	line_remove()
	column_remove()
	cube_remove()
	column_unique()
	column_unique_possibilities()
	update3()
	line_remove()
	column_remove()
	cube_remove()
	cube_unique()
	cube_unique_possibilities()
	update4()


def get_values():
	puzzle.clear()
	with open('sudoku.csv') as csv_file:
		reader = csv.reader(csv_file)
		i = 0
		for row in reader:
			puzzle.append([])
			for n in row:
				puzzle[i].append(int(n))
			i = i + 1


def create_dict():
	for x in range(89):
		try:
			i = math.floor(x / 10)
			j = x % 10
			if puzzle[i][j] == 0:
				possibilities[str(x)] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
			else:
				continue
		except:
			continue


def line_remove():
	for i in range(9):
		for j in range(9):
			if puzzle[i][j] == 0:
				continue
			else:
				for k in range(9):
					n = 10 * i + k
					try:
						possibilities[str(n)].remove(puzzle[i][j])
					except:
						continue


def column_remove():
	for i in range(9):
		for j in range(9):
			if puzzle[i][j] == 0:
				continue
			else:
				for k in range(9):
					n = j + 10 * k
					try:
						possibilities[str(n)].remove(puzzle[i][j])
					except:
						continue


def cube_remove():
	cubes = [[0, 1, 2, 10, 11, 12, 20, 21, 22],
	         [3, 4, 5, 13, 14, 15, 23, 24, 25],
	         [6, 7, 8, 16, 17, 18, 26, 27, 28],
	         [30, 31, 32, 40, 41, 42, 50, 51, 52],
	         [33, 34, 35, 43, 44, 45, 53, 54, 55],
	         [36, 37, 38, 46, 47, 48, 56, 57, 58],
	         [60, 61, 62, 70, 71, 72, 80, 81, 82],
	         [63, 64, 65, 73, 74, 75, 83, 84, 85],
	         [66, 67, 68, 76, 77, 78, 86, 87, 88]]
	for i in range(9):
		for j in range(9):
			if puzzle[i][j] == 0:
				continue
			else:
				n = 10 * i + j
				for x in range(9):
					if n in cubes[x]:
						for element in cubes[x]:
							try:
								possibilities[str(element)].remove(
								    puzzle[i][j])
							except:
								continue
					else:
						continue


def update1():  # based on the three previous steps it uppdates the puzzle
	for x in range(89):
		if (x % 10 == 9):
			continue
		else:
			try:
				if len(possibilities[str(x)]) == 1:
					i = math.floor(x / 10)
					j = x % 10
					puzzle[i][j] = possibilities[str(x)][0]
					del possibilities[str(x)]
					check[0] = check[0] + 1
					check_cycle[0] += 1
			except:
				continue


def check_changes():
	if check[0] == 0:
		return True
	else:
		check[0] = 0
		return False


def line_unique():  # gathers the possibilities in a line
	unique.clear()
	for i in range(9):
		unique.append([])
		for k in range(9):
			n = 10 * i + k
			try:
				unique[i] += possibilities[str(n)]
			except:
				continue


def line_unique_possibilities():  # finds unique possibilities in a line
	unique_elements.clear()
	for i in range(9):
		unique_elements.append([])
		for j in range(1, 10):
			y = unique[i].count(j)
			if y == 1:
				unique_elements[i].append(j)
			else:
				continue


def update2():  # changes puzzle ased on unique possibilities of a line
	for i in range(9):
		for j in range(len(unique_elements[i])):
			for k in range(9):
				try:
					n = 10 * i + k
					if unique_elements[i][j] in possibilities[str(n)]:
						puzzle[i][k] = unique_elements[i][j]
						del possibilities[str(n)]
						check_cycle[0] += 1
					else:
						continue
				except:
					continue


def column_unique():  # gathers the possibilities in a column
	unique.clear()
	for i in range(9):
		unique.append([])
		for k in range(9):
			n = i + 10 * k
			try:
				unique[i] += possibilities[str(n)]
			except:
				continue


def column_unique_possibilities():  # finds unique possibilities in a coulumn
	unique_elements.clear()
	for i in range(9):
		unique_elements.append([])
		for j in range(1, 10):
			y = unique[i].count(j)
			if y == 1:
				unique_elements[i].append(j)
			else:
				continue


def update3():  # changes puzzle ased on unique possibilities of a column
	for i in range(9):
		for j in range(len(unique_elements[i])):
			for k in range(9):
				try:
					n = i + 10 * k
					if unique_elements[i][j] in possibilities[str(n)]:
						puzzle[k][i] = unique_elements[i][j]
						del possibilities[str(n)]
						check_cycle[0] += 1
					else:
						continue
				except:
					continue


def cube_unique():
	unique.clear()
	cubes = [[0, 1, 2, 10, 11, 12, 20, 21, 22],
	         [3, 4, 5, 13, 14, 15, 23, 24, 25],
	         [6, 7, 8, 16, 17, 18, 26, 27, 28],
	         [30, 31, 32, 40, 41, 42, 50, 51, 52],
	         [33, 34, 35, 43, 44, 45, 53, 54, 55],
	         [36, 37, 38, 46, 47, 48, 56, 57, 58],
	         [60, 61, 62, 70, 71, 72, 80, 81, 82],
	         [63, 64, 65, 73, 74, 75, 83, 84, 85],
	         [66, 67, 68, 76, 77, 78, 86, 87, 88]]
	for i in range(9):
		unique.append([])
		for key in cubes[i]:
			try:
				unique[i] += possibilities[str(key)]
			except:
				continue


def cube_unique_possibilities():
	unique_elements.clear()
	for i in range(9):
		unique_elements.append([])
		for j in range(1, 10):
			y = unique[i].count(j)
			if y == 1:
				unique_elements[i].append(j)
			else:
				continue


def update4():
	cubes = [[0, 1, 2, 10, 11, 12, 20, 21, 22],
	         [3, 4, 5, 13, 14, 15, 23, 24, 25],
	         [6, 7, 8, 16, 17, 18, 26, 27, 28],
	         [30, 31, 32, 40, 41, 42, 50, 51, 52],
	         [33, 34, 35, 43, 44, 45, 53, 54, 55],
	         [36, 37, 38, 46, 47, 48, 56, 57, 58],
	         [60, 61, 62, 70, 71, 72, 80, 81, 82],
	         [63, 64, 65, 73, 74, 75, 83, 84, 85],
	         [66, 67, 68, 76, 77, 78, 86, 87, 88]]
	for i in range(9):
		for j in range(len(unique_elements[i])):
			for key in cubes[i]:
				try:
					if unique_elements[i][j] in possibilities[str(key)]:
						x = math.floor(key / 10)
						y = key % 10
						puzzle[x][y] = unique_elements[i][j]
						del possibilities[str(key)]
						check_cycle[0] += 1
					else:
						continue
				except:
					continue


def guess():
	keys = []
	for key in possibilities:
		if len(possibilities[key]) < 5:
			keys.append(key)
	#print(keys)
	sampling = random.choices(keys, k=5)
	#print(sampling)
	for value in sampling:
		try:
			n = random.choice(possibilities[str(value)])
			#print(value, n)
			x = math.floor(int(value) / 10)
			y = int(value) % 10
			puzzle[x][y] = n
			del possibilities[str(value)]
			line_remove()
			column_remove()
			cube_remove()
		except:
			continue
			#print('error')


def test():
	count = 0
	ideal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	temp = []
	for i in range(9):
		if sorted(puzzle[i]) == ideal:
			count += 1
	for i in range(9):
		temp.append([])
		for j in range(9):
			temp[i].append(puzzle[j][i])
	for i in range(9):
		if sorted(temp[i]) == ideal:
			count += 1
	if count == 18:
		return True
	else:
		return False


main()
