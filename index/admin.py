from django.contrib import admin


from .models import Article, Category, Comment



class FilterByTitle(admin.SimpleListFilter):
    title = "عنوان های پرتکرار"
    parameter_name = "title"

    def lookups(self, request, model_admin):
        return {
            ('tate', "تیت"),
            ('musk', "ماسک"),
        }
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(title__icontains = self.value())


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "descr", "star")
    list_filter = ("star", FilterByTitle)
    list_editable = ("star",)


admin.site.register(Category)
admin.site.register(Comment)
