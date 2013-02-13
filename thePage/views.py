from django.http import HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import render_to_response, get_object_or_404
import random

def base(request):
    l1 = []
    l2 = []
    l3 = []
    hexs = []
    l1.append(random.randint(300,5000))
    l2.append(random.randint(300,5000))
    l3.append(random.randint(300,5000))
    hexs.append('00');
    for i in range(255):
        l1.append(random.randint(1,200))
        l2.append(random.randint(1,200))
        l3.append(random.randint(1,200))
        temp = hex(i+1)
        temp = temp[2:]
        if(len(temp) == 1):
            temp = '0' + temp
        hexs.append(temp)
    
    return render_to_response('thePage/first.html', {'list1': l1, 'list2': l2, 'list3': l3, 'xAxis':hexs})