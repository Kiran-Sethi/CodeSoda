// num = ["23", "+", "32", "-", "45", "+", "1"];
num = ["123", "-", "4", "+", "00", "-", "29"];

// num = num.reverse();

numStack = [];
opStack = [];

for (i of num) {
  if (i == "+" || i == "-") {
    opStack.push(i);
  } else {
    numStack.push(i);
  }
}

console.log(numStack);
console.log(opStack);

result = 0;

epStack = [];

for (let i = 0; i < numStack.length; i++) {
  if (i + 1 < numStack.length) {
    if (i == 0) {
      if (opStack[i] == "+") {
        result = parseInt(numStack[i]) + parseInt(numStack[i + 1]);
        epStack.push(result);
      } else {
        result = parseInt(numStack[i]) - parseInt(numStack[i + 1]);
        epStack.push(result);
      }
    } else {
      if (opStack[i] == "+") {
        result = epStack.pop() + parseInt(numStack[i + 1]);
        epStack.push(result);
      } else {
        result = epStack.pop() - parseInt(numStack[i + 1]);
        epStack.push(result);
      }
    }
  }
}

console.log(result);
