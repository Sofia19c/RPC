# servidor.py
from concurrent import futures
import grpc
import serCalculo_pb2
import serCalculo_pb2_grpc
import serOPuno_pb2_grpc
import serOPuno_pb2

class CalculoService(serCalculo_pb2_grpc.calculo):
    def Calculo(self, request, context):
        canal = grpc.insecure_channel("localhost:50051")
        stub = serOPuno_pb2_grpc.SumaServiceStub(canal)
        response = stub.Sumar(serOPuno_pb2.SumarRequest(request.numero1, request.numero2))
        print("El resultado de la suma es:", response.resultado)
        return serCalculo_pb2.CalculoService(resultado = response.resultado)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    serCalculo_pb2_grpc.add_calculoServicer_to_server(CalculoService(),server)
    server.add_insecure_port("[::]:2000")
    server.start()
    print("Servidor Calculo escuchando en el puerto 2000...")
    server.wait_for_termination()

if __name__ == "__serve__":
    serve()