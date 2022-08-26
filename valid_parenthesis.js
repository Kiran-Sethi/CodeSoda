// Link : https://leetcode.com/problems/valid-parentheses

var isValid = function (s) {
  const typeDict = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  let stack = [];
  for (i of s) {
    if (i === "(" || i === "[" || i === "{") {
      stack.push(i);
    } else {
      if (stack.pop() === typeDict[i]) {
        continue;
      } else {
        return false;
      }
    }
  }

  if (stack.length > 0) {
    return false;
  } else {
    return true;
  }
};

// test cases

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false
