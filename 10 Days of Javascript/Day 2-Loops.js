function vowelsAndConsonants(s) {
  let vowel = [];
  let consonant = [];
  for (let index = 0; index < s.length; index++) {
    if (
      s[index] === "a" ||
      s[index] === "e" ||
      s[index] === "i" ||
      s[index] === "o" ||
      s[index] === "u"
    ) {
      vowel.push(s[index]);
    } else {
      consonant.push(s[index]);
    }
  }

  vowel.forEach((n) => console.log(n));
  consonant.forEach((n) => console.log(n));
}
