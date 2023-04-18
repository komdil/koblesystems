Update a Customer
================

**PUT /api/customers({id})**

Request:

.. code-block:: json

   {
       "FirstName": "Jane",
       "LastName": "Doe",
       "Email": "jane.doe@example.com"
   }

Response:

.. code-block:: json

   {
       "@odata.context": "/api/$metadata#Customers/$entity",
       "Id": 1,
       "FirstName": "Jane",
       "LastName": "Doe",
       "Email": "jane.doe@example.com"
   }
