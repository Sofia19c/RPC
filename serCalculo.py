# servidor.py
from concurrent import futures
import grpc
import serCalculo_pb2
import serCalculo_pb2_grpc

class CalculoService(serCalculo_pb2_grpc.calculo):
    def Calculo(self, request, context):
        resultado= request.numero1 
        return serCalculo_pb2.CalculoService()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    serCalculo_pb2_grpc.add_calculoServicer_to_server(CalculoService(),server)
    server.add_insecure_port("[::]:2000")
    server.start()
    print("Servidor Calculo escuchando en el puerto 2000...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()