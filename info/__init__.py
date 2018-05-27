# from logging.handlers import RotatingFileHandler
""""""
from logging.handlers import RotatingFileHandler
import sys


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import *
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import configs
import logging
import logging.config
from logging import StreamHandler
# from logging.handlers import RotatingFileHandler
import os.path


db = SQLAlchemy()

class Logging(StreamHandler):
    def __init__(self,filename = "logs/log"):
        self.baseFilename = os.path.abspath(filename)
        """
        Open the current base file with the (original) mode and encoding.
        Return the resulting stream.
        """
        super(Logging, self).__init__()

def set_log(level):
    # 设置 志的记录等级
    # sys.path.append('logs')
    logging.basicConfig(level=level)
    # 调试debug级
    # 创建 志记录 ，指明 志保存的 径、每个 志 件的最   、保存的 志 件个数上限
    # logging.config.fileConfig("logs")
    # logger = logging.getLogger('logs')

    file_log_handler = RotatingFileHandler(filename= "logs/log",maxBytes=1024 * 1024 * 100,backupCount=10)

    # print(RotatingFileHandler("logs"))
    # print(os.path.abspath("logs/log"))

    # 创建 志记录的格式  志等级 输  志信息的 件名  数  志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的 志记录 设置 志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的 志 具对象(flask app使 的)添加 志记录
    logging.getLogger().addHandler(file_log_handler)





def create_app(config_name):

    log =configs[config_name]
    set_log(log.LEVEL_LOG)


    app = Flask(__name__)

    app.config.from_object(configs[config_name])
    db.init_app(app)

    redis = StrictRedis(host =configs[config_name].REDIS_HOST,port = configs[config_name].REDIS_PORT)




    CSRFProtect(app)
    Session(app)
    return app