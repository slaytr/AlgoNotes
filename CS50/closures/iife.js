// immediately invoked function expression
// non iife
function hello() {
  var message = 'hello!'

  function say() {
    console.log(message)
  }
  return say
}

const sayhello = hello()

// iife
const sayhello2 = (function() {
  var message = 'hello!'

  function say() {
    console.log(message)
  }
  return say
})()

sayhello2()

// iife example, count variable is not accessible in the global scope

const counter = function() {
  let count = 0
  return {
    inc: function() {
      count = count + 1
    },
    get: function() {
      console.log(count)
    }
  }
}()

counter.get()
counter.inc()
counter.inc()
counter.get()

// iife example
function makeArr() {
  let myarr = []
  for (let i = 0; i < 5; i++) {
    // myarr.push(function() {console.log(i)})
    myarr.push(function(){
      return function(x) {console.log(x)}(i)
    })
  }
  return myarr
}

const test_arr = makeArr()
test_arr[0]()
