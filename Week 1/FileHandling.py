import os # module needed to delete files

# File handling
# creating, opening, reading, writing, and deleting using Python
# Python has built-in functions so no imports for the most part

# Important for data persistence and processing
# automation of many real-world tasks
# and handling large data sets

# open() is the key function and takes 2 parameters: filename and mode
# 4 different modes
# "r" - read; throws error if file does not exist
# "a" - append; creates file if it does not exist
# "w" - write; if a file already has data, it will be overwritten
# "x" = create; throws error if file fails to create (ex. file path error)

# Determine if file is binary or text using "b" and "t"

# myFile = open("./Week 1/resources/MyNewFile.txt", "x") create new file
# mySecondFile = open("./Week 1/resources/MySecondFile.txt", "+w") 
# + allows for 2 operations (+w is create and write)

# myFile = open("./Week 1/resources/MyNewFile.txt", "r")
# print(myFile.read())

# readline() reads a single line, and moves cursor to next line
# print(myFile.readline().strip('\n'))
# print(myFile.readline())
# print(myFile.readline())

# read(x) reads x amount of characters from wherever cursor is
# print(myFile.read(5)) 

# Close file when we are done
# myFile.close()

# Access files using exact paths
# with open('C:/Users/jason/Repos/TRNG2364-DataFoundations/Week 1/resources/MyNewFile.txt') as myFile:
#     print(myFile.read())
# with automatically closes at the end of the block

# pokemonTeam = []

# for p in range(6):
#     pokemon = input("Enter a Pokemon for your team: ")
#     pokemonTeam.append(pokemon)

# with open("./Week 1/resources/MyPokemonTeam.txt", "+w") as teamFile:
#     for p in pokemonTeam:
#         teamFile.write(p + '\n')
#     print("Your Pokemon team has been saved!")

# with open("./Week 1/resources/MyPokemonTeam.txt", "r") as teamFile:
#     print("Your Pokemon team consists of: ")
#     print(teamFile.read())

# Let's delete MySecondFile
# Best practice to check if it exists before we delete
# if os.path.exists("./Week 1/resources/MySecondFile.txt"):
#     os.remove("./Week 1/resources/MySecondFile.txt")
#     print("File deleted successfully")
# else:
#     print("Something went wrong, file was not deleted")

with open("./Week 1/resources/MyNewFile.txt") as myFile:
    lines = myFile.readlines() # creates a list of each line

    print(myFile.tell()) # tells you how far from the start of the file the cursor is

    position = myFile.seek(5, 0) # seek manually moves the cursor
                                 # the second parameter is optional
                                 # 0 (default) means from the start
                                 # 1 means from its current
                                 # 2 means from the end
                                    # you have to open the file in binary "b"
                                    # to enable 1 and 2
    
    # position = myFile.seek(5, 1) # !!have to open in binary!!
    # but 0 seek is allowed with 1 and 2
    position = myFile.seek(0, 2) # sends cursor to end of the file
    
    print(position)

# Opening a file in binary is required for any read/write on non-text files
# line one
# line two
# line three
# line four