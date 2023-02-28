/*
exploring void return functions in dart
*/

void main(){
    sayHello();
    helloArguments("Dart is fun");
    helloOptionalArgs("Hello", "Doe");
    helloOptionalNamedArgs("Hi", name: "Mom!");
}

// explicity tell the function what to print
void sayHello(){
  print("Hello world");
}

// void function that accepts arguments
void helloArguments(String message){
  print(message);
}

//void function with optional - position params

void helloOptionalArgs(String message, [String? name = "John"]){
  print('$message, $name');
}

// void function with optional - named params

void helloOptionalNamedArgs(String message, {String? name = "Doe"}){
  print('$message, $name');
}