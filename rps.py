import random

my_list = ["Rock", "Paper", "Scissors"]

while True:
	while True:
		print("1:Rock / 2:Paper / 3:Scissors ")
		urchoice = input("What you chose? : ")

		if(urchoice == "1" or urchoice == "2" or urchoice == "3"):
			break

	rand_choice = random.choice (my_list)
	print("\nCPU played : "+rand_choice)
	if(urchoice == "1"):
		print("You played : Rock\n")
	elif(urchoice == "2"):
		print("You played : Paper\n")
	elif(urchoice == "3"):
		print("You played : Scissors\n")
	

	if(urchoice == "1" and rand_choice == "Rock"):
		print("DRAW !")
	elif(urchoice == "1" and rand_choice == "Paper"):
		print("You Lose !")
	elif(urchoice == "1" and rand_choice == "Scissors"):
		print("You Win :")

	elif(urchoice == "2" and rand_choice == "Rock"):
		print("You Win !")
	elif(urchoice == "2" and rand_choice == "Paper"):
		print("DRAW !")
	elif(urchoice == "2" and rand_choice == "Scissors"):
		print("You Lose !")

	elif(urchoice == "3" and rand_choice == "Rock"):
		print("You Win !")
	elif(urchoice == "3" and rand_choice == "Paper"):
		print("DRAW !")
	elif(urchoice == "3" and rand_choice == "Scissors"):
		print("You Lose !")


	
	quit = input("\nYou wanna continue playing? (1 for yes / any other character for no) : ")
	if(quit == "1"):
		print("\n")
	else:
		break