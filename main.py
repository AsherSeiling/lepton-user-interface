import compress_files as cf
import decompress_files as dcf
import os



# Functions and classes to compress files
class compression:
	def single_file():
		print("What is the directory of the file that you want to compress")
	def entire_dir():
		pass

# Compression starter UI
def compression_ui():
	print("Do you want to compress a single file or an entire directory(f/d)")
	var_search = input().lower()
	if var_search == "d":
		pass
	elif var_search == "f":
		pass
	else:
		compression_ui()


# Main function ran on start
def main():
	print("Compression or Decompress(com/dec)")
	var_search = input().lower()
	if var_search == "com":
		pass
	elif var_search == "dec":
		pass
	else:
		main()

# Runs the main function on the start of the program
if __name__ == '__main__':
	main()