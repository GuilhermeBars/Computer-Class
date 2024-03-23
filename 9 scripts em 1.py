#1 Calcular sucessor e antecessor
Numero_Inteiro = int(input('Digite um numero para saber seu sucessor e antecessor: '))

Antecessor = Numero_Inteiro - 1
Sucessor = Numero_Inteiro + 1
print (f'O numero {Numero_Inteiro}, tem o sucessor {Sucessor} e o antecessor {Antecessor}.')

#2 Calcular a area de um triangulo

Base = float(input('Digite o tamanho da base: '))
Altura = float(input('Digite o tamanho da altura: '))
Area = Base * Altura / 2
print (f"O tamanho da area de um triangulo com base {Base}, e altura {Altura}, tem uma area de {Area}")

#3 Calcular reajuste de salario

Salario_Atual = float(input("Digite o valor do salario atual: "))
Reajuste = float(input("Digite o valor do reajuste em porcentagem: "))
valor_reajuste = Salario_Atual * Reajuste / 100
Salario_reajustado = Salario_Atual + valor_reajuste
print (f"O valor do salario era {Salario_Atual}, e agora apos o reajuste e de {Salario_reajustado}")

#4 Calculo de consumo de combustivel

consumo = float(input("Digite o valor do consumo de combustivel em litros: "))
distancia = float(input("Digite a distancia percorida pelo veiculo em kilometros: "))
consumoemmkml = distancia/consumo
print(f"O valor de consumo do seu veiculo e de {consumoemmkml} KM/L")

#5 Calcule o volume do cubo

Lado = float(input('Insira o tamanho do lado do cubo:'))
Volume = Lado**3
print (f"O volume total do cubo e igual a: {Volume}")  

#6 Calculadora de custo para piso por m**2

Comprimento = float(input("Digite o tamanho do comprimento em metros: "))
Largura = float(input("Digite o tamanho da largura em metros: "))
PrecoM2 = float(input("Digite o tamanho do preco por metro quadrado: "))
M2 = Comprimento * Largura
RealPreco = M2 * PrecoM2
print (f"Para forrar um piso de {M2} metros quadrados sera necessario gastar {RealPreco} reais")

#7 Calculadora de IMC

peso = float(input("Insira o peso em kilogramas: "))
altura = float(input("Insira a altura em metros: "))
imc = peso/ altura**2
print (f"O Indice de Massa Corporal de uma pessoa de {peso} Kg e {altura}m e igual a {imc}")

#8 Calculadora de distribuicao de premios

premio = float(input("Insira o valor do premio a ser dividido: "))
primeirolugar = premio * 46 / 100
segundolugar = premio * 32 / 100
terceirolugar = premio - primeirolugar - segundolugar
print (f"O valor do premio do primeiro lugar e: {primeirolugar}: ")
print (f"O valor do premio do segundo lugar e: {segundolugar}: " )
print (f"O valor do premio do terceiro lugar e: {terceirolugar}: ")

#9 Progama de caixa

valorcompra = float(input("Digite o valor da compra: "))
valorpago = float(input("Digite o valor pago pelo cliente:"))
troco = valorpago - valorcompra
print ("O valor a ser pago e : {valorcompra}")
print ("O valor pago foi: {valorpago}")
print (f"O valor do troco sera: {troco}")







              
                    

            
