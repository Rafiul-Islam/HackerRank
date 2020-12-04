function getCount(objects) {
  let count = 0;

  for (let index = 0; index < objects.length; index++) {
    if (objects[index].x === objects[index].y) {
      count++;
    }
  }
  return count;
}
