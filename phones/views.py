from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', '')
    template = 'catalog.html'
    phones = list(Phone.objects.all().values())
    context = {'phones': phones}
    if sort == 'min_price' or sort == 'max_price':
        for i in range(len(phones)):
            lowest_value_index = i
            for j in range(i + 1, len(phones)):
                if phones[j]['price'] < phones[lowest_value_index]['price']:
                    lowest_value_index = j
            phones[i], phones[lowest_value_index] = phones[lowest_value_index], phones[i]
        if sort == 'min_price':
            context = {'phones': phones}
        if sort == 'max_price':
            context = {'phones': phones[::-1]}
    if sort == 'name':
        for i in range(len(phones)):
            lowest_value_index = i
            for j in range(i + 1, len(phones)):
                if phones[j]['name'] < phones[lowest_value_index]['name']:
                    lowest_value_index = j
            phones[i], phones[lowest_value_index] = phones[lowest_value_index], phones[i]
        context = {'phones': phones}

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = list(Phone.objects.filter(slug=slug).values())
    context = {'phone': phone[0]}
    return render(request, template, context)
