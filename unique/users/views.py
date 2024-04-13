from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User


def index(request):

    return render(request,"index.html")
    # template = loader.get_template("index.html")
    
    # user_list = User.objects.all().values()

    # context = {
    #     "user_list":user_list
    # }

    # return HttpResponse(template.render(context))

def About(request):
    template = loader.get_template("About.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context)) 

def All(request):
    template = loader.get_template("All.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))   

def blog_1(request):
    template = loader.get_template("blog-details1.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def blog_2(request):
    template = loader.get_template("blog-details2.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))   

def blog_3(request):
    template = loader.get_template("blog-details3.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))   

def blog(request):
    template = loader.get_template("blog.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def contact(request):
    template = loader.get_template("Contact.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context)) 

def events(request):
    template = loader.get_template("events.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))  

def gallary(request):
    template = loader.get_template("gallary.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))   

def interview(request):
    template = loader.get_template("interview.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))   

def login(request):
    template = loader.get_template("login.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))  

def offers(request):
    template = loader.get_template("offers.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def path(request):
    template = loader.get_template("Path.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))  

def portfolio_2(request):
    template = loader.get_template("portfolio-details-2.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context)) 

def portfolio_3(request):
    template = loader.get_template("portfolio-details-3.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))

def portfolio_4(request):
    template = loader.get_template("portfolio-details-4.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context)) 

def portfolio_5(request):
    template = loader.get_template("portfolio-details-5.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))  

def portfolio_6(request):
    template = loader.get_template("portfolio-details-6.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))  

def portfolio(request):
    template = loader.get_template("portfolio-details.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))  

def privacy(request):
    template = loader.get_template("privacy.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context)) 

def search(request):
    template = loader.get_template("search.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))  

def service(request):
    template = loader.get_template("services-details.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context)) 

# def signup(request):
#     template = loader.get_template("signup.html")
    
#     user_list = User.objects.all().values()

#     context = {
#         "user_list":user_list
#     }

#     return HttpResponse(template.render(context))           

def sitemap(request):
    template = loader.get_template("sitemap.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))  

def swiper(request):
    template = loader.get_template("swiper.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))  

def terms(request):
    template = loader.get_template("terms.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context)) 

def testimonial(request):
    template = loader.get_template("testimonial.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))  

def verify(request):
    template = loader.get_template("verify-cert.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context)) 

def Why_Unique(request):
    template = loader.get_template("Why_Unique.html")
    
    user_list = User.objects.all().values()

    context = {
        "user_list":user_list
    }

    return HttpResponse(template.render(context))                        