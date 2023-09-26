from datetime import date
def test(month, year): 
    return str(date(year,month,13).strftime("%A")=='Friday')
print(test(3,2020))
