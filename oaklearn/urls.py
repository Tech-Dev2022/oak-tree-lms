from django.urls import path
from . import views

urlpatterns = [
     path('index/', views.index),
     path('contacts/', views.contacts),
     path('about/', views.about),
          
]

# Change URL patterns to make learning application 
"""

     These pages must include
          1. Home
          2. Revision Guides 
               # Main Page Shows Education Level (Varsity, High School, Primary Level, Nursery)
               # Second Level Subject Based Revision
                    # Critical Sub level is admin specific entries of new courses.
               

          3. Oak App
          4. About Us 
          5. Contacts
          6. Dashboard App
               # Applications Include 
                    # Learning Stage 
                    # Score Counter 
                    # Machine Learning Driven Text Recognition 
     # Key Factors are the optimization of user experience 
          
     """
