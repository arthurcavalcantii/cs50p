

file = input("File name: ").casefold().strip()
extension = file.rsplit(sep=".")[1]
match extension:
    case "gif" | "jpg" | "jpeg" | "png" :
        print(f"image/{extension}")
    case "pdf" | "zip" :
        print(f"application/{extension}")
    case "txt":
        print(f"text/{extension}")