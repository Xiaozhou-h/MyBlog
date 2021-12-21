from django.contrib import admin
from .models import MyUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'name',
                    'introduce', 'company', 'profession',
                    'address', 'telephone', 'wx', 'qq', 'wb', 'photo']
    # 在修改界面添加mobile,qq,weChat的信息输入框
    # 将源码的UserAdmin.fieldsets转换成列表格式
    fieldsets = list(UserAdmin.fieldsets)
    # 重写UserAdmin的fieldsets，添加模型字段信息录入
    fieldsets[1] = (_('Personal info'),
                    {'fields': ('name', 'introduce', 'email', 'company',
                                'profession', 'address', 'telephone',
                                'wx', 'qq', 'wb', 'photo')})

    # 根据当前用户名设置数据访问权限
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(id=request.user.id)
# Register your models here.
