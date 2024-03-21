from django.shortcuts import render
from .models import destinationPlaces, offerDeals


# Create your views here.
def home(request):
    dest1=offerDeals()
    dest1.place='Chennai'
    dest1.price=10000
    dest1.img='chennai.jpg'
    dest1.description='place of chennai'

    dest2=offerDeals()
    dest2.place='Kerala'
    dest2.price=12000
    dest2.img='kerala.jpg'
    dest2.description='place of kerala'

    dest3=offerDeals()
    dest3.place='Bangalore'
    dest3.price=9000
    dest3.img='bangalore.jpg'
    dest3.description='place of bangalore'

    dest4=offerDeals()
    dest4.place='Hyderabad'
    dest4.price=8000
    dest4.img='hyderabad.jpg'
    dest4.description='place of hyderabad'

    dests=[dest1,dest2,dest3,dest4]
    return render(request,"home.html",{'dests':dests})


#create a views here destination page rendering
def destinations(request):
    destplace1=destinationPlaces()
    destplace1.place='Chennai'
    destplace1.price=10000
    destplace1.img='chennai.jpg'
    destplace1.description='place of chennai'

    destplace2=destinationPlaces()
    destplace2.place='Kerala'
    destplace2.price=12000
    destplace2.img='kerala.jpg'
    destplace2.description='place of kerala'

    destplace3=destinationPlaces()
    destplace3.place='Bangalore'
    destplace3.price=9000
    destplace3.img='bangalore.jpg'
    destplace3.description='place of bangalore'

    destplace4=destinationPlaces()
    destplace4.place='Hyderabad'
    destplace4.price=8000
    destplace4.img='hyderabad.jpg'
    destplace4.description='place of hyderabad'

    destplace5=destinationPlaces()
    destplace5.place='Delhi'
    destplace5.price=8000
    destplace5.img='delhi.jpg'
    destplace5.description='place of delhi'

    destplace6=destinationPlaces()
    destplace6.place='Maldives'
    destplace6.price=15000
    destplace6.img='maldives.jpg'
    destplace6.description='place of maldives'

    destplace7=destinationPlaces()
    destplace7.place='Manali'
    destplace7.price=20000
    destplace7.img='manali.jpg'
    destplace7.description='place of manali'
    
    destplace8=destinationPlaces()
    destplace8.place='Mumbai'
    destplace8.price=13000
    destplace8.img='mumbai.jpg'
    destplace8.description='place of mumbai'

    destplace9=destinationPlaces()
    destplace9.place='Goa'
    destplace9.price=10000
    destplace9.img='goa.jpg'
    destplace9.description='place of goa'

    destplace10=destinationPlaces()
    destplace10.place='Jammu & Kashmir'
    destplace10.price=15000
    destplace10.img='jammu.jpg'
    destplace10.description='place of Jammu and Kashmir'


    destplaces=[destplace1,destplace2,destplace3,destplace4,destplace5,destplace6,destplace7,destplace8,destplace9,destplace10]
    return render(request,"destinations.html",{'destplaces':destplaces})
   


