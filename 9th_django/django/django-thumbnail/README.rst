=====
thumbnailapp
=====
 
 
thumbnailapp is a simple Django app to conduct Web-based thumbnailapp. For each
question, visitors can choose between a fixed number of answers.
 
Detailed documentation is in the "docs" directory.
 
Quick start
-----------
 
1. Add "thumbnailapp" to your INSTALLED_APPS setting like this::
 
    INSTALLED_APPS = [
        ...
        'thumbnailapp',
    ]
 
2. Include the thumbnailapp URLconf in your project urls.py like this::
 
    path('thumbnailapp/', include('thumbnailapp.urls')),
 
3. Run `python manage.py migrate` to create the thumbnailapp models.
 
4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a thumbnailapp (you'll need the Admin app enabled).
5. Visit http://127.0.0.1:8000/thumbnailapp/ to participate in the thumbnailapp.