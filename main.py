import compress_files as cf
import decompress_files as dcf
import os



# Functions and classes to compress files
class compression:
	def single_file():
		print("What is the directory of the file that you want to compress")
		dir_comp = input().lower()
		if dir_comp.endswith(".jpg") != True:
			if dir_comp.endswith(".jpeg") != True:
				print("This is not a JPG")
				compression.single_file()
		print("Where do you want to save the outputed file")
		file_save = input()

	def entire_dir():
		pass
comps = compression
# Compression starter UI
def compression_ui():
	print("Do you want to compress a single file or an entire directory(f/d)")
	var_search = input().lower()
	if var_search == "d":
		pass
	elif var_search == "f":
		comps.single_file()
	else:
		compression_ui()


# Main function ran on start
def main():
	print("Compression or Decompress(com/dec)")
	var_search = input().lower()
	if var_search == "com":
		compression_ui()
	elif var_search == "dec":
		pass
	else:
		main()

# Runs the main function on the start of the program
if __name__ == '__main__':
	main()