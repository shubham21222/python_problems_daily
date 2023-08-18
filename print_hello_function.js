//qus:-Write a function createHelloWorld. It should return a new function that always returns "Hello World".


function createHelloWorld() {
    function helloWorld() {
      return "Hello World";
    }
    return helloWorld;
  }
  
  var hello = createHelloWorld();
  
  
  console.log(hello()); // Output: Hello World