def save_to_file(response: str, filename: str):
    with open(filename, "w") as file:
        file.write(response)
    print(f"Output saved to {filename}")
