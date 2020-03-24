// chap 1
// looping triangle
let str = '';
for (let i = 0; i < 7; i++) {
    for (let j = i; j < i+1; j++) {
        str += '#';
    }
    console.log(str);
}
// ------------------------------
for (let line = "#"; line.length < 8; line += "#")
  console.log(line);
//   fizzbuzz

fizzBuzz = () => {
    for (let i = 0; i <= 100; i++) {
      if (i % 15 == 0) {
        console.log("FizzBuzz");
      } else if (i % 3 == 0) {
        console.log("Buzz");
      } else if (i % 5 == 0) {
        console.log("Fizz");
      }
      else {
        console.log(i);
      }
    }
  }
  
  console.log(fizzBuzz());

  for (let n = 1; n <= 100; n++) {
    let output = "";
    if (n % 3 == 0) output += "Fizz";
    if (n % 5 == 0) output += "Buzz";
    console.log(output || n);
  }
// chessboard
let board = "";
let size = prompt("Size?");
for (let i = 0; i < size; i++) { 
  for (let j = 0; j < size; j++)
    if ((i+j) % 2 == 0) {
      board += ' ';
    } else {
      board += '#';
    }
  board += '\n';
}
console.log(board)
// chap 2


// takes two args and returns min

min = (n1,n2) => {
    if (n1 > n2) {
        return n2;
    } else {
        return n1;
    }
}
W
console.log(min(1,2))

function min(a, b) {
    if (a < b) return a;
    else return b;
  }
}
// --------------

// recursion, isEven

isEven = (int) => {
    if (int < 0) {
      int *= -1;
    }
    if (int == 0) {
      return true;
    } else if (int == 1) {
      return false;
    } else {
      return isEven(int-2);
    }
  }
  console.log(isEven(24));

  function isEven(n) {
    if (n == 0) return true;
    else if (n == 1) return false;
    else if (n < 0) return isEven(-n);
    else return isEven(n - 2);
  }


//   count chars

function countChars(str,char) {
    let count = 0;
    for (let i = 0; i < str.length; i++) {
      if (str[i] == char) {
        count++;
      }
    }
    return count;
  }
  
  console.log(countChars("a","d"));


  //sum of range

  range = (start,end,step) => {
    let arr = [];
    let count = 0;
    while (arr.length <= end - start) {
      arr.push(start+count);
      count += step;
    }
    return arr;
  }
  let arr = range(1,5,1);
  sum = (arr) => {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
      sum += arr[i];
    }
    return sum;
  }
    
  console.log(sum(range(1,5,1)))
// 
  function range(start, end, step = start < end ? 1 : -1) {
    let array = [];
  
    if (step > 0) {
      for (let i = start; i <= end; i += step) array.push(i);
    } else {
      for (let i = start; i >= end; i += step) array.push(i);
    }
    return array;
  }
  
  function sum(array) {
    let total = 0;
    for (let value of array) {
      total += value;
    }
    return total;
  }
  
  // array to list need to do
  function arrayToList(array) {
    let list = null;
    for (let i = array.length - 1; i >= 0; i--) {
      list = {value: array[i], rest: list};
    }
    return list;
  }
