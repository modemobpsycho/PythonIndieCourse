digit = int(input("Введите цифру: "))

match digit:
    case 0 | 3 | 6 | 9:
        print("Без остатка делятся на 3")
    case 1 | 4 | 7:
        print("При делении на 3 дают остаток 1")
    case 2 | 5 | 8:
        print("При делении на 3 дают остаток 2")
    case  _:
        print(f"{digit} не является цифрой")




