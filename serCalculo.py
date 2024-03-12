# servidor.py
from concurrent import futures
import grpc
import serCalculo_pb2
import serCalculo_pb2_grpc
import serOPuno_pb2_grpc
import serOPuno_pb2
import serOPdos_pb2_grpc
import serOPdos_pb2

class CalculoService(serCalculo_pb2_grpc.calculo):
    def CalculoSuma(self, request, context):
        canalUno = grpc.insecure_channel("localhost:50051")
        stub = serOPuno_pb2_grpc.SumaServiceStub(canalUno)
        response = stub.Sumar(serOPuno_pb2.SumarRequest(numero1= request.numero1, numero2= request.numero2))
        print("El resultado de la suma es:", response.resultado)
        return serCalculo_pb2.calculoResponse(resultado = response.resultado)

    def CalculoResta(self, request, context):
        canalDos = grpc.insecure_channel("localhost: 3000")
        stub = serOPdos_pb2_grpc.RestaServiceStub(canalDos)
        response = stub.Resta(serOPdos_pb2.RestaRequest(numero3=request.numero3, numero4=request.numero4))
        print("El resultado de la resta es:", response.resultado)
        return serCalculo_pb2.calculoResponse(resultado= response.resultado)

def serveSuma():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    serCalculo_pb2_grpc.add_calculoServicer_to_server(CalculoService(),server)
    server.add_insecure_port("[::]:2000")
    server.start()
    print("Servidor Calculo escuchando en el puerto 2000...")
    server.wait_for_termination()

if __name__ == "__main__":
    serveSuma()