function getDayName(dateString) {
  let dayName;
  let d = new Date(dateString);
  let days = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
  ];

  dayName = days[d.getDay()];

  return dayName;
}
