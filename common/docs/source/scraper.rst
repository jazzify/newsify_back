Scraper
===============

Scraper is the core app used to scrape the websites, parse the information and save it in its respective models.


Scraper admin 
--------------------
Make the posts modifiables in the admin

Just add the following code to add a simple model view:
::

   from scraper.models import Post

   admin.site.register(Post)

You can also check the following link for a better approach:
https://docs.djangoproject.com/en/dev/ref/contrib/admin/

Scraper models 
---------------------
We are gonna find the Post model in here which is basically every post in the app the goal is to have a new ``post`` for every new news on each news platform

``post_type`` is the way we can differentiate between news platforms posts

Every other field is well self-explanatory.

Scraper serializers 
--------------------------
The ``PostSerializer`` is responsable to serialize the ``Post`` model.
By now this gonna return every field.


Scraper services 
-----------------------
We have the ``ScraperManager`` this is the core of the hole project due to is its responsability to scrape every news platform looking for the most recent post and save it into our DB


Scraper tests 
--------------------
TODO


Scraper views 
--------------------
``PostViewSet`` will handle our ``posts`` methods logic, it haves all the methods inherited from ``ModelViewSet``.


Scraper commands
--------------------
``scrape`` command is gonna be used to scrape every post on the news platforms using the ``ScraperManager`` is gonna be used as a cronjob
