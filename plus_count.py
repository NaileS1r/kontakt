from static import COUNTER_FILE
def plus_count(name):
    with open(COUNTER_FILE, "r") as f:
        counter = int(f.read())
    filename = f"{name}{counter}.json"
    counter+=1
    with open(COUNTER_FILE, "w") as file:
        file.write(str(counter))
    return filename