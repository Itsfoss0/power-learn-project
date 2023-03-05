import 'dart:io';

void main(){
     print("Enter a number");
     String?  number = stdin.readLineSync().toString();
     determineNumber(int.parse(number));
}

void determineNumber(int number){
     if (number > 10){
     	print("Your number is greater than 10");
     }else if (number < 10){
     	print("Your number is less than 10");
     }else{
        print("Your number is equal to 10");
     }

}