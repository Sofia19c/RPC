import grpc
import serCalculo_pb2
import serCalculo_pb2_grpc

def cliente(self, request):
    numero1 = int(input("Por favor, introduce el primer numero"))
    numero2 = int(input("Por favor, introduce el segundo numero"))
    numero3 = int(input("Por favor, introduce el tercer numero"))
    numero4 = int(input("Por favor, introduce el cuarto numero"))

    canal = grpc.insecure_channel("localhost:2000")
    stub = serCalculo_pb2_grpc.calculoStub(canal)
    response = stub.Calculo(serCalculo_pb2.calculoRequest(numero1, numero2, numero3, numero4))
    print("El resultado de la operacion es: ", response.resultado)

if __name__ == "__main__":
    cliente()