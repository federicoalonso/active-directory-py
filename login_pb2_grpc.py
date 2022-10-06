# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import login_pb2 as login__pb2


class LoginServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LoginUser = channel.unary_unary(
                '/login.LoginService/LoginUser',
                request_serializer=login__pb2.LoginRequest.SerializeToString,
                response_deserializer=login__pb2.LoginReply.FromString,
                )


class LoginServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LoginUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LoginServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LoginUser': grpc.unary_unary_rpc_method_handler(
                    servicer.LoginUser,
                    request_deserializer=login__pb2.LoginRequest.FromString,
                    response_serializer=login__pb2.LoginReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'login.LoginService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LoginService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LoginUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/login.LoginService/LoginUser',
            login__pb2.LoginRequest.SerializeToString,
            login__pb2.LoginReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
