function make1() {
  const arr = []

  for (var i = 0; i < 5; i++) {
    arr.push(function () {
      console.log(i)
    })
  }
  return arr
}

const array_of_functions1 = make1()

console.log(`Return value of function:`)
array_of_functions1[0]() // returns 5

function make2() {
  const arr = []

  for (let j = 0; j < 5; j++) {
    arr.push(function () {
      console.log(j)
    })
  }
  return arr
}

const array_of_functions2 = make2()


console.log(`Return value of function:`) // returns 0
array_of_functions2[0]()
