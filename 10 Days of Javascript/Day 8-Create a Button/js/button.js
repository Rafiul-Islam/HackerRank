let count = 0;
btn = document.getElementById("btn");
btn.innerHTML = count;
btn.onclick = function () {
  count++;
  btn.innerHTML = count;
};
