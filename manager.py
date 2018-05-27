import os
# os.chdir('/Users/host_z/Desktop/Manager/information_29')
# from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db

#
# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# redis = StrictRedis(host = Config.REDIS_HOST,port = Config.REDIS_PORT)
#
#
# CSRFProtect(app)
# Session(app)
# 脚本管理对象
app = create_app("unit")



manager = Manager(app)

# 数据库迁移
Migrate(app,db)
# 数据库添加到manager
manager.add_command("mysql",MigrateCommand)



@app.route("/")
def index():
    # from flask import session
    # session["name"] = "haahhaha"
    return "ok page"

if __name__ == "__main__":
    manager.run()


