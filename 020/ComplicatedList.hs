complicatedList n = length ([(x, y) |
   x <- [(- n) .. n],
   abs x >= 3,
   y <- [(- n) .. n],
   abs y >= 3,
   x - y <= (x * y) / 2 && (x * y) / 2 <= x + y
   ])