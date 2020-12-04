function reverseString(s) {
  let array = [];
  if (typeof s == "string") {
    array = s.split("");
    console.log(array.reverse().join(""));
  } else {
    console.log("s.split is not a function");
    console.log(s);
  }
}
