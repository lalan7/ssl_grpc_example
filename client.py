import grpc

import service_pb2
import service_pb2_grpc


def main():
    host = 'localhost'
    port = 8080

    stub = service_pb2_grpc.ServerStub(channel)
    stub.Foo(service_pb2.Empty())

if __name__ == '__main__':
    main()
