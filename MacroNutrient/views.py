from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.
def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        consume = Consume(user=request.user, food_consumed=consume)
        consume.save()

    
    foods = Food.objects.all()
    consumed_foods = Consume.objects.filter(user=request.user)
    context = {
        'foods':foods,
        'consumed_foods':consumed_foods,
    }
    return render(request, 'index.html', context)


def delete_item(request, id):
    consumed_food = Consume.objects.get(id=id)
    consumed_food.delete()
    return redirect('/')
