agua = 500
leche = 300
cafe = 100
dinero = 0

menu = {
        "espresso": {"agua": 50, "leche": 0, "cafe": 18, "precio": 1.5},
            "latte": {"agua": 200, "leche": 150, "cafe": 24, "precio": 2.5},
            "capuccino": {"agua": 250, "leche": 100, "cafe": 24, "precio": 3.0}
            }
eleccion = input("Elije tu tipo de cafe: (espresso/latte/capuccino): ")

def verificar_recursos(eleccion):
    bebida = menu[eleccion]
    if bebida["agua"] > agua:
        print("No hay suficiente agua para el pedido")
        return False
    if bebida["leche"] > leche:
        print("No hay suficiente leche para el pedido")
        return False
    
    def procesar_pago(precio):
    monedas = float(input("Ingrese el dinero ($): "))
    if monedas < precio:
        print("Dinero insuficiente. Retire las monedas...")
        
        return False
    else;