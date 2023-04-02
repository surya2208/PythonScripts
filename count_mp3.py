import os

def count_mp3_files(input_dir):
    count = 0
    for item in os.listdir(input_dir):
        item_path = os.path.join(input_dir, item)
        if os.path.isfile(item_path) and item_path.endswith('.mp3'):
            count += 1
        elif os.path.isdir(item_path):
            count += count_mp3_files(item_path)
    return count

print(count_mp3_files("D:\\Entertainment"))
