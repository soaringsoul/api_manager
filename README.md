# APi管理中心简单说明

----------

## 简介

刚刚接手公司数据管理工作时，有部分工作是要对公司合作的数据供应商，及各供应商提供的数据接口信息进行管理。

这些信息都是以excel文件的形式交接给我的，如果boss或者其他同事想要了解，就必须整理一个excel表格出来提供出去。

但是这些信息又比较敏感，尤其是供应商和接口价格，有是只有boss才能查看，也就是`权限管理`了。

所以就使用`flask-appbuilder`写了这个简单的接口管理中心。主要有以下功能：

1. 记录已接入的所有供应商的接口信息

包括接口名称、供应商、分组、应用平台、价格、计费方式，数据时效性、覆盖范围等

2. 随时新增、删除和修改接口信息

3. 接口信息的查询

4. 接口信息查看权限管理，让指定的用户只能查看指定的字段

后来，以这个为初衷，开始搭建数据中心，把这个`接口管理中心`作为后台管理中的一个功能模块，集成到数据中心去了，这个项目于是又充当了一次`数据中心`-`接口管理中心`的Demo，所以实际中并未使用，写完后，也未进行迭代升级，仅作为记录吧。

## 使用说明

本项目主要使用`flask-appbuilder`，更多设置的细节可以参考[Flask-AppBuilder文档](https://github.com/dpgaspar/Flask-AppBuilder)

### 1 安装依赖

主要使用了以下python库，`pip install -r requirements.txt`安装即可：

	Flask-AppBuilder==1.12.0
	PyMySQL==0.9.2
	SQLAlchemy==1.2.12
	WTForms==2.2.1

### 2 创建管理员账户

运行`fabmanager create-admin`，依次输入用户名、密码等信息。

### 3 启动

* 运行`fabnamnager run`

![create_admin](/screenshots/create_admin.jpg)

* 浏览器打开`http://localhost:8080/`

![login_index](/screenshots/login_index.jpg)



###  4 使用

* 输入 创建的用户名和密码，登录

![logoin_in](/screenshots/logoin_in.jpg)

* 查看所有api信息

![api_info](/screenshots/api_info.jpg)



* 按条件查找api信息

![search](/screenshots/search.jpg)



*  增加或者修改api信息

![add_api](/screenshots/add_api.jpg)