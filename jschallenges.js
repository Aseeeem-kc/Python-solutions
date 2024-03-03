// String reverse
function stringReverse(string) {
    const reversedString = string.split("").reverse().join("");
    return reversedString;
}
// console.log(stringReverse("12435"));

// Palindrome check
function palindromeCheck(string) {
    const isPalindrome = string === string.split("").reverse().join("");
    return isPalindrome;
}
// console.log(palindromeCheck("1221"));






// Count vowels
function countVowels(string) {
    const vowels = "aeiouAEIOU";
    let count = 0;
    for (let char of string) {
        if (vowels.includes(char)) {
            count++;
        }
    }
    return count;
}
// console.log(countVowels("the quick brown fox"));

// Check odd or even
function oddEven(num) {
    const isEven = num % 2 === 0;
    return isEven;
}
// console.log(oddEven(5));

// Fibonacci series
function fibonacciSeries() {
    let fibonacciSequence = [0, 1];
    while (fibonacciSequence.length < 10) {
        const nextFibonacci = fibonacciSequence[fibonacciSequence.length - 1] + fibonacciSequence[fibonacciSequence.length - 2];
        fibonacciSequence.push(nextFibonacci);
    }
    return fibonacciSequence;
}
// console.log(fibonacciSeries());

// Check prime
function isPrime(n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 === 0 || n % 3 === 0) return false;
    const sqrtN = Math.floor(Math.sqrt(n));
    for (let i = 5; i <= sqrtN; i += 6) {
        if (n % i === 0 || n % (i + 2) === 0) {
            return false;
        }
    }
    return true;
}
// console.log(isPrime(17));

// Count words in a sentence
function countWords(sentence) {
    const words = sentence.trim().split(/\s+/).filter(word => word !== "");
    return words.length;
}
// console.log(countWords("   the quick brown fox   "));

// Reverse array
function reverseArray(arr) {
    const reversedArr = arr.slice().reverse();
    return reversedArr;
}
console.log(reverseArray([]));

// Find maximum
function findMaximum(arr) {
    const max = Math.max(...arr);
    return max;
}
console.log(findMaximum([5, 4, 8, 7]));





// Find minimum
function findMinimum(arr) {
    const min = Math.min(...arr);
    return min;
}
// console.log(findMinimum([5, 4, 8, 7]));




// Check Armstrong number
function isArmstrong(number) {
    const numString = String(number);
    const numDigits = numString.length;
    let armstrongSum = 0;
    for (let digit of numString) {
        armstrongSum += Math.pow(parseInt(digit), numDigits);
    }
    const isArmstrong = armstrongSum === number;
    return isArmstrong;
}
// console.log(isArmstrong(153));

// Remove duplicates
function removeDuplicates(arr) {
    const uniqueArr = [...new Set(arr)];
    return uniqueArr;
}
// console.log(removeDuplicates([1, 1, 2, 5, 6, 4, 6, 7, 5]));

// Check anagram
function checkAnagram(str1, str2) {
    const sortedStr1 = str1.replace(/\s/g, "").toLowerCase().split("").sort().join("");
    const sortedStr2 = str2.replace(/\s/g, "").toLowerCase().split("").sort().join("");
    const isAnagram = sortedStr1 === sortedStr2;
    return isAnagram;
}
// console.log(checkAnagram("listen", "silent"));

// Count characters
function countCharacters(string) {
    const charCount = {};
    for (let char of string) {
        if (char !== " ") { // Skip spaces
            charCount[char] = (charCount[char] || 0) + 1;
        }
    }
    return charCount;
}
console.log(countCharacters("hello world"));


// Check perfect number
function isPerfectNumber(number) {
    let divisorSum = 0;
    for (let i = 1; i < number; i++) {
        if (number % i === 0) {
            divisorSum += i;
        }
    }
    const isPerfect = divisorSum === number;
    return isPerfect;
}
// console.log(isPerfectNumber(6));

// Array sum
function arraySum(arr) {
    const sum = arr.reduce((acc, cur) => acc + cur, 0);
    return sum;
}
// console.log(arraySum([1, 2, 3, 4]));

// Find average
function findAverage(arr) {
    const avg = arr.length === 0 ? 0 : arraySum(arr) / arr.length;
    return avg;
}
// console.log(findAverage([1, 2, 3, 4, 5]));

// Factorial finder
function factorialFinder(number) {
    if (number < 0) return null;
    if (number === 0) return 1;
    let result = 1;
    for (let i = 1; i <= number; i++) {
        result *= i;
    }
    return result;
}
// console.log(factorialFinder(5));

// Fibonacci sequence up to a number
function fiboUptoANumber(n) {
    let fibonacciSequence = [];
    let a = 0, b = 1;
    for (let i = 0; i < n; i++) {
        fibonacciSequence.push(a);
        [a, b] = [b, a + b];
    }
    return fibonacciSequence;
}
// console.log(fiboUptoANumber(10));