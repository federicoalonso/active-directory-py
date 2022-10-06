from getpass import getpass
from json import dumps
import re
from easyad import EasyAD
from concurrent import futures
import time
import grpc
import login_pb2
import login_pb2_grpc

class LoginService(login_pb2_grpc.LoginServiceServicer):
    def LoginUser(self, request, context):
        print("Login Service was invoked")
        login_reply = login_pb2.LoginReply()
        login_reply.ok = self.login(request.username, request.password)
        return login_reply
    
    def login(username, password):

        config = dict(AD_SERVER="ServidorAD",
                AD_DOMAIN="dominio.local")
                #   , CA_CERT_FILE="myrootca.crt")
        ad = EasyAD(config)
        # Authenticate a user
        # username = input("Username: ")
        # password = getpass("Password: ")

        local_admin_group_name = "Domain Admins"

        user = ad.authenticate_user(username, password, json_safe=True)

        # ad.config["AD_BIND_USERNAME"] = "user"
        # ad.config["AD_BIND_PASSWORD"] = "VeryDifficoultPassword"

        if user:
            # Successful login! Let's print your details as JSON
            print(dumps(user, sort_keys=True, indent=2, ensure_ascii=False))

            # Lets find out if you are a member of the "LocalAdministrators" group
            # print(ad.user_is_member_of_group(user, local_admin_group_name))
            return True
        else:
            print("Those credentials are invalid. Please try again.")
            return False

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    login_pb2_grpc.add_LoginServiceServicer_to_server(LoginService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()



if __name__ == "__main__":
    serve()