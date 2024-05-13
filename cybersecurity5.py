import os

def secure_file_deletion(file_path):
    with open(file_path, 'w') as file:
        file.write(os .urandom(1024))
        #overwrite the file with random data
        os.remove(file_path)
        print(f"{file_path} securely deleted")
        
        #example 
        file_path_to_delete = "example.text"
        