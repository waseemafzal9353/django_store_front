from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import F, Func, Value, Count, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from store.models import Customer, Order, OrderItem, Product
from tags.models import TaggedItem

def say_hello(request):
    # query_set = Order.objects.all().prefetch_related('orderitem_set__product').select_related('customer').order_by('-placed_at')[:5]
    # query_set = Product.objects.annotate(new_id=F('id'))
    # query_set = Customer.objects.annotate(
    #     full_name=Func(F('first_name'), Value(' '), F('last_name'), function=Func('CONCAT'))
    # )
    # query_set = Customer.objects.annotate(
    #     full_name=Concat('first_name', Value(' '), 'last_name')
    # )
    # grouping data
    # discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField()) 
    # query_set = Customer.objects.annotate(
    #     order_count=Count('order')
    # )
    # query_set = Product.objects.annotate(
    #     discounted_price = discounted_price
    # )
    
    TaggedItem.objects.get_tag_for(Product, 1)
    return render(request, 'hello.html')

