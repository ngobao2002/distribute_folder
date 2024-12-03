import os
import shutil

# Đường dẫn đến folder plugins chứa 10,000 folder nhỏ
source_folder = "D:\plugins"

# Danh sách các folder đích
destination_folders = [
    "D:\plugins1",
    "D:\plugins2",
    "D:\plugins3",
    "D:\plugins4"
]

def distribute_folders(source_folder, destination_folders):
    # Lấy danh sách tất cả folder con trong folder plugins
    all_folders = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]
    total_folders = len(all_folders)
    
    # Số lượng folder con trong mỗi folder đích
    num_destinations = len(destination_folders)
    folders_per_destination = total_folders // num_destinations
    remainder = total_folders % num_destinations

    # Chia folder con vào từng folder đích
    start_idx = 0
    for i, dest_folder in enumerate(destination_folders):
        os.makedirs(dest_folder, exist_ok=True)
        
        # Xác định phạm vi folder con cho folder đích này
        end_idx = start_idx + folders_per_destination + (1 if i < remainder else 0)
        
        # Di chuyển folder con
        for folder_name in all_folders[start_idx:end_idx]:
            source_path = os.path.join(source_folder, folder_name)
            dest_path = os.path.join(dest_folder, folder_name)
            shutil.move(source_path, dest_path)

        print(f"Đã di chuyển {end_idx - start_idx} folder vào {dest_folder}")
        start_idx = end_idx

# Gọi hàm
distribute_folders(source_folder, destination_folders)
