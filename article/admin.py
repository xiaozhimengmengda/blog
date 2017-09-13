from django.contrib import admin
from .models import Article
from .models import Category

admin.site.site_header = '小智的blog'
admin.site.site_title = '小智的blog'


class ArticleAdmin(admin.ModelAdmin):
    # 控制展示的字段
    list_display = ['title', 'create_time', 'description']
    # 创建和修改是展示的字段
    # fields
    # 可以查询的字段
    search_fields = ['title', 'create_time']
    # actions 操作动作
    actions = None

    # 重写过滤显示，只显示status=0的信息
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(status=0)

    # 重写admin删除中调用的是这样方法，修改model为逻辑删除
    def delete_model(self, request, obj):
        obj.status = 1
        obj.save()

    class Media:
        js = (
            '/static/kindeditor/kindeditor-min.js',
            '/static/kindeditor/lang/zh_CN.js',
            '/static/kindeditor/config.js'
        )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'create_time', 'status']
    search_fields = ['name', 'create_time']
    actions = None

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(status=0)

    def delete_model(self, request, obj):
        obj.status = 1
        obj.save()

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
