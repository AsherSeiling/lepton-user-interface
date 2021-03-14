import os
def compress_single_file(url, save_url):
	url1 = os.path.basename(url)
	name, exstension = os.path.splitext(url1)
	if save_url[len(save_url) - 1] != "/":
		save_url += "/"
	os.system(f"./lepton/build/lepton {url} {save_url}{name}.lep")
	
# Module to compress an antire directory
def compress_dir(url, save_folder):
	files = os.listdir(url)
	compressable_files = []
	for i in files:
		if i.lower().endswith(".jpg") == True:
			compressable_files.append(i)
		elif i.lower().endswith(".jpeg") == True:
			compressable_files.append(i)
	for i in compressable_files:
		compress_single_file((url + i), save_folder)
	print(len(compressable_files))
