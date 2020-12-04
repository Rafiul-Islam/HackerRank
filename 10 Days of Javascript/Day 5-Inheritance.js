Rectangle.prototype.area = function () {
  return this.w * this.h;
};

class Square extends Rectangle {
  constructor(p) {
    super();
    this.p = p;
    super.area = () => this.p * this.p;
  }
}
