import os

class NOTE:
    def __init__(self, Title, PW):
        self.Title = Title
        self.PW = PW

def CreatingNote(content):
    global exit
    while True:
        Title, PW = input("\nCreate note -> title of note | PW : ").split()
        if Title in [line.split()[0] for line in content.splitlines() if line.strip()]:
            print("error : title in use.")
            continue
        try:
            PW = int(PW)
        except ValueError:
            print("error : Password must be entered in numbers.")
            continue
        break
    User = NOTE(Title, PW)
    exit = 1
    with open("noteList.txt", "a", encoding="utf-8") as f:
        f.write(f"\n{User.Title} {User.PW}")
    filename = f"{User.Title}.txt"
    open(filename, "a", encoding="utf-8").close()
    os.system(f"notepad.exe {filename}")

def matching(Title, PW):
    with open("noteList.txt", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 2: continue
            saved_title, saved_pw = line.strip().split()    
            if Title == saved_title and PW == saved_pw:
                return True
    return False

exit = 0

while exit == 0:
    Start = input("1. 노트 목록 + 실행\n2. 노트 생성\n3. 노트 삭제\n")

    with open("noteList.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    with open("noteList.txt", "r", encoding="utf-8") as f:
        content = f.read()

    if Start == "1": # Note list
        print("\n")
        if not lines:
            print("노트가 없습니다.\n")
            CreatingNote(content)
            exit = 1
        else:
            for i in lines:
                i = i.strip()
                if not i: continue
                title = i.split()[0]
                print(title)
                
            Title, PW = input("\nTitle of note | PW : ").split()
            User = NOTE(Title, PW)

            if matching(User.Title, PW):
                filename = f"{User.Title}.txt"
                open(filename, "a", encoding="utf-8").close()
                os.system(f"notepad.exe {filename}")
                exit = 1
            else:
                print("Not found\n")
                CreatingNote(content)
                exit = 1

    elif Start == "2": # Create note
        CreatingNote(content)
        exit = 1

    elif Start == "3": # Delete note
        Title, PW = input("\n삭제를 원하는 노트 (Title of note | PW) -> ").split()
        User = NOTE(Title, PW)
        if matching(User.Title, PW):
            print("Delete successful\n")

            new_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) < 2: continue
                saved_title, saved_pw = line.strip().split()
                if not (saved_title == User.Title and saved_pw == User.PW):
                    new_lines.append(f"{saved_title} {saved_pw}\n")

            with open("noteList.txt", "w", encoding="utf-8") as f:
                f.writelines(new_lines)

            note_file = f"{Title}.txt"
            if os.path.exists(note_file):
                os.remove(note_file)
        
        else: print("Not found\n")

    else:
        print("다시 입력하세요.\n")