const person = {
  name: "bill",
  greet: function() {
    console.log("my name is " + this.name)
  }
}

person.greet() // prints bill

const greet = person.greet

greet()

console.log(JSON.stringify(person))

// JSON.stringify(obj) | turns object to string, removes functions
// obj.funcName.toString() | stringify functions first to include them
