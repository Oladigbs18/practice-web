// a function to count the number of vowels in a string
function countVowels(str) {
  var count = 0;
  var vowels = ['a', 'e', 'i', 'o', 'u'];
  for (var i = 0; i < str.length; i++) {
    if (vowels.indexOf(str[i]) !== -1) {
      count++;
    }
  }
  return count;
}


// a function to remove spaces in a string
function removeSpaces(str) {
  return str.split(' ').join('');
}