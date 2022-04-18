recommendClothing degreesCelsius
    | degreesFahrenheit <= 50 = "You should wear a jacket"
    | degreesFahrenheit < 65  = "You should wear a sweater"
    | degreesFahrenheit < 80 = "You should wear a longsleeve shirt"
    | degreesFahrenheit>= 80 = "You should wear a shortsleeve shirt"

    where degreesFahrenheit = 1.8 * degreesCelsius + 32