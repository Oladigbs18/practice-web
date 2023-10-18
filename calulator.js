//love Calculator
let userChoice1 = prompt("What is your name?");
let userChoice2 = prompt("What is your crush name?");
var length = function(str) {
  return str.length;
};
let loveScore = Math.random((length(userChoice1 + userChoice2))) * 100;
loveScore = Math.floor(loveScore) + 1;
if (loveScore >= 90 && loveScore <= 100) {
  alert(
    `Your love score is ${loveScore}%. Coding Champions.`
  );
} else if (loveScore >= 80 && loveScore <= 89) {
    alert(
      `Your love score is ${loveScore}%. Coding Soulmates.`
    );
} else if (loveScore >= 70 && loveScore <= 79) {
    alert(
      `Your love score is ${loveScore}%. Coding Buddies.`
    );
} else if (loveScore >= 60 && loveScore <= 69) {
    alert(
      `Your love score is ${loveScore}%. Coding Acquaintances.`
    );
} else {
    alert(
      `Your love score is ${loveScore}%. Better Keep Coding Solo.`
    );
}
