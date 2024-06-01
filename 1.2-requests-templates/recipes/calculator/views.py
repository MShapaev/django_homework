from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def dishes(request, dish):
    count_person = int(request.GET.get('servings', 1))
    print(count_person)
    recipe = DATA[dish]
    amount = {k:v*count_person for (k,v) in recipe.items()}
    context = {'recipe': amount}
    return render(request, 'calculator/index.html', context)
