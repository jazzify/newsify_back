Common
==============
Common app keeps every common folder and models

Common models
--------------------
``BaseModel`` is the base model, used for every other model it adds a ``created_at`` field to every model and change the way we set a unique identifier to every model instance

Common docs
--------------------
``Common`` also holds the documentation stuff, we use `ReDoc <https://github.com/Redocly/redoc>`_ for the ``api`` documentation and `Sphinx <https://www.sphinx-doc.org/en/master/>`_ for the ``backend`` app documentation.

- **ReDoc**

    - We used the `Django rest framework <https://www.django-rest-framework.org/topics/documenting-your-api/#a-minimal-example-with-redoc>`_ example given to create the minimal ``ReDoc`` documentation.

    - We also use `this guide <https://www.django-rest-framework.org/api-guide/schemas/>`_ to generate the ``OpenAPI`` schema.
