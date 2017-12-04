searchable_collection
------------------------------
[![Build Status](https://travis-ci.org/joranbeasley/searchable_collection.svg?branch=master)](https://travis-ci.org/joranbeasley/searchable_collection)
[![Coverage Status](https://coveralls.io/repos/github/joranbeasley/searchable_collection/badge.svg?branch=master)](https://coveralls.io/github/joranbeasley/searchable_collection?branch=master)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/870c467e59784d86bd598a5d5d928bbd)](https://www.codacy.com/app/joranbeasley/searchable_collection?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=joranbeasley/searchable_collection&amp;utm_campaign=Badge_Grade)
[![Documentation Status](https://readthedocs.org/projects/searchablecollection/badge/?version=latest)](http://searchablecollection.readthedocs.io/en/latest/?badge=latest)
  

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
    
# Check out tonnes of examples
# [READ THE DOCS!!](http://searchablecollection.readthedocs.io/en/latest/)
 [![Documentation Status](https://readthedocs.org/projects/searchablecollection/badge/?version=latest)](http://searchablecollection.readthedocs.io/en/latest/?badge=latest)
  
 