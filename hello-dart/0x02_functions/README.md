## Functions in Dart
Functions are an essential part of any programming lanuguage. In Dart ( or pretty much all the programming languages), functions are used to encapsulate a piece of code that can be called and executed multiple times with different input parameters. They help to organize code, improve readability, and reduce redundancy by allowing you to group related pieces of code together into reusable modules. In this way, functions play a crucial role in making code more efficient and maintainable, and they are a fundamental building block of the Dart programming Language. Primarily, functions emphasize the concept of DRY - Do not repeat yourself.


Before we look at what kind of functions dart supports, lets have a look at the anatomy of a function in the dart programming language. 

```
return_type function_name (parameter lists){
    function logic

    return (value)
}

```
Lets quickly look at how what types of functions dart supports

1. __Void functions__: These sort of functions don't return any value after they are executed. They also have a ```void``` return value in the function definition body
2. __Anonymous functions__: These sort of functions are also called anonymous functions
The general syntax of these functions is 
```
(Datatype <parameters>){
    // logic
}
```

They can also be assigned to a variable. Here is what I mean

```dart
var add = (int a, int b){
    return (a + b);
};
```
3. __Arrow functions__: Just as the name suggest, these are arrow functions