function sides(literals, ...expressions) {
  const [A, P] = expressions;
  const rootResult = Math.sqrt(P * P - 16 * A);
  const s1 = (P + rootResult) / 4;
  const s2 = (P - rootResult) / 4;
  return [s2, s1];
}
