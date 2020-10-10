has_high_income = False
has_good_credit = True
has_criminal_record = True

if has_high_income and has_good_credit: # Mesmo que if x && y
    print("Eligible for loan")
if has_high_income or has_good_credit:  # Mesmo que if x || y
    print("Eligible for loan")
if has_good_credit and not has_criminal_record: # Se x e nao-y
    print("Eligible for loan")