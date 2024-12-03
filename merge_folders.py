import os
import shutil

# Danh sách các folder nhỏ
source_folders = [
    "D:\plugins1.1",
    "D:\plugins1.2",
    "D:\plugins1.3"
]

# Folder lớn để gom tất cả folder con lại
destination_folder = "D:\plugins1"

def merge_folders(source_folders, destination_folder):
    # Tạo folder lớn nếu chưa tồn tại
    os.makedirs(destination_folder, exist_ok=True)
    
    # Di chuyển tất cả folder con từ các folder nhỏ vào folder lớn
    for source_folder in source_folders:
        for folder_name in os.listdir(source_folder):
            source_path = os.path.join(source_folder, folder_name)
            dest_path = os.path.join(destination_folder, folder_name)
            
            if os.path.isdir(source_path):  # Chỉ di chuyển nếu là folder
                shutil.move(source_path, dest_path)
                print(f"Đã di chuyển {folder_name} từ {source_folder} đến {destination_folder}")
    
    print("Hoàn tất việc gom các folder con!")

# Gọi hàm
merge_folders(source_folders, destination_folder)
