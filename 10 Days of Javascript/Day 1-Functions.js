function factorial(params) {
  var result = 1;
  for (let index = 1; index <= params; index++) {
    result *= index;
  }
  return result;
}
