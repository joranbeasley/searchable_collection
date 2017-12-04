searchable_collection
------------------------------
[![Coverage Status](https://coveralls.io/repos/github/joranbeasley/searchable_collection/badge.svg?branch=master)](https://coveralls.io/github/joranbeasley/searchable_collection?branch=master)

## Overview

This package attempts to provide an ORM like interface to searching lists

    my_list = SearchableCollection()
    my_list.extend(some_other_list_of_stuff)
    
    print(my_list.find_one_where(some_attribute__in=["passed","pending"])) 
    print(my_list.find_one_where(some_attribute__not_in=["passed","pending"])) 
    print(my_list.find_one_where(subclass__class_attribute__not_in=["passed","pending"])) 

    print(list(my_list.find_all_where(status__not_in="ok")))
    print(list(my_list.find_all_where(status="waiting")))
    
## Installation

    pip install searchable_collection
    # or
    pip install git+ssh://<gitrepo>
    # or
    # Download Project and 
    python setup.py install

### Requirements

    - python 2.6+
    - python 3    

### Run the tests
 
    pytest tests    
    
## Check out tonnes of examples
 