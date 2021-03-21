import socket; import PySimpleGUI as GUI; import threading

def clr():
	print("\n" * 150)
gameEnded = False
exit = False
pickedSpaces = [0]
playerOnePicked = [0, 0, 0, 0, 0, 0, 0, 0, 0]
playerTwoPicked = [0, 0, 0, 0, 0, 0, 0, 0, 0]
clr()
while not exit:
	board = """     |     |
  1  |  2  |  3
     |     |
-----------------
     |     |
  4  |  5  |  6
     |     |
-----------------
     |     |
  7  |  8  |  9
     |     |
"""
	playerWon = -1
	error = True
	pickedSpaces = [0]
	playerOnePicked = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	playerTwoPicked = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	while error:
		try:
			choice = int(input("Welcome to tic-tac-toe.\n\n1 - Play\n2 - Exit\n"))
			if choice == 2:
				exit = True
				playerWon = -1
				error = False
			elif choice == 1:
				error = False
			else:
				clr()
				input("Input a valid nunber.\n\nPress -ENTER- to try again.\n")
				clr()
		except:
			clr()
			input("Input a valid nunber.\n\nPress -ENTER- to try again.\n")
			clr()
	while not gameEnded and not exit:
		clr()
		error = True
		invalidSpace = False
		while error:
			try:
				choice = int(input("Player 1, please pick a number on the board:\n\n" + board))
				error = False
			except:
				clr()
				input("Input a valid number.\n\nPress -ENTER- to try again.error\n")
				clr()
				error = True
				invalidSpace = True
			for space in pickedSpaces:
				if choice == space:
					invalidSpace = True
			if choice < 1 or choice > 9:
				invalidSpace = True
			if not invalidSpace:
				pickedSpaces.append(choice)
				board = board.replace(str(choice), "X")
				playerOnePicked[choice - 1] = 1
				if playerOnePicked[0] == 1 and playerOnePicked[1] == 1 and playerOnePicked[2] == 1 or playerOnePicked[3] == 1 and playerOnePicked[4] == 1 and playerOnePicked[5] == 1 or playerOnePicked[6] == 1 and playerOnePicked[7] == 1 and playerOnePicked[8] or playerOnePicked[0] and playerOnePicked[3] and playerOnePicked[6] or playerOnePicked[1] and playerOnePicked[4] and playerOnePicked[7] or playerOnePicked[2] and playerOnePicked[5] and playerOnePicked[8] or playerOnePicked[0] and playerOnePicked[4] and playerOnePicked[8] or playerOnePicked[2] and playerOnePicked[4] and playerOnePicked[6] == 1:
					gameEnded = True
					playerWon = 1
				if len(pickedSpaces) >= 10:
					gameEnded = True
					playerWon = 0
			elif not error:
				clr()
				input("Input a valid number.\n\nPress -ENTER- to try again.invalid\n")
				clr()
				error = True
				invalidSpace = False
		if not gameEnded:
			clr()
			error = True
			invalidSpace = False
			while error:
				try:
					choice = int(input("Player 2, please pick a number on the board:\n\n" + board))
					error = False
				except:
					clr()
					input("Input a valid number.\n\nPress -ENTER- to try again.error\n")
					clr()
					error = True
					invalidSpace = True
				for space in pickedSpaces:
					if choice == space:
						invalidSpace = True
				if choice < 1 or choice > 9:
					invalidSpace = True
				if not invalidSpace:
					pickedSpaces.append(choice)
					board = board.replace(str(choice), "O")
					playerTwoPicked[choice - 1] = 1
					if playerTwoPicked[0] == 1 and playerTwoPicked[1] == 1 and playerTwoPicked[2] == 1 or playerTwoPicked[3] == 1 and playerTwoPicked[4] == 1 and playerTwoPicked[5] == 1 or playerTwoPicked[6] == 1 and playerTwoPicked[7] == 1 and playerTwoPicked[8] or playerTwoPicked[0] and playerTwoPicked[3] and playerTwoPicked[6] or playerTwoPicked[1] and playerTwoPicked[4] and playerTwoPicked[7] or playerTwoPicked[2] and playerTwoPicked[5] and playerTwoPicked[8] or playerTwoPicked[0] and playerTwoPicked[4] and playerTwoPicked[8] or playerTwoPicked[2] and playerTwoPicked[4] and playerTwoPicked[6] == 1:
						gameEnded = True
						playerWon = 2
					if len(pickedSpaces) >= 10:
						gameEnded = True
						playerWon = 0
				elif not error:
					clr()
					input("Input a valid number.\n\nPress -ENTER- to try again.invalid\n")
					clr()
					error = True
					invalidSpace = False
	clr()
	if playerWon == 1:
		input(board + "\nPlayer 1 Won!\n\nPress -ENTER- to go back to the menu.")
	elif playerWon == 2:
		input(board + "\nPlayer 2 Won!\n\nPress -ENTER- to go back to the menu.")
	elif playerWon == 0:
		input(board + "\nNobody won.\n\nPress -ENTER- to go back to the menu.")
	clr()
	gameEnded = False