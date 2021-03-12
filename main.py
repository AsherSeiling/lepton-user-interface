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
		file_save = input().lower()
		cf.compress_single_file(dir_comp, file_save)
	def directory_comp():
		print("What is the directory that you want to compress")
		print("What is the directory that you want to compress")
		dir_comp = input().lower()
		print("Where do you want to save the outputed files")
		file_save = input().lower()
		cf.compress_dir(dir_comp, file_save)

comps = compression
# Compression starter UI
def compression_ui():
	print("Do you want to compress a single file or an entire directory(f/d)")
	var_search = input().lower()
	if var_search == "d":
		compression.directory_comp()
	elif var_search == "f":
		comps.single_file()
	else:
		compression_ui()

# Functions and classes to decompress a file or file
class decompression:
	def decomp_file():
		print("What is the directory of the file that you want to decompress")
		dir_decomp = input().lower()
		if dir_decomp.endswith(".lep") != True:
			print("This is not a LEP")
			decompression.decomp_file()
		print("Where do you want to save the outputed file")
		file_save = input().lower()
		dcf.decompress_single_file(dir_decomp, file_save)
	def decomp_dir():
		print("What is the directory that you want to decompress")
		print("What is the directory that you want to decompress")
		dir_decomp = input().lower()
		print("Where do you want to save the outputed files")
		file_save = input().lower()
		dcf.decompress_dir(dir_decomp, file_save)
decomp = decompression
# User interface for decompression
def decomp_ui():
	print("Do you want to decompress a single file or an entire directory(f/d)")
	var_search = input().lower()
	if var_search == "d":
		decomp.decomp_dir()
	elif var_search == "f":
		decomp.decomp_file()
	else:
		decomp_ui()

# Main function ran on start
def main():
	print("Compression or Decompress(com/dec)")
	var_search = input().lower()
	if var_search == "com":
		compression_ui()
	elif var_search == "dec":
		decomp_ui()
	else:
		main()

# Runs the main function on the start of the program
if __name__ == '__main__':
	main()