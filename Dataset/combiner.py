import os
import shutil
import sys

if len(sys.argv) < 4:
    print("Usage python3 <script_name> <dir_path> <final_dir_path> <filter_by_first_letter>")
    exit()

path = sys.argv[1]

folder_names = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
merged_folder_path = os.path.join(path, sys.argv[2])
if not os.path.exists(merged_folder_path):
    os.makedirs(merged_folder_path)

count = 0
for folder_name in folder_names:
	if folder_name[0] == sys.argv[3]:
		folder_path = os.path.join(path, folder_name)
		for file_name in os.listdir(folder_path):
			file_path = os.path.join(folder_path, file_name)
			if os.path.isfile(file_path):
				new_file_path = os.path.join(merged_folder_path, "frame_" + str(count))
				shutil.copy2(file_path, new_file_path)
				count+=1
