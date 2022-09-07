numero=int(input("Digite o primeiro número: "))
numero2=int(input("Digite o segundo número: "))
operacao=input("Digite a  operação desejada: ")
if operacao == "+":
 resultado=numero+numero2
elif operacao == "-":
 resultado=numero-numero2
elif operacao == "*":
 resultado=numero*numero2
elif operacao == "/":
 resultado=numero/numero2
elif operacao == "//":
 resultado=numero//numero2
elif operacao == "%":
 resultado=numero%numero2
else:
 print("erro")
print("O resultado é:", resultado)
