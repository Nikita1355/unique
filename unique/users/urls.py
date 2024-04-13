from django.urls import path
from . import views 

urlpatterns = [


    path('', views.index, name='index'),
    
    path('About', views.About, name='About'),

    path('All', views.All, name='All'),

    path('blog-details1', views.blog_1, name='blog-details1'),

    path('blog-details2', views.blog_2, name='blog-details2'),

    path('blog-details3', views.blog_3, name='blog-details3'),

    path('blog', views.blog, name='blog'),

    path('login', views.login, name='login'),

    path('Contact', views.contact, name='Contact'),

    path('events', views.events, name='events'),

    path('gallary', views.gallary, name='gallary'),

    path('interview', views.interview, name='interview'),

    path('offers', views.offers, name='offers'),

    path('Path', views.path, name='Path'),

    path('portfolio-details-2', views.portfolio_2, name='portfolio-details-2'),

    path('portfolio-details-3', views.portfolio_3, name='portfolio-details-3'),

    path('portfolio-details-4', views.portfolio_4, name='portfolio-details-4'),

    path('portfolio-details-5', views.portfolio_5, name='portfolio-details-5'),

    path('portfolio-details-6', views.portfolio_6, name='portfolio-details-6'),

    path('portfolio-details', views.portfolio, name='portfolio-details'),

    path('privacy', views.privacy, name='privacy'),

    path('search', views.search, name='search'),

    path('services-details', views.service, name='services-details'),

    path('sitemap', views.sitemap, name='sitemap'),

    path('swiper', views.swiper, name='swiper'),

    path('terms', views.terms, name='terms'),

    path('testimonial', views.testimonial, name='testimonial'),

    path('verify-cert', views.verify, name='verify-cert'),

    path('Why_Unique', views.Why_Unique, name='Why_Unique'),

]