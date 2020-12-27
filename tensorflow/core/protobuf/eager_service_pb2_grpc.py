# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from tensorflow.core.protobuf import eager_service_pb2 as tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2


class EagerServiceStub(object):
    """//////////////////////////////////////////////////////////////////////////////

    Eager Service defines a TensorFlow service that executes operations eagerly
    on a set of local devices, on behalf of a remote Eager executor.

    The service impl will keep track of the various clients and devices it has
    access to and allows the client to enqueue ops on any devices that it is able
    to access and schedule data transfers from/to any of the peers.

    A client can generate multiple contexts to be able to independently execute
    operations, but cannot share data between the two contexts.

    NOTE: Even though contexts generated by clients should be independent, the
    lower level tensorflow execution engine is not, so they might share some data
    (e.g. a Device's ResourceMgr).

    //////////////////////////////////////////////////////////////////////////////
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateContext = channel.unary_unary(
                '/tensorflow.eager.EagerService/CreateContext',
                request_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CreateContextRequest.SerializeToString,
                response_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CreateContextResponse.FromString,
                )
        self.UpdateContext = channel.unary_unary(
                '/tensorflow.eager.EagerService/UpdateContext',
                request_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.UpdateContextRequest.SerializeToString,
                response_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.UpdateContextResponse.FromString,
                )
        self.Enqueue = channel.unary_unary(
                '/tensorflow.eager.EagerService/Enqueue',
                request_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueRequest.SerializeToString,
                response_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueResponse.FromString,
                )
        self.StreamingEnqueue = channel.stream_stream(
                '/tensorflow.eager.EagerService/StreamingEnqueue',
                request_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueRequest.SerializeToString,
                response_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueResponse.FromString,
                )
        self.WaitQueueDone = channel.unary_unary(
                '/tensorflow.eager.EagerService/WaitQueueDone',
                request_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.WaitQueueDoneRequest.SerializeToString,
                response_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.WaitQueueDoneResponse.FromString,
                )
        self.RunComponentFunction = channel.unary_unary(
                '/tensorflow.eager.EagerService/RunComponentFunction',
                request_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.RunComponentFunctionRequest.SerializeToString,
                response_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.RunComponentFunctionResponse.FromString,
                )
        self.KeepAlive = channel.unary_unary(
                '/tensorflow.eager.EagerService/KeepAlive',
                request_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.KeepAliveRequest.SerializeToString,
                response_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.KeepAliveResponse.FromString,
                )
        self.CloseContext = channel.unary_unary(
                '/tensorflow.eager.EagerService/CloseContext',
                request_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CloseContextRequest.SerializeToString,
                response_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CloseContextResponse.FromString,
                )


class EagerServiceServicer(object):
    """//////////////////////////////////////////////////////////////////////////////

    Eager Service defines a TensorFlow service that executes operations eagerly
    on a set of local devices, on behalf of a remote Eager executor.

    The service impl will keep track of the various clients and devices it has
    access to and allows the client to enqueue ops on any devices that it is able
    to access and schedule data transfers from/to any of the peers.

    A client can generate multiple contexts to be able to independently execute
    operations, but cannot share data between the two contexts.

    NOTE: Even though contexts generated by clients should be independent, the
    lower level tensorflow execution engine is not, so they might share some data
    (e.g. a Device's ResourceMgr).

    //////////////////////////////////////////////////////////////////////////////
    """

    def CreateContext(self, request, context):
        """This initializes the worker, informing it about the other workers in the
        cluster and exchanging authentication tokens which will be used in all
        other RPCs to detect whether the worker has restarted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateContext(self, request, context):
        """This updates the eager context on an existing worker when updating the set
        of servers in a distributed eager cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Enqueue(self, request, context):
        """This takes a list of Execute and DeleteTensorHandle operations and enqueues
        (in async mode) or executes (in sync mode) them on the remote server.
        All outputs of ops which were not explicitly deleted with
        DeleteTensorHandle entries will be assumed to be alive and are usable by
        future calls to Enqueue.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingEnqueue(self, request_iterator, context):
        """A streaming version of Enqueue.
        Current server implementation sends one response per received request.
        The benefit for using a streaming version is that subsequent requests
        can be sent without waiting for a response to the previous request. This
        synchronization is required in the regular Enqueue call because gRPC does
        not guarantee to preserve request order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaitQueueDone(self, request, context):
        """Takes a set of op IDs and waits until those ops are done. Returns any error
        in the stream so far.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RunComponentFunction(self, request, context):
        """This takes an Eager operation and executes it in async mode on the remote
        server. Different from EnqueueRequest, ops/functions sent through this
        type of requests are allowed to execute in parallel and no ordering is
        preserved by RPC stream or executor.
        This request type should only be used for executing component functions.
        Ordering of component functions should be enforced by their corresponding
        main functions. The runtime ensures the following invarients for component
        functions (CFs) and their main functions (MFs):
        (1) MF1 -> MF2 ==> CF1 -> CF2 ("->" indicates order of execution);
        (2) MF1 || MF2 ==> CF1 || CF2 ("||" indicates possible parallel execution);
        (3) For CF1 and CF2 that come from the same MF, CF1 || CF2
        For executing ops/main functions, use Enqueue or StreamingEnqueue instead
        for correct ordering.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def KeepAlive(self, request, context):
        """Contexts are always created with a deadline and no RPCs within a deadline
        will trigger a context garbage collection. KeepAlive calls can be used to
        delay this. It can also be used to validate the existence of a context ID
        on remote eager worker. If the context is on remote worker, return the same
        ID and the current context view ID. This is useful for checking if the
        remote worker (potentially with the same task name and hostname / port) is
        replaced with a new process.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CloseContext(self, request, context):
        """Closes the context. No calls to other methods using the existing context ID
        are valid after this.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateContext': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateContext,
                    request_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CreateContextRequest.FromString,
                    response_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CreateContextResponse.SerializeToString,
            ),
            'UpdateContext': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateContext,
                    request_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.UpdateContextRequest.FromString,
                    response_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.UpdateContextResponse.SerializeToString,
            ),
            'Enqueue': grpc.unary_unary_rpc_method_handler(
                    servicer.Enqueue,
                    request_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueRequest.FromString,
                    response_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueResponse.SerializeToString,
            ),
            'StreamingEnqueue': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingEnqueue,
                    request_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueRequest.FromString,
                    response_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueResponse.SerializeToString,
            ),
            'WaitQueueDone': grpc.unary_unary_rpc_method_handler(
                    servicer.WaitQueueDone,
                    request_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.WaitQueueDoneRequest.FromString,
                    response_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.WaitQueueDoneResponse.SerializeToString,
            ),
            'RunComponentFunction': grpc.unary_unary_rpc_method_handler(
                    servicer.RunComponentFunction,
                    request_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.RunComponentFunctionRequest.FromString,
                    response_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.RunComponentFunctionResponse.SerializeToString,
            ),
            'KeepAlive': grpc.unary_unary_rpc_method_handler(
                    servicer.KeepAlive,
                    request_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.KeepAliveRequest.FromString,
                    response_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.KeepAliveResponse.SerializeToString,
            ),
            'CloseContext': grpc.unary_unary_rpc_method_handler(
                    servicer.CloseContext,
                    request_deserializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CloseContextRequest.FromString,
                    response_serializer=tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CloseContextResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tensorflow.eager.EagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EagerService(object):
    """//////////////////////////////////////////////////////////////////////////////

    Eager Service defines a TensorFlow service that executes operations eagerly
    on a set of local devices, on behalf of a remote Eager executor.

    The service impl will keep track of the various clients and devices it has
    access to and allows the client to enqueue ops on any devices that it is able
    to access and schedule data transfers from/to any of the peers.

    A client can generate multiple contexts to be able to independently execute
    operations, but cannot share data between the two contexts.

    NOTE: Even though contexts generated by clients should be independent, the
    lower level tensorflow execution engine is not, so they might share some data
    (e.g. a Device's ResourceMgr).

    //////////////////////////////////////////////////////////////////////////////
    """

    @staticmethod
    def CreateContext(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tensorflow.eager.EagerService/CreateContext',
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CreateContextRequest.SerializeToString,
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CreateContextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateContext(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tensorflow.eager.EagerService/UpdateContext',
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.UpdateContextRequest.SerializeToString,
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.UpdateContextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Enqueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tensorflow.eager.EagerService/Enqueue',
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueRequest.SerializeToString,
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingEnqueue(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/tensorflow.eager.EagerService/StreamingEnqueue',
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueRequest.SerializeToString,
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.EnqueueResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WaitQueueDone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tensorflow.eager.EagerService/WaitQueueDone',
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.WaitQueueDoneRequest.SerializeToString,
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.WaitQueueDoneResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RunComponentFunction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tensorflow.eager.EagerService/RunComponentFunction',
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.RunComponentFunctionRequest.SerializeToString,
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.RunComponentFunctionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def KeepAlive(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tensorflow.eager.EagerService/KeepAlive',
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.KeepAliveRequest.SerializeToString,
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.KeepAliveResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CloseContext(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tensorflow.eager.EagerService/CloseContext',
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CloseContextRequest.SerializeToString,
            tensorflow_dot_core_dot_protobuf_dot_eager__service__pb2.CloseContextResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)