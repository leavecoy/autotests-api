import grpc

import user_service_pb2
import user_service_pb2_grpc
import day_info_service_pb2
import day_info_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub_user = user_service_pb2_grpc.UserServiceStub(channel)
stub_info = day_info_service_pb2_grpc.DayInfoServiceStub(channel)

response_user = stub_user.GetUser(user_service_pb2.GetUserRequest(username="Alice"))
response_day_info = stub_info.GetInfo(day_info_service_pb2.GetDayInfoRequest(username="Alice"))
print(response_user, response_day_info, sep="\n")