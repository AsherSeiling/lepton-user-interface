import os
def compress_single_file(url, save_url):
	url1 = os.path.basename(url)
	name, exstension = os.path.splitext(url1)
	os.system(f"./lepton/build/lepton {url} {save_url}/{name}.lep")
	
