<p align="center"><img width=20.5% src="https://avatars.githubusercontent.com/u/67179924?s=280&v=4"></p>

***
<h1 align="center">Assignment 7 on closures</h1>
<h4 align="center">Submission by Lohith G N (EPAI batch 3) </h4>

***

 &nbsp;  &nbsp; ![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)  &nbsp;  &nbsp; 
 ![GitHub repo size](https://img.shields.io/github/repo-size/lohith0501/The-School-of-AI-session-7-assignment-lohith0501)  &nbsp;  &nbsp; 
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)  &nbsp;  &nbsp; 
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/lohith0501/The-School-of-AI-session-7-assignment-lohith0501/Session_7-workflow)  &nbsp;  &nbsp; 
![GitHub last commit](https://img.shields.io/github/last-commit/lohith0501/The-School-of-AI-session-7-assignment-lohith0501)  &nbsp;  &nbsp; 
![GitHub Repo stars](https://img.shields.io/github/stars/lohith0501/The-School-of-AI-session-7-assignment-lohith0501?style=social)  &nbsp;  &nbsp; 
![Maintaner](https://img.shields.io/badge/maintainer-Lohith-blue)  &nbsp;  &nbsp; 


## Summary of assignment 
- Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable (+ 4 tests) - 200
- Write a closure that gives you the next Fibonacci number (+ 2 tests) - 100
- We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests) - 250
- Modify above such that now we can pass in different dictionary variables to update different dictionaries (+ 6 tests) - 250
Once done, upload the code to github, run actions, and then proceed to answer S7 - Assignment Solutions. 

## Functions in session 7 main module

There are five main functions in main module as explained below

> docstring_check(fn)
>> Function to check docstring with more than 50 characters
Here we create a function to check and check if this function has docstring with 50 character each. here we create docstring_check function which takes the function who has to be checked as a parameter. here we have defined `min_count` which is the minimun character count. Then we have defined another function `mycount` which is a closure which takes in mincount as non local parameter and then checks its length by fetching the dfocstring of the function. It returns a True if docstring is more than 50 characters else returns false.

> myfibonacci()
>> Function to calculate the next fibonacci number, here we define `first` and `second` number as free variables i.e. will be used by `generate_my_next_number` closure and that closure will add these numbers and further update to return resulatnat sum.

> mycounter(fn)
>> Function to calculate how many times a function is being called, so to do that we define a `mycounter` function with `count` as free variable. Then we defined `inner` function which updates the `count` value and returns it.

> mycounter_with_global_dict(fn)
>> in this functiion we define 4 functions i.e. `add`, `mul`, `sub`, and `div`. in this task we keep a global dictionary `mydict` to have a check on how many times each operation is being called. so here we define a function `mycounter_with_global_dict` which takes in function as a parameter, the free variable `count` is the value obtained from the key of the global dictioanry as function name. Here we define a closure called inner which takes in  `a` and `b` as parameters, which are the numbers over which each operation will be perfomed. The function updated the global dictionary and returns the count

> mycounter_with_global_dict_2(fn, mydict:dict)
>>Function is similar to previous one.Instead of updating in global variable we pass a dictionay as a parameter and that gets updated. 

## Test cases 

There are eighteen test cases in test module and important ones are explained below

| Case name | Description |
| ------ | ----------- |
| test_function_name_had_cap_letter   | capital letter check in functions. |
| test_readme_contents | Checks if readme file contains at least 500 words. |
| test_readme_proper_description    | Checks if contents of readme file are having keywords which are described earlier in list. |
| test_readme_file_for_formatting | Checks if readme file contains at least 25 #. |
| test_readme_exists | Checks if readme file exists. |
| test_docstring_check | Checks if docstring exists. |
|test_myfibonacci | Checks if fibonacci module is working as expected. |
| test_mycounter_with_global_dict | Checks if counter is working as expected when dictionary is passed. |

***

<h1 align="center">Thank you</h1>

***

