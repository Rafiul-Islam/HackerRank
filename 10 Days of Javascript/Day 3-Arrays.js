function getSecondLargest(nums) {
  let sortedArray = nums.sort((a, b) => a < b);
  let result;
  for (let index = 0; index < sortedArray.length; index++) {
    if (sortedArray[index] > sortedArray[index + 1]) {
      result = sortedArray[index + 1];
      break;
    }
  }
  return result;
}
