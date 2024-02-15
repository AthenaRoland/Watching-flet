class UserDatasChange():
    def __init__(self,filepath, value):
        with open(f"{filepath}", "w", encoding="utf-8") as file:
            file.write(value)
            file.close()