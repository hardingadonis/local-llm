import requests
from tqdm import tqdm

def download_file_with_progress(url, destination):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(destination, 'wb') as file, tqdm(
            desc=destination,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

    print(f"Download successful. File saved to {destination}")

def show_menu(model_links, model_names):
    print("Choose models to download (enter model numbers separated by commas):")
    for i, link in enumerate(model_names, 1):
        print(f"{i}. Model " + model_names[i - 1])

    choices = input("Enter model numbers (e.g., 1, 3, 5): ")
    try:
        choices = [int(choice) for choice in choices.split(',')]
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        return

    for choice in choices:
        if 1 <= choice <= len(model_names):
            url = model_links[choice - 1]
            destination = f"models/" + model_names[choice - 1]

            download_file_with_progress(url, destination)
        else:
            print(f"Invalid choice: {choice}. Skipping.")

if __name__ == "__main__":
    model_links = [
        "https://gpt4all.io/models/gguf/mistral-7b-openorca.Q4_0.gguf",
        "https://gpt4all.io/models/gguf/mistral-7b-instruct-v0.1.Q4_0.gguf",
        "https://gpt4all.io/models/gguf/gpt4all-falcon-q4_0.gguf",
        "https://gpt4all.io/models/gguf/orca-2-7b.Q4_0.gguf",
        "https://gpt4all.io/models/gguf/orca-2-13b.Q4_0.gguf",
        "https://gpt4all.io/models/gguf/wizardlm-13b-v1.2.Q4_0.gguf",
        "https://gpt4all.io/models/gguf/nous-hermes-llama2-13b.Q4_0.gguf",
        "https://gpt4all.io/models/gguf/gpt4all-13b-snoozy-q4_0.gguf",
        "https://gpt4all.io/models/gguf/mpt-7b-chat-merges-q4_0.gguf",
        "https://gpt4all.io/models/gguf/orca-mini-3b-gguf2-q4_0.gguf",
        "https://gpt4all.io/models/gguf/replit-code-v1_5-3b-q4_0.gguf",
        "https://gpt4all.io/models/gguf/starcoder-q4_0.gguf",
        "https://gpt4all.io/models/gguf/rift-coder-v0-7b-q4_0.gguf",
    ]

    model_names = [
        "mistral-7b-openorca.Q4_0.gguf",
        "mistral-7b-instruct-v0.1.Q4_0.gguf",
        "gpt4all-falcon-q4_0.gguf",
        "orca-2-7b.Q4_0.gguf",
        "orca-2-13b.Q4_0.gguf",
        "wizardlm-13b-v1.2.Q4_0.gguf",
        "nous-hermes-llama2-13b.Q4_0.gguf",
        "gpt4all-13b-snoozy-q4_0.gguf",
        "mpt-7b-chat-merges-q4_0.gguf",
        "orca-mini-3b-gguf2-q4_0.gguf",
        "replit-code-v1_5-3b-q4_0.gguf",
        "starcoder-q4_0.gguf",
        "rift-coder-v0-7b-q4_0.gguf",
    ]

    show_menu(model_links, model_names)