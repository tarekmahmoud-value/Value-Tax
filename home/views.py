from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render
def tax_calculation_view(request):
    context = {}
    if request.method == "POST":
        gross_salary = request.POST.get("gross_salary")
        net_salary = request.POST.get("net_salary")
        social_option = request.POST.get("social_option")
        context = calculate_tax_and_social(gross_salary, net_salary, social_option)
    return render(request, "tax_calculation.html", context)


def calculate_tax_and_social(gross_salary=None, net_salary=None, social_option=None):
    if gross_salary and net_salary:
        return {"error": "You can only enter Gross Salary or Net Salary, not both."}

    result = {
        "gross_salary": gross_salary,
        "net_salary": net_salary,
        "social_insurance_employee": 0,
        "social_insurance_company": 0,
        "family_martyrs": 0,
        "monthly_tax": 0,
        "employee_cost": 0,
    }

    # التأمينات
    if gross_salary:
        gross_salary = float(gross_salary)
        if social_option == "25":
            social_employee = (gross_salary / 1.25) * 0.11
            social_company = (gross_salary / 1.25) * 0.1875
        elif social_option == "30":
            social_employee = (gross_salary / 1.30) * 0.11
            social_company = (gross_salary / 1.30) * 0.1875
        elif social_option == "total":
            base_salary = min(gross_salary, 12600)
            social_employee = base_salary * 0.11
            social_company = base_salary * 0.1875
        else:
            social_employee = 0
            social_company = 0

        # أسر الشهداء
        family_martyrs = gross_salary * (0.0005)

        # احتساب الضريبة
        monthly_tax = tax_formula(gross_salary, social_employee)

        # تكلفة الموظف
        employee_cost = gross_salary + social_company

        # الراتب الصافي
        net_salary = gross_salary - (social_employee + monthly_tax + family_martyrs)

        result.update({
            "gross_salary": gross_salary,
            "net_salary": net_salary,
            "social_insurance_employee": social_employee,
            "social_insurance_company": social_company,
            "family_martyrs": family_martyrs,
            "monthly_tax": monthly_tax,
            "employee_cost": employee_cost,
        })

    return result


def tax_formula(income, insurances):
    insurances = (insurances * (0.11)) * 12
    income = (income * 12) - (20000 + insurances)
    income = (int(income / 10)) * 10

    if income <= 40000:
        tax = 0
    elif income <= 55000:
        tax = (income - 40000) * 0.1
    elif income <= 70000:
        tax = (income - 55000) * 0.15 + 1500
    elif income <= 200000:
        tax = (income - 70000) * 0.2 + 1500 + 2250
    elif income <= 400000:
        tax = (income - 200000) * 0.225 + 1500 + 2250 + 26000
    elif income <= 600000:
        tax = (income - 400000) * 0.25 + 1500 + 2250 + 26000 + 45000
    elif income <= 1200000:
        tax = (income - 400000) * 0.25 + 1500 + 2250 + 26000 + 45000 + \
              (4000 if income <= 700000 else 6750 if income <= 800000 else 10250 if income <= 900000 else 15250)
    else:
        tax = (income - 1200000) * 0.275 + 300000

    return tax / 12  # Monthly tax
