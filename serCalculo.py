from concurrent import futures
import grpc
import time
import serCalculo_pb2
import serCalculo_pb2_grpc
import serOPuno_pb2_grpc
import serOPuno_pb2
import serOPdos_pb2_grpc
import serOPdos_pb2

class CalculoService(serCalculo_pb2_grpc.calculoServicer):
    def grpc_call_with_retry(self, stub_method, request, max_attempts=2, initial_backoff=1):
        backoff = initial_backoff
        for attempt in range(max_attempts):
            try:
                response = stub_method(request)
                return response
            except grpc.RpcError as e:
                print(f"Hubo un fallo en el RPC: {e.code()}, Intentando de nuevo en {backoff} segundos...")
                time.sleep(backoff)
                backoff *= 2  # Exponential backoff
        return None

    def suma_local(self, numero1, numero2):
        return numero1 + numero2

    def resta_local(self, numero3, numero4):
        return numero3 - numero4

    def Calculo(self, request, context):
        canalUno = grpc.insecure_channel("localhost:50051")
        stubUno = serOPuno_pb2_grpc.SumaServiceStub(canalUno)
        responseSuma = self.grpc_call_with_retry(stubUno.Sumar, serOPuno_pb2.SumarRequest(numero1=request.numero1, numero2=request.numero2))
        if responseSuma is None:
            print("Fallo al conectar con el servicio de suma, realizando operación localmente.")
            resultadoSuma = self.suma_local(request.numero1, request.numero2)
        else:
            resultadoSuma = responseSuma.resultado
        print("El resultado de la suma es: ", resultadoSuma)
        
        canalDos = grpc.insecure_channel("localhost:3000")
        stubDos = serOPdos_pb2_grpc.RestaServiceStub(canalDos)
        responseResta = self.grpc_call_with_retry(stubDos.Resta, serOPdos_pb2.RestaRequest(numero3=request.numero3, numero4=request.numero4))
        if responseResta is None:
            print("Fallo al conectar con el servicio de resta, realizando operación localmente.")
            resultadoResta = self.resta_local(request.numero3, request.numero4)
        else:
            resultadoResta = responseResta.resultado
        print("El resultado de la resta es: ", resultadoResta)

        return serCalculo_pb2.calculoResponse(resultado=resultadoSuma * resultadoResta)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    serCalculo_pb2_grpc.add_calculoServicer_to_server(CalculoService(), server)
    server.add_insecure_port("[::]:2000")
    server.start()
    print("Servidor de cálculo escuchando en el puerto 2000...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
