import os
import shutil
import time

def main():

	deleted_folders_count = 0
	deleted_files_count = 0

	path = "/PATH_TO_DELETE"
	days=30
	seconds=time.time()-(days*24*60*60)	
	if os.path.exists(path):
		for root_folder,folders,files in os.walk(path):
			if seconds>=get_file_or_folder_age(root_folder):
				remove_folder(root_folder)
				deleted_folders_count+=1
				break
			else:
				for folder in folders:
					folder_path=os.path.join(root_folder,folder)
					if seconds>=get_file_or_folder_age(root_folder):
						remove_folder(folder_path)
						deleted_folders_count+=1
				
				for file in files:
					file_path=os.path.join(root_folder,file)
					if seconds>=get_file_or_folder_age(root_folder):
						remove_file(file_path)
						deleted_files_count+=1
	else :
		print("path not found")
	print("total folders deleted=",deleted_folders_count)	
	print("total files deleted=",deleted_files_count)
def remove_folder(path):
	if not os.remove(path):
		print("Removed succesfully")
	else:
		print("unable to delete")	
def remove_file(path):
	if not os.remove(path):
		print("Removed succesfully")
	else:
		print("unable to delete")
def get_file_or_folder_age(path):
	ctime=os.stat(path).st_ctime
	return ctime
if __name__=="__main__"	:
	main()
