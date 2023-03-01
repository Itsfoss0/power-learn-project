/*
type casting in dart
*/

void main(){
  // type casting 

  String two = "2";
  int number = 34;
  double dbl = 33.0;

  print(int.parse(two));
  print(number.runtimeType);
  print(dbl.toString());
  print(dbl.toString().runtimeType);
  print(dbl.toStringAsFixed(2));
}