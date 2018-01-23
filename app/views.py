from flask_appbuilder import ModelView
from flask import redirect
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_appbuilder.actions import  action
from .models import DataService, Providers, Function, Apigroup, Salesmethod, Applicationplatform,\
    Apitype, Signcontract, Remarks, Sales, Presentsales
from app import appbuilder, db
from flask_appbuilder.widgets import ListThumbnail, ListWidget, ListItem, ListBlock, ShowBlockWidget, ListLinkWidget


class DataServiceModelView(ModelView):
    datamodel = SQLAInterface(DataService)

    base_order = ('api_name', 'desc')
    label_columns = {'api_name': '数据接口', 'function': '功能说明', 'provider': '数据供应商',
                      'sales_method': '计费方式', 'api_group': '接口分组', 'sales': '服务商报价',
                     'Application_plat': '使用平台', 'input_params': '输入参数', 'sign_contract': '合同事宜',
                     'output_result': '返回结果', 'api_type': '适用类型', 'application_plat': '应用平台',
                     'remarks': '备注', 'present_sales': '当前价格'
                     }
    # 定义查看界面，显示的字段
    # list_columns = ['api_name', 'provider', 'function', 'api_group', 'input_params', 'output_result',
    #                 'sales',  'sales_method', 'application_plat', 'api_type',
    #                 'sign_contract', 'remarks' ]
    list_columns = ['api_name', 'provider', 'function', 'api_group',
                    'application_plat', 'api_type', 'sign_contract', 'present_sales', 'sales_method', 'remarks']
    # 定义添加记录界面显示的各个字段
    add_columns = ['name', 'provider', 'input_params', 'output_result', 'present_sales',
                    'sales', 'function', 'api_group', 'sales_method',
                    'application_plat', 'api_type', 'sign_contract', 'remarks',
                   'begin_date', 'end_date'
                    ]
    edit_columns = ['name', 'provider', 'input_params', 'output_result','present_sales'
                    'sales', 'function', 'api_group', 'sales_method',
                    'application_plat', 'api_type', 'sign_contract', 'remarks'
                    ]

    # expand 表示是否展开组

    edit_fieldsets = [
        (
            '基本信息',
            {'fields': ['name', 'provider', 'input_params', 'output_result', 'sales', 'function', 'api_group',
                        'present_sales',
                        'sales_method']}),
        (
            '数据接口应用信息',
            {'fields': ['application_plat', 'api_type', 'sign_contract', 'remarks', 'begin_date',
                        'end_date'], 'expanded': True}),
    ]
    show_fieldsets = [
        (
            '基本信息',
            {'fields': ['name', 'provider', 'input_params', 'output_result', 'function', 'api_group',
                        'sales', 'sales_method']}),
        (
            '数据接口应用信息',
            {'fields': ['application_plat', 'api_type', 'sign_contract', 'remarks', 'begin_date',
                        'end_date'], 'expanded': True}),
    ]
    add_fieldsets = [
        (
            '基本信息',
            {'fields': ['name', 'provider', 'input_params', 'output_result', 'function', 'api_group', 'sales',
                        'sales_method']}),
        (
            '数据接口应用信息',
            {'fields': ['present_sales', 'application_plat', 'api_type', 'sign_contract', 'remarks', 'begin_date',
                        'end_date'], 'expanded': True}),
    ]

    @action("muldelete", "删除", "确定要删除选中的项目吗", "fa-rocket", single=False)
    def muldelete(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())

    add_title = "添加数据接口"
    edit_title = '编辑记录'

    # 在输入框下添加说明文字
    description_columns = {'name': '数据接口名'}


# 定义数据服务商视图
class ProviderGroupModelView(ModelView):
    datamodel = SQLAInterface(Providers)
    related_views = [DataServiceModelView]
    list_title = '数据供应商列表'


# 定义api分组视图
class ApiGroupModelView(ModelView):
    datamodel = SQLAInterface(Apigroup)
    related_views = [DataServiceModelView]


# 定义价格
class SalesModelView(ModelView):
    datamodel = SQLAInterface(Sales)
    related_views = [DataServiceModelView]


# 定义当前使用的价格
class PresentSalesModelView(ModelView):
    datamodel = SQLAInterface(Presentsales)
    related_views = [DataServiceModelView]

# 定义计费方式视图
class SalesMethodModelView(ModelView):
    datamodel = SQLAInterface(Salesmethod)
    related_views = [DataServiceModelView]


# 定义api功能分组视图
class FunctionModelView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [DataServiceModelView]


# 定义应用平台视图
class ApplicationPlatformModeView(ModelView):
    datamodel = SQLAInterface(Applicationplatform)
    related_views = [DataServiceModelView]


# 定义适用类型视图
class ApiTypeModelView(ModelView):
    datamodel = SQLAInterface(Apitype)
    related_views = [DataServiceModelView]


# 定义是否签订合同视图
class SignContractModelView(ModelView):
    datamodel = SQLAInterface(Signcontract)
    related_views = [DataServiceModelView]


class RemarksModelView(ModelView):
    datamodel = SQLAInterface(Remarks)
    related_views = [DataServiceModelView]


class DataServiceLinkModelView(DataServiceModelView):
    list_title = '数据接口列表'
    list_widget = ListLinkWidget


db.create_all()
appbuilder.add_view(DataServiceLinkModelView, "数据接口", icon="fa-star",
                    category="数据接口", category_icon="fa-envelope")

appbuilder.add_view(ProviderGroupModelView,"数据供应商",
                    icon="fa-database", category="数据分组-必填项")

appbuilder.add_view(ApiGroupModelView, "接口分组",
                    icon="fa-database", category="数据分组-必填项")

appbuilder.add_view(PresentSalesModelView, "当前采购价格",
                    icon="fa-database", category="数据分组-必填项")

appbuilder.add_view(SalesModelView, "服务商报价",
                    icon="fa-database", category="数据分组-选填项")

appbuilder.add_view(SalesMethodModelView, "计费方式",
                    icon="fa-database", category="数据分组-必填项")

appbuilder.add_view(FunctionModelView, "Api功能分类",
                    icon="fa-database", category="数据分组-必填项")

appbuilder.add_view(ApplicationPlatformModeView, "Api应用平台",
                    icon="fa-database", category="数据分组-必填项")

appbuilder.add_view(ApiTypeModelView, "Api适用对象",
                    icon="fa-database", category="数据分组-必填项")

appbuilder.add_view(SignContractModelView, "合同签订事宜",
                    icon="fa-database", category="数据分组-必填项")

appbuilder.add_view(RemarksModelView, "备注",
                    icon="fa-database", category="数据分组-选填项")

appbuilder.add_link("商户易贷", href="https://easyloan.adas.com/download",
                    icon="fa-android", category="数喆数据-网址导航")


appbuilder.add_link("商户易贷风控web端", href='https://zhimatest.adas.com:81/',
                    icon="fa-check-circle", category="数喆数据-网址导航")