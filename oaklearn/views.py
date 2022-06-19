from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'oaklearn/index.html')



def contacts(request):
    return HttpResponse("find email below \n chewe.kasonde@outlook.com")

def about(request):
    # Rendering the about us page
    return render(request,'oaklearn/about.html')