import os
import subprocess

def list_gguf_files(folder_path):
    gguf_files = [f for f in os.listdir(folder_path) if f.endswith('.gguf')]
    return gguf_files

def show_menu_and_execute_command(gguf_files, command_template):
    print("Choose a model to run:")
    for i, file_name in enumerate(gguf_files, 1):
        print(f"{i}. {file_name}")

    try:
        choice = int(input("Enter the number of the model you want to run: "))
        if 1 <= choice <= len(gguf_files):
            chosen_file = gguf_files[choice - 1]
            command = command_template.replace("{MODEL_FILE}", chosen_file)
            subprocess.run(command, shell=True)
        else:
            print("Invalid choice. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    folder_path = "models"
    command_template = "python -m llama_cpp.server --model \"./models/{MODEL_FILE}\" --chat_format chatml --n_gpu_layers 1"

    gguf_files = list_gguf_files(folder_path)
    if gguf_files:
        show_menu_and_execute_command(gguf_files, command_template)
    else:
        print("No .gguf files found in the specified folder.")
