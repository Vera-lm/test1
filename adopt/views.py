from django.shortcuts import render
from django.http import Http404
from django.urls import path
from .models import Sighting

# Create your views here.
 
def map(request):
	squirrels = Sighting.objects.all()[:100]
	context = {'squirrels': squirrels}
	return render(request, 'adopt/index.html', context)

def homepage(request):
    return render(request,'adopt/homepage.html')


def list_squirrel(request):
    sights = Sighting.objects.all()
    fields = ['Unique_Squirrel_ID','Longtitude','Latitude','Date','Shift']
    context = { 'sights':sights, 'fields':fields, }
    return render(request, 'adopt/list.html', context)

def update_squirrel(request,Unique_Squirrel_ID):
    sight = Sighting.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == 'POST':
        form = SquirrelMap(request.POST, instance = sight)
        if form.is_valid():
            form.save()
            return redirect(f'/adopt')
        else:
            return JsonResponse({'errors':form.errors}, status=400)
    else:
        form = SquirrelMap(instance = sight)

    context = { 'form':form, }
    return render(request, 'adopt/update.html', context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelMap(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/adopt/')
    else:
        form = SquirrelMap()

    context = { 'form':form,  }

    return render(request,'adopt/add.html', context)


def stat_squirrel(request):
    try:
        sightings_total = Sighting.objects.count()
        sightings_adult = Sighting.objects.filter(age='Adult').count()
        sightings_juvenile = Sighting.objects.filter(age='Juvenile').count()        
        most_common_date_query = Sighting.objects.values('date').annotate(total=Count('date')).order_by('-total')[0]
        latest_date = Sighting.objects.order_by('date').latest('date').date
        earliest_date = Sighting.objects.order_by('date').earliest().date
        running_true = Sighting.objects.filter(running=True).count()
        running_false = Sighting.objects.filter(running=False).count()
        chasing_true = Sighting.objects.filter(chasing=True).count()
        chasing_false = Sighting.objects.filter(chasing=False).count()
        climbing_true = Sighting.objects.filter(climbing=True).count()
        climbing_false = Sighting.objects.filter(climbing=False).count()    
        has_no_sightings = False
        context = {
                'has_no_sightings': has_no_sightings,
                'sightings_total': sightings_total,
                'sightings_adult': sightings_adult,
                'sightings_juvenile': sightings_juvenile,
                'latest_date': latest_date,
                'earliest_date': earliest_date,
                'most_common_date': most_common_date_query['date'],
                'most_common_date_count': most_common_date_query['total'],
                'running_true': running_true,
                'running_false': running_false,
                'chasing_true': chasing_true,
                'chasing_false': chasing_false,
                'climbing_true': climbing_true,
                'climbing_false': climbing_false,
            }   
    except Exception as e:
        print('No records in database:\n' + str(e))
        has_no_sightings = True
        context = {
                'has_no_sightings': has_no_sightings,
            }
    
    return render(request, 'adopt/stats.html', context)
