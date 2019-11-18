# poo-locadora
Object Oriented Programming project - Rental Store 

## Objective
Create a rental store project in any oriented programming language.  
The store has clients and products.
[Clients](https://github.com/senavs/poo-locadora/blob/master/project/entity/client.py) have id number, name, address, phone and debt. 
They are able to rent any product in the store. 
[Products](https://github.com/senavs/poo-locadora/blob/master/project/entity/product.py) a name and the quantity.
If the client din't give the product back, a fine will placed to the client.
To control clients rents, [Register](https://github.com/senavs/poo-locadora/blob/master/project/entity/register.py) will have the client id and product id.
To salve all the classes and register, [Database](https://github.com/senavs/poo-locadora/blob/master/project/entity/dbase.py) will take care of it.

## Controllers
All classes Client, Product and Register are considered entities and don't have methods to manage the rental store.
To do that, they have [controllers classes](https://github.com/senavs/poo-locadora/tree/master/project/controler).

## Notebooks
To see how the entities and controllers work, there [notebooks](https://github.com/senavs/poo-locadora/tree/master/notebooks) for them.  
###### NOTE: [Register notebook](https://github.com/senavs/poo-locadora/blob/master/notebooks/poo-locadora-register.ipynb) calls all the others classes, so you can see all in register notebook.

# Version
**v1.0**
* Database table and table colletion
* Client class, controller and notebook
* Product class, controller and notebook
* Register class, controller and notebook
