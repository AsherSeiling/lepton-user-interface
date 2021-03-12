import os
def compress_single_file(url, save_url):
	name, exstension = os.path.splitext(url)
	os.system(f"./lepton/build/lepton {url} {save_url}{name}.lep")
	
