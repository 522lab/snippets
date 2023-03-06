import os

directory = "/mnt/c/Users/522/Desktop"

for subdir, dirs, files in os.walk(directory):
	for file in files:
		if file.endswith(".tsv"):
			old_path = os.path.join(subdir, file)
			new_file = os.path.splitext(file)[0] + subdir.split('/')[-1] + ".tsv"
			new_path = os.path.join(subdir, new_file)
			os.rename(old_path, new_path)
