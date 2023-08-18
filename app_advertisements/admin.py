from django.contrib import admin
from .models import Advertisements
# Register your models here.
#регистрируем модель
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at','auction', 'updated_at', 'image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title','description', 'image'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, qertyset):
        qertyset.update(action=False)
    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, qertyset):
        qertyset.update(action=True)

admin.site.register(Advertisements, AdvertisementsAdmin)