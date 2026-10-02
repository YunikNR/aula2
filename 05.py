inadimplencia = input("Voçê tem histórico de inadimplência?(sim ou não)")
if inadimplencia == "não":
    bens_garantia = input("Você tem bens como garantia?(sim ou não)")
    if bens_garantia == "sim":
        system = "Empréstimo aprovado."
    elif bens_garantia == "não":
        renda_mensal = float(input("Qual a sua renda mensal?"))
        score = int(input("Qual o seu score?"))
    else:
        system = "Resposta inválida"
elif inadimplencia == "sim":
    system = "Empréstimo reprovado."
else:
    system = "Resposta inválida"

