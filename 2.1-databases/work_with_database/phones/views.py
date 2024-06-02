from django.shortcuts import render, redirect, HttpResponse
from phones.models import Phone
from django.utils.text import slugify


def index(request):
    return redirect('catalog')


def show_catalog(request, sort=None):
    template = 'catalog.html'
    phones_object = Phone.objects.all()
    phones = [{'name': p.name, 'image': p.image, 'price': p.price, 'slug': p.slug} for p in phones_object]
    # print(phones)
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = sorted(phones, key=lambda x: x['name'])
    if sort == 'min_price':
        phones = sorted(phones, key=lambda x: x['price'])
    if sort == 'max_price':
        phones = sorted(phones, key=lambda x: x['price'], reverse=True)
    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product_objects = Phone.objects.filter(slug=slug)
    for p in product_objects:
        phone = {'name': p.name, 'image': p.image, 'release_date': p.release_date, 'price': p.price, 'slug': p.slug,
                 'lte_exists': p.lte_exists}

    context = {
        'phone': phone
    }
    return render(request, template, context)


def import_csv(request):
    """"Необходимо после запуска севера перейти по пути <ваш сайт>/import/   для автоматического наполнения базы данных из CSV файла"""
    f = open('phones.csv', 'r')
    res = f.readlines()
    for line in res[1:]:
        line = line.split(';')
        phone = Phone()
        phone.id = line[0]
        phone.name = line[1]
        phone.image = line[2]
        phone.price = line[3]
        phone.release_date = line[4]
        phone.lte_exists = line[5]
        slug = slugify(line[1])
        phone.slug = slug
        phone.save()

    f.close()
    return HttpResponse('Наполнили базу данных из CSV файла')
