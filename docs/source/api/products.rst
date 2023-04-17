===============
User Endpoints
===============

.. contents::
   :local:
   :depth: 1

User Registration
=================

**Endpoint:** /api/v1/users/register

**Method:** POST

**Request Example:**

.. code-block:: json

   {
       "username": "johndoe",
       "email": "johndoe@example.com",
       "password": "mysecurepassword"
   }

**Response Example (Success):**

.. code-block:: json

   {
       "status": "success",
       "message": "User registered successfully.",
       "data": {
           "id": 1,
           "username": "johndoe",
           "email": "johndoe@example.com"
       }
   }

**Response Example (Error):**

.. code-block:: json

   {
       "status": "error",
       "message": "Email already exists."
   }

.. note::

   In case of an error, a detailed message will be provided in the "message" field.

