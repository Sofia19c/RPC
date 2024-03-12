# servidor.py
from concurrent import futures
import grpc
import serOPdos_pb2
import serOPdos_pb2_grpc

class RestaService(serOPdos_pb2_grpc.RestaServiceServicer):
    def Resta(self, request, context):
        resultado = request.numero3 - request.numero4
        return serOPdos_pb2.RestaResponse(resultado=resultado)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    serOPdos_pb2_grpc.add_RestaServiceServicer_to_server(RestaService(), server)
    server.add_insecure_port("[::]:3000")
    server.start()
    print("Servidor OPdos escuchando en el puerto 3000...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()