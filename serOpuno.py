# servidor.py
from concurrent import futures
import grpc
import suma_pb2
import suma_pb2_grpc

class SumaService(suma_pb2_grpc.SumaServiceServicer):
    def Sumar(self, request, context):
        resultado = request.numero1 + request.numero2
        return suma_pb2.SumaResponse(resultado=resultado)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    suma_pb2_grpc.add_SumaServiceServicer_to_server(SumaService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Servidor RPC escuchando en el puerto 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()