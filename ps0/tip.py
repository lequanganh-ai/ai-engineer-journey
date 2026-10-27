# Soát đề: OK
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #bỏ dấu $ và trả về số thực
    return float(d.replace("$", ""))


def percent_to_float(p):
    #bỏ dấu % và trả về số thực dạng thập phân 
    return float(p.replace("%", ""))/100

main()
