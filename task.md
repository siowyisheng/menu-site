# Requirements

## Overview

Create the base for a simplified menu platform with REST APIs with an admin access level and a public access level. The code should be layout in an clean organised fashion and functionally complete.

## Submission

Please provide a link to your GitHub repo. It is recommended to do small commits as you work. Language and framework is up to you, but Python Django is desired. The code should be deployable locally.

## Class objects

There is only 1 menu that contains multiple categories (i.e. Drinks, Sandwiches).

Each category can have many items (i.e. Coke, Fanta).

A menu item has the following details:

- item ID
- name
- description
- thumbnail image URL

## Authentication

Only an "admin" level user should have access to creating and deleting menu items, but anyone can view menu items.

## Error Codes

To be determined by the developer

## Bonuses

If you have additional bandwidth, some nice to haves are:

Unit tests
ReadMe's / comments
Basic front end to interact with the APIs

## Endpoints

GET {{url}}/menu
Get the full menu including all categories

GET {{url}}/menu/:categoryID
Get a specific category

POST {{url}}/item/:id
Create a new item or update an existing one

POST {{url}}/category
Create a new category

DEL {{url}/item/:id
Delete a menu item

GET {{url}}/menu?limit=10
Pagination to 10 limited menu items
