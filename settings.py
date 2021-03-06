import os

#设置templates路径：
template_path = os.path.join(os.path.dirname(__file__), "templates")

#设置静态文件解析路径：
static_path = os.path.join(os.path.dirname(__file__), "static"),

#设置防跨站请求攻击：
xsrf_cookies = True,
#默认为False，即不可防御。

#设置登陆路径，未登陆用户在操作时跳转会用到这个参数：
login_url = "/login-do",
#默认为@tornado.web.authenticated

#设置调试模式：
debug = True,
#默认为False，即不是调试模式。

#设置cookie密钥：
cookie_secret = "ettdskftehisdjklagkfdee!@e+_kla"
#默认为字符串"secure cookies"

#设置是否自动编码：在2.0以上需要设置此项来兼容您之前的APP
autoescape = None,
#不设置默认为自动编码。

#设置template_loader，可以从独立的路径中导入template：
template_loader=None,
#其中utils为自己定义的模块，ZipLoader是tornado.template.BaseLoader的子类。

#设置gzip压缩：
gzip=True

#设置静态路径头部：
static_url_prefix = "/mystatic/",
#默认是"/static/"

#设置静态文件处理类：
static_handler_class = None,
#默认是tornado.web.StaticFileHandler

#设置静态文件的参数：
static_handler_args = { "key1":"value1", "key2":"value2"  }
#默认为空字典。

#设置日志处理函数
log_function = None,
# 日志处理函数your_fun，按照自己的意图记录日志。