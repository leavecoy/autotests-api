import grpc
from concurrent import futures
import user_service_pb2
import user_service_pb2_grpc
import day_info_service_pb2
import day_info_service_pb2_grpc
from datetime import datetime, date

class UserServiceServicer(user_service_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        print(f"Получен запрос к методу GetUser от пользователя: {request.username}")
        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}")

class DayInfoServiceServicer(day_info_service_pb2_grpc.DayInfoServiceServicer):
    def GetInfo(self, request, context):
        print(f"Получен запрос к методу GetInfo от пользователя {request.username}")
        return day_info_service_pb2.GetDayInfoResponse(
            info=f"Текущая дата: {date.today()}, время: {datetime.now().time()}"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_service_pb2_grpc.add_UserServiceServicer_to_server(UserServiceServicer(), server)
    day_info_service_pb2_grpc.add_DayInfoServiceServicer_to_server(DayInfoServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC сервер запущен на порту 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()




