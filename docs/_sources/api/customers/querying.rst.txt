Filter Customers by Email
=========================

**GET /api/customers?$filter=Email eq 'john.doe@example.com'**

Response:

.. code-block:: json

   {
       "@odata.context": "/api/$metadata#Customers",
       "value": [
           {
               "Id": 1,
               "FirstName": "John",
               "LastName": "Doe",
               "Email": "john.doe@example.com"
           }
       ]
   }

Select Specific Fields
======================

**GET /api/customers?$select=FirstName,LastName**

Response:

.. code-block:: json

   {
       "@odata.context": "/api/$metadata#Customers(FirstName,LastName)",
       "value": [
           {
               "FirstName": "John",
               "LastName": "Doe"
           },
           {
               "FirstName": "Jane",
               "LastName": "Smith"
           }
       ]
   }

Order Customers by Last Name
============================

**GET /api/customers?$orderby=LastName**

Response:

.. code-block:: json

   {
       "@odata.context": "/api/$metadata#Customers",
       "value": [
           {
               "Id": 1,
               "FirstName": "John",
               "LastName": "Doe",
               "Email": "john.doe@example.com"
           },
           {
               "Id": 2,
               "FirstName": "Jane",
               "LastName": "Smith",
               "Email": "jane.smith@example.com"
           }
       ]
   }

Pagination
==========

**GET /api/customers?$skip=0&$top=2**

Response:

.. code-block:: json

   {
       "@odata.context": "/api/$metadata#Customers",
       "value": [
           {
               "Id": 1,
               "FirstName": "John",
               "LastName": "Doe",
               "Email": "john.doe@example.com"
           },
           {
               "Id": 2,
               "FirstName": "Jane",
               "LastName": "Smith",
               "Email": "jane.smith@example.com"
           }
       ]
   }
