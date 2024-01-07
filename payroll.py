# create a function to calculate various taxes for an employee
# see instructions for details

# Ryan Dennis

# Define Function
def calc_payroll_tax(gross_pay):
    medicare = gross_pay * 0.0145
    futa = gross_pay * 0.006

    # Social Security tax amount employer submits to IRS
    ss_tax_employer = gross_pay * 0.062

    # Additional Social Security tax amount the "employee" pays to the IRS
    ss_tax_employee = gross_pay * 0.062

    total_tax = medicare + futa + ss_tax_employee
    net_pay = gross_pay - total_tax

    # Print Statements
    print(f"Gross Pay: $ {gross_pay:.2f}")
    print(f"Medicare Tax: $ {medicare:.2f}")
    print(f"FUTA Tax: $ {futa:.2f}")
    print(f"Social Security Tax paid by employer: $ {ss_tax_employer:.2f}")
    print(f"Social Security Tax paid by employee: $ {ss_tax_employee:.2f}")
    print(f"Total Payroll Tax paid by employee: $ {total_tax:.2f}")
    print(f"Net Pay: $ {net_pay:.2f}")
