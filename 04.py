status = input("Você é estudante? (sim ou nao)")
if status == "sim":
    desconto = "tem desconto"
else:
    dia = input("Qual o dia da semana?(seg;ter;qua;qui;sex)")
    if dia == "ter":
        sala = input("Qual o tipo de sala?(comum ou vip)")
        if sala == "comum":
            desconto = "tem desconto"
        else:
            desconto = "não tem desconto"
    else:
        desconto = "não tem desconto"
print(f"Você {desconto}")

