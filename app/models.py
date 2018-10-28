from sqlalchemy import Column, Integer, String, ForeignKey, Date
from flask_appbuilder.models.decorators import renders
from flask_appbuilder.models.mixins import ImageColumn
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from flask import Markup
import datetime
import uuid


# 定义数据服务商，
class Providers(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 定义数据接口功能类型：欺诈风险评估、信用风险评估、运营风险评估
class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 定义接口分组，如银行卡信息，个人身份验证等
class Apigroup(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=True)

    def __repr__(self):
        return self.name


# 定义计费类型：查得or查询
class Salesmethod(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


# 定义使用平台
class Applicationplatform(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=True)

    def __repr__(self):
        return self.name


# 定义api适用类型：个人，企业
class Apitype(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=True)

    def __repr__(self):
        return self.name


class Signcontract(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Remarks(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=True)

    def __repr__(self):
        return self.name


class Sales(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=True)

    def __repr__(self):
        return self.name


class Presentsales(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)

    def __repr__(self):
        return self.name

# 定义数据时效性
class Updatespeed(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)

    def __repr__(self):
        return self.name

# 定义数据接口覆盖范围
class Coverage(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(500), nullable=False)

    def __repr__(self):
        return self.name

def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


def today_after_a_year():
    return (datetime.datetime.today()  + datetime.timedelta(days=365)).strftime('%Y-%m-%d')


class DataService(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=False, nullable=False)

    # 数据服务商
    provider_id = Column(Integer, ForeignKey('providers.id'), nullable=False)
    provider = relationship("Providers")


    # 定义当前价格
    present_sales = Column(String(500), unique=False, nullable=False)

    # 定义字段显示样式，该字段不会真正写入后台数据库
    @renders('name')
    def api_name(self):
        # will render this columns as bold on ListWidget
        return Markup('<b>' + self.name + '</b>')
    # 服务商报价
    sales = Column(String(500), unique=False, nullable=False)
    # 功能
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")

    # 数据接口分组
    api_group_id = Column(Integer, ForeignKey('apigroup.id'), nullable=False)
    api_group = relationship("Apigroup")
    # api计费方式
    sales_method_id = Column(Integer, ForeignKey('salesmethod.id'), nullable=False)
    sales_method = relationship("Salesmethod")
    # 使用平台
    application_plat_id = Column(Integer, ForeignKey('applicationplatform.id'), nullable=False)
    application_plat = relationship("Applicationplatform")
    # 输入参数
    input_params = Column(String(500),  nullable=True)
    # 输出结果
    output_result = Column(String(500),  nullable=True)
    # 定义接口适用类型，个人还是企业
    api_type_id = Column(Integer, ForeignKey('apitype.id'), nullable=False)
    api_type = relationship("Apitype")

    # 定义数据时效性
    update_speed_id = Column(Integer, ForeignKey('updatespeed.id'), nullable=True)
    update_speed = relationship("Updatespeed")

    # 定义数据覆盖范围
    coverage_id = Column(Integer, ForeignKey('coverage.id'), nullable=True)
    coverage = relationship("Coverage")


    # 是否签订合同
    sign_contract_id = Column(Integer, ForeignKey('signcontract.id'), nullable=False)
    sign_contract = relationship("Signcontract")
    # 特殊情况备注
    remarks = Column(String(1000), unique=False, nullable=False)
    # 定义日期
    begin_date = Column(Date, default=today)
    end_date = Column(Date, default=today_after_a_year)




    def __repr__(self):
        return self.name
