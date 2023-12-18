import signal
from concurrent import futures

import grpc

import time

import service_pb2
import service_pb2_grpc


class ServerServicer(service_pb2_grpc.ServerServicer):
    def Foo(self, request, context):
        return service_pb2.Empty(message='Hello! Current time is ' + time.ctime())

def main():
    port = '8080'

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    service_pb2_grpc.add_ServerServicer_to_server(ServerServicer(), server)

    server.add_secure_port('[::]:'+port, server_credentials)

    server.start()
    try:
        while True:
            signal.pause()
    except KeyboardInterrupt:
        pass
    server.stop(0)

if __name__ == '__main__':
    main()
