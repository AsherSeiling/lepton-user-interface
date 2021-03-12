import os
# Module to decompress a single file
def decompress_single_file(url, save_url):
	url1 = os.path.basename(url)
	name, exstension = os.path.splitext(url1)
	if save_url[len(save_url) - 1] != "/":
		save_url += "/"
	os.system(f"./lepton/build/lepton {url} {save_url}/{name}.jpg")
	print(f"./lepton/build/lepton {url} {save_url}/{name}.jpg")
	
# Module to decompress an antire directory
def decompress_dir(url, save_folder):
	files = os.listdir(url)
	compressable_files = []
	for i in files:
		if i.lower().endswith(".lep") == True:
			compressable_files.append(i)
	for i in compressable_files:
		decompress_single_file((url + i), save_folder)
