function regexVar() {
  let re = {
    test: function (s) {
      let vowels = ["a", "e", "i", "o", "u"];
      let first_letter = s[0];
      let last_letter = s[s.length - 1];
      if (first_letter === last_letter) {
        return vowels.includes(first_letter);
      }
      return false;
    },
  };
  return re;
}
