import grpc
import serCalculo_pb2
import serCalculo_pb2_grpc

def cliente():
    n1 = int(input("Por favor, introduce el primer numero: "))
    n2 = int(input("Por favor, introduce el segundo numero: "))
    n3 = int(input("Por favor, introduce el tercer numero: "))
    n4 = int(input("Por favor, introduce el cuarto numero: "))

    canal = grpc.insecure_channel("localhost:2000")
    stub = serCalculo_pb2_grpc.calculoStub(canal)
    response = stub.Calculo(serCalculo_pb2.calculoRequest(numero1 = n1, numero2 = n2, numero3 = n3, numero4 = n4))
    print("El resultado de la operacion es: ", response.resultado)

if __name__ == "__main__":
    cliente()