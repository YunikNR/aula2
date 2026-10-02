# Perguntando qual é a idade
idade = int(input("Qual a sua idade?"))
# Se a idade não corresponder a condição, então ele vai para baixo. se sim, ele vai pra dentro do if.
if 2 <= idade < 18:
    altura = int(input("Qual a sua altura em centimetros?"))
    # Se ele atende à essa condição, então não precisa perguntar se tem autorização.
    if idade >= 12 and altura >= 140:
        system = "Acesso liberado!"
    # Se a altura for menor que 50cm (que é a altura minima de um recem nascido) ele falará:
    elif altura <= 50:
        system = "A altura miníma é 50cm"
    # Se ele não atende à condição, então ele precisa de autorização.
    else:
        autorizacao = input("Seus responsáveis autorizam (sim ou não)?")
        if autorizacao == "sim":
            system = "Acesso liberado!"
        elif autorizacao == "não":
            system = "Acesso Negado."
        # Se ele digitar outra coisa ele terá essa resposta:
        else:
            system = "A resposta tem que ser *sim* ou *não*."
# Se ele tem maior de 18 anos, não precisa perguntar outras coisas, pois o brinquedo não é para maiores de 18 anos.
elif idade >= 18:
    system = "O brinquedo não pode maiores de 18 anos."
# Se essa condição ser verdadeira, não tem sentido um recem nascido saber escrever
elif idade == 0 or idade == 1:
    system = "Você em teoria, não era pra saber escrever..."
# Qualquer resposta além dessa, só pode ser negativa.
else:
    system = "A idade não pode ser negativa!"
# Falar para o client
print(system)
