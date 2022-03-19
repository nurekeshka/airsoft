import os


def find_folder(folder):
    return os.getenv('startup')


def main():
    print(find_folder('startup'))


if __name__ == "__main__":
    main()