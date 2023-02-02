import urllib.request

def bytes_to_mb(bytes):
    return bytes / (1024**2)


def percent_use(user_bytes, total_bytes):
    return (user_bytes / total_bytes) * 100

def extract_data(file_url):
    with urllib.request.urlopen(file_url) as file:
        data = file.read().decode('utf-8')
    return data

def create_report(data):
    users = {}
    total_bytes = 0
    for line in data.split("\n"):
        if len(line.split(",")) < 2:
            continue
        user, bytes_str = line.split(",", 1)
        bytes = int(bytes_str)
        total_bytes += bytes
        users[user] = {"bytes": bytes, "mb": bytes_to_mb(bytes)}
    for user in users:
        users[user]["percent_use"] = percent_use(users[user]["bytes"], total_bytes)
    with open("relatorio.txt", "w") as file:
        for user in users:
            file.write(f"{user}: {users[user]['mb']}MB ({users[user]['percent_use']:.2f}%)\n")
    return users

data = extract_data("https://raw.githubusercontent.com/f360-dev/provas/master/usuarios.txt")
users = create_report(data)