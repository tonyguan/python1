# coding=utf-8
# 代码文件：chapter24/QQ2006/qq_server.py

import json
import logging
import socket
import traceback as tb

from com.zhijieketang.qq.server.user_dao import UserDao

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(threadName)s - '
                           '%(name)s - %(funcName)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# 服务器端IP
SERVER_IP = '127.0.0.1'
# 服务器端端口号
SERVER_PORT = 8888

# 操作命令代码
COMMAND_LOGIN = 1  # 登录命令
COMMAND_LOGOUT = 2  # 下线命令
COMMAND_SENDMSG = 3  # 发消息命令
COMMAND_REFRESH = 4  # 刷新好友列表命令

# 所有已经登录的客户端信息
clientlist = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

logger.info('服务器启动, 监听自己的端口{0}...'.format(SERVER_PORT))

# 创建字节序列对象列表，作为接收数据的缓冲区
buffer = []

# 主循环
while True:
    try:
        # 接收数据报包
        data, client_address = server_socket.recvfrom(1024)
        json_obj = json.loads(data.decode())
        logger.info('服务器接收客户端，消息：{0}'.format(json_obj))

        # 取出客户端传递过来的操作命令
        command = json_obj['command']

        if command == COMMAND_LOGIN:  # 用户登录过程
            # 通过用户Id查询用户信息
            userid = json_obj['user_id']
            userpwd = json_obj['user_pwd']
            logger.debug('user_id:{0}  user_pwd:{1}'.format(userid, userpwd))

            dao = UserDao()
            user = dao.findbyid(userid)
            logger.info(user)

            # 判断客户端发送过来的密码与数据库的密码是否一致
            if user is not None and user['user_pwd'] == userpwd:  # 登录成功
                # 登录成功
                # 创建保存用户登录信息的二元组
                clientinfo = (userid, client_address)
                # 用户登录信息添加到clientlist
                clientlist.append(clientinfo)

                json_obj = user
                json_obj['result'] = '0'

                # 取出好友用户列表
                dao = UserDao()
                friends = dao.findfriends(userid)
                # 返回clientinfo中userid列表
                cinfo_userids = map(lambda it: it[0], clientlist)

                for friend in friends:
                    fid = friend['user_id']
                    # 添加好友状态 '1'在线 '0'离线
                    friend['online'] = '0'
                    if fid in cinfo_userids:  # 用户登录
                        friend['online'] = '1'

                json_obj['friends'] = friends
                logger.info('服务器发送用户成功，消息：{0}'.format(json_obj))

                # JSON编码
                json_str = json.dumps(json_obj)
                # 给客户端发送数据
                server_socket.sendto(json_str.encode(), client_address)
            else:  # 登录失败
                json_obj = {}
                json_obj['result'] = '-1'
                # JSON编码
                json_str = json.dumps(json_obj)
                # 给客户端发送数据
                server_socket.sendto(json_str.encode(), client_address)

        elif command == COMMAND_SENDMSG:  # 用户发送消息

            # 获得好友Id
            fduserid = json_obj['receive_user_id']
            # 向客户端发送数据
            # 在clientlist中查找好友Id
            filter_clientinfo = filter(lambda it: it[0] == fduserid, clientlist)
            clientinfo = list(filter_clientinfo)

            if len(clientinfo) == 1:
                _, client_address = clientinfo[0]

                # 服务器转发消息给客户端
                # JSON编码
                json_str = json.dumps(json_obj)
                server_socket.sendto(json_str.encode(), client_address)

        elif command == COMMAND_LOGOUT:  # 用户发送下线命令
            # 获得用户Id
            userid = json_obj['user_id']
            for clientinfo in clientlist:
                cuserid, _ = clientinfo
                if cuserid == userid:
                    # 从clientlist集合中删除用户
                    clientlist.remove(clientinfo)
                    break

            logger.info(clientlist)

        # 刷新用户列表
        # 如果clientlist中没有元素时跳到下次循环
        if len(clientlist) == 0:
            continue

        json_obj = {}
        json_obj['command'] = COMMAND_REFRESH
        usersid_map = map(lambda it: it[0], clientlist)
        useridlist = list(usersid_map)
        json_obj['OnlineUserList'] = useridlist
        # logger.info("服务器向客户端发送消息，刷新用户列表：{0}".format(json_obj))

        for clientinfo in clientlist:
            _, address = clientinfo
            # JSON编码
            json_str = json.dumps(json_obj)
            # 给客户端发送数据
            server_socket.sendto(json_str.encode(), address)

    except Exception:
        tb.print_exc()
        logger.info('timed out')
