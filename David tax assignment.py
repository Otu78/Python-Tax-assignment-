# Simple Personal Income Tax Calculator (2009)

def compute_tax(status, income):
    rates = {
        0: [(8350,0.10),(33950,0.15),(82250,0.25),(171550,0.28),(372950,0.33),(10**18,0.35)],
        1: [(16700,0.10),(67900,0.15),(137050,0.25),(208850,0.28),(372950,0.33),(10**18,0.35)],
        2: [(8350,0.10),(33950,0.15),(68525,0.25),(104425,0.28),(186475,0.33),(10**18,0.35)],
        3: [(11950,0.10),(45500,0.15),(117450,0.25),(190200,0.28),(372950,0.33),(10**18,0.35)]
    }

    tax = 0
    last = 0

    for limit, rate in rates[status]:
        if income > limit:
            tax += (limit - last) * rate
            last = limit
        else:
            tax += (income - last) * rate
            break

    return tax


status = int(input("Enter filing status (0=Single, 1=Married joint, 2=Married separate, 3=Head): "))
income = float(input("Enter taxable income: $"))

tax = compute_tax(status, income)
print("Your tax is: $", round(tax, 2))
