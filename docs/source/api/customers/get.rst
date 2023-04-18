Retrieve a Customer
===================

**GET /api/customers({id})**

Response:

.. code-block:: json

   {
       "@odata.context": "/api/$metadata#Customers/$entity",
       "Id": 1,
       "FirstName": "John",
       "LastName": "Doe",
       "Email": "john.doe@example.com"
   }
