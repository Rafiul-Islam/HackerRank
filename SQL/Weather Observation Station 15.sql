SELECT ROUND(LONG_W, 4) FROM STATION WHERE lAT_N = (
    SELECT MAX(LAT_N) FROM STATION WHERE lAT_N < 137.2345
)