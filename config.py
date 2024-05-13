class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:qq44882960@127.0.0.1:3306/hourse_data"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False #会打印原生sql语句，便于观察测试
    SECRET_KEY = "123456"