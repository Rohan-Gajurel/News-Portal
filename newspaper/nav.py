from newspaper.models import Category

def navigation(request):
    categories =Category.objects.all()
    return {
        'categories': categories }