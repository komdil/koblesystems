Create a Customer
================

**POST /api/customers**

Request:

.. code-block:: json

   {
       "FirstName": "John",
       "LastName": "Doe",
       "Email": "john.doe@example.com"
   }

Response:

.. code-block:: json

   {
       "@odata.context": "/api/$metadata#Customers/$entity",
       "Id": 1,
       "FirstName": "John",
       "LastName": "Doe",
       "Email": "john.doe@example.com"
   }
