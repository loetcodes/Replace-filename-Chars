"""

Python3 code to replace hyphens with underscores in files in a directory or folder 

"""

import os 

# Function to rename multiple files 
def main():
	#directory = input("Enter folder path: ")
	directory = "Files/GitHub/100-Days-of-Code---PythonChallenge-01"
	folder = os.listdir(directory)
	i = 0
	for filename in range(len(folder)):
		new_name = folder[filename].replace("-", "_")
		old_file = directory + "/" + folder[filename]
		new_file = directory + "/" + new_name

		os.rename(old_file, new_file) 
		i += 1


if __name__ == '__main__': 
	
	# Calling main() function
	main() 
