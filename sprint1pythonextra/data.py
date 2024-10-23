import os


def update_tendencies(rock_count, paper_count, scissors_count):
    file = open("tendencies", "r+")
    rock_count += int(file.readline().split(":")[1])
    paper_count += int(file.readline().split(":")[1])
    scissors_count += int(file.readline().split(":")[1])
    file.truncate()
    file.seek(0)
    file.write(f"rock:{rock_count}\n")
    file.write(f"paper:{paper_count}\n")
    file.write(f"scissors:{scissors_count}\n")

    # Truncar el archivo para evitar que queden datos antiguos
    file.truncate()

def reset_values():
    file = open("tendencies", "r+")
    file.write(f"rock:{1}\n")
    file.write(f"paper:{1}\n")
    file.write(f"scissors:{1}\n")

def rate_app(username,stars):
    file = open("rating","r+")
    file.seek(0, os.SEEK_END)
    file.write(f"{username}:{stars}\t")
    file.flush()

def alter_user_tendencies(value):
    if value == "rock":
        update_tendencies(0,1,0)
    if value == "paper":
        update_tendencies(0,0,1)
    if value == "scissors":
        update_tendencies(1,0,0)


if __name__ == '__main__':
    reset_values()