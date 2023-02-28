/*
Functions that have a return value
*/

void main(){
  int a = 2;
  int b = 3;
  print(compliment("Dart"));
  int sum = add(a, b);
  print('$a + $b is $sum');
  print(isGreater(a, b));
  print(isNegative(num: b));
}

// String return value 
String compliment(String language){
  return ('$language is a nice programming Language');
}

// int return value
int add(int a, int b){
  return (a + b);
}

// bool return value
bool isGreater(int a, int b){
  // return true if `a` is greater than `b`
  return (a > b);
}

// bool return value with defualt parameter
bool isNegative({int num = 0}){
  return (num < 0);
}