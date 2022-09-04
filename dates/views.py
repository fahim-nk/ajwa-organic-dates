from urllib.robotparser import RequestRate
from django.shortcuts import render
import pickle
import joblib




# Create your views here.
def home(request):
    return render(request, 'index.html')
    # if request.method == "GET":
    #     designation = request.GET['designation']
    #     age = request.GET['age']
    #     location = request.GET['location']
    #     disease = request.GET['disease']
    #     print(designation, age, location, disease)



def result(request):
    list=[]
    
    list.append(request.GET['designation'])
    list.append(request.GET['age'])
    # list.append(request.GET['location'])
    list.append(request.GET['disease'])



    list2=[]

    if request.GET['designation'] == "business":
        list2.append(0)
    elif request.GET['designation'] == "farmer":
        list2.append(1)
    elif request.GET['designation'] == "Unemployment":
        list2.append(2)
    elif request.GET['designation'] == "pvtsector":
        list2.append(3)
    elif request.GET['designation'] == "gvt":
        list2.append(4)

    list2.append(request.GET['age'])
    # if request.GET['location'] == "Palakkad":
    #     list2.append(7)
    # elif request.Get['location'] =="Calicut":
    #     list2.append()
    # list2.append(request.GET['location'])
    if request.GET['disease'] == "yes":
        list2.append(1)
    elif request.GET['disease'] == "no":
        list2.append(0)

   
   
    print(list2)

    model = joblib.load('Random1_forest.sav')
    answer = model.predict([list2])
    if answer == 0:
        answ='economy'
    elif answer == 1:

        answ='ordinary'
    elif answer == 2:
        answ='good'
    elif answer == 3:
        answ='premium'
    elif answer == 4:
        answ='delux'
    else:
        answ='please enter correcct information'
    # context = {'list' : list2, 'answer': answer}
    return render(request, 'result.html', {'answ':answ})




