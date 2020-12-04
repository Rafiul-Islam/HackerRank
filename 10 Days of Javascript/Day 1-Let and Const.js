function main() {
  var r = readLine();
  var area = Math.PI * r * r;
  console.log(area);
  var circle = 2 * Math.PI * r;
  console.log(circle);
  try {
    PI = 0;
    console.log(PI);
  } catch (error) {
    console.error("You correctly declared 'PI' as a constant.");
  }
}
