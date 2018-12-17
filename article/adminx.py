import xadmin
from xadmin import views
from .models import Article
from .models import Category


# 开启后台主题样式选择
class BaseSetting(object):
    enable_themes = True
    user_bootswatch = True


# 后台全局设置
class GlobalSettings(object):
    # 后台标签
    site_title = '小智的blog'
    # 后台页脚
    site_footer = 'python'


class ArticleAdmin:
    # 控制展示的字段
    list_display = ['category','title', 'create_time', 'description', 'title_img']
    # 创建和修改是展示的字段
    # fields
    # 可以查询的字段
    search_fields = ['title', 'create_time']
    # actions 操作动作
    style_fields = {'article':'ueditor'}
    # 直接编辑
    #list_editable = ['article']

    #重写过滤显示，只显示status=0的信息
    def get_context(self):
        context = super(ArticleAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = Category.objects.filter(status=0)
        return context

    # 重写admin删除中调用的是这样方法，修改model为逻辑删除
    def delete_model(self, request, obj):
        obj.status = 1
        obj.save()
    #
    # class Media:
    #     js = (
    #         '/static/kindeditor/kindeditor-min.js',
    #         '/static/kindeditor/lang/zh_CN.js',
    #         '/static/kindeditor/config.js'
    #     )


class CategoryAdmin:
    list_display = ['name', 'create_time', 'status']
    search_fields = ['name', 'create_time']



xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Category, CategoryAdmin)
