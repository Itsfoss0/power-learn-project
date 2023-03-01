/*
functions with optional parameters
* optional positional parameters
* optional named parameters
*/

void main(){
  int numA = 2;
  int sum = optionalPositionalParameters(numA);
  int divide = divideWithName(numA, divisor: 2);
  int divide_2 = divideWithName(numA);
  print('Sum of Addition is: $sum');
  print('Dividing $numA is: $divide');
  print('Dividing $numA without passing divisor: $divide_2');

}

// optional positional parameter
int optionalPositionalParameters(int numA, [int numB = 0]){
  // Add  numA to numB. If numB is not passed
  // Add numA to 0

  return (numA + numB);
}

// optional named parameters

int divideWithName(int number, {int divisor = 1}){
  // divide a number with the divisor
  // if divisor is not passed, 1 will be used

  return (number ~/ divisor);
}