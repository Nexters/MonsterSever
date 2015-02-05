from django.contrib import admin
from users.models import User, Payment

# admin.TabularInline 상속도 가능함!
class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 3 # has_many form 을 최소 3개 만듬


class UserAdmin(admin.ModelAdmin):
  # form 에 나올 필드들 명시
  fieldsets = [
      (None,               {'fields': ['name']}),
      ('Date information', {'fields': ['age'], 'classes': ['collapse']}), # collapse 기본으로 접혀있는.
  ]
  inlines = [PaymentInline]
  list_display = ('name', 'age') # index 에서 보여질 field
  list_filter = ['login_date'] # 필터 생성
  search_fields = ['name','age'] # 검색 필드

admin.site.register(User, UserAdmin)

