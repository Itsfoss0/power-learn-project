#!/usr/bin/env node
const person = {
    name: ["John", "Doe"],
    age: 32,
    bio() {
      console.log(`${this.name[0]} ${this.name[1]} is ${this.age} years old.`);
    },
    introduction() {
      console.log(`Hi! I'm ${this.name[0]}.`);
    },
  };
  
person.bio();
person.introduction();