# Math formulas
## 1. General description of the solution
Programs that calculate area and perimeter for:
- Circle
- Square
- Rectangle
- Triangle
## 2. Description of each function with call examples
### Area
- Returns area of the circle with radius $R$, calculated using the formula: $S = \pi R^2$
```
area(3)
28.274333882308138
```
- Returns area of the square with side $a$, calculated using the formula: $S = a^2$
```
area(3)
9
```
- Returns area of the rectangle with sides $a$ and $b$, calculated using the formula: $S = ab$
```
area(3, 4)
12
```
- Returns area of the triangle with side a and height h, dropped to the side $a$, calculated using the formula: $S = \frac{ah}{2}$
```
area(3, 4)
6
```
### Perimeter
- Returns perimeter of the circle with radius $R$, calculated using the formula: $S = 2\pi R$
```
perimeter(3)
18.84955592153876
```
- Returns perimeter of the square with side $a$, calculated using the formula: $S = 4a$
```
perimeter(3)
12
```
- Returns perimeter of the rectangle with sides $a$ and $b$, calculated using the formula: $S = 2(a+b)$
```
perimeter(3, 4)
14
```
- Returns perimeter of the triangle with sides a, b, c, calculated using the formula: $S = a+b+c$
```
perimeter(2, 3, 4)
9
```
## 3. Commit history
