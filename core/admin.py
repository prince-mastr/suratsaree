from django.contrib import admin

from .models import (
    Item, OrderItem, Order, Payment, Coupon, Refund,
    Address, UserProfile, Variation, ItemVariation ,Category,
    SharedItem, Share, Sharelist, Item_Images , Transport
)


class PropertyImageInline(admin.TabularInline):
    model = Item_Images
    extra = 3

def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'dispatched',
                    'shipping_address',
                    'billing_address',
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
    ]
    list_filter = ['ordered',
                   'dispatched',
                   ]
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


class ItemVariationAdmin(admin.ModelAdmin):
    list_display = ['variation',
                    'value',
                    'attachment']
    list_filter = ['variation', 'variation__item']
    search_fields = ['value']

class ItemAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['stock','category__name']
    inlines = [ PropertyImageInline, ]


class ItemVariationInLineAdmin(admin.TabularInline):
    model = ItemVariation
    extra = 1


class VariationAdmin(admin.ModelAdmin):
    list_display = ['item',
                    'name']
    list_filter = ['item']
    search_fields = ['name']
    inlines = [ItemVariationInLineAdmin]

class UserAdmin(admin.ModelAdmin):
    list_filter = ['rate_type']

admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(SharedItem)
admin.site.register(Share)
admin.site.register(Sharelist)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile, UserAdmin)
admin.site.register(Category)
admin.site.register(Transport)

""" admin.site.register(ItemVariation, ItemVariationAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund) """

