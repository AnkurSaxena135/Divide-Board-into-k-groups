# Divide Board into k groups

This is a java code to divide a square board into a number of equal contiguous groups. The groups are randomly allocated every time.
## Examples
+  An example [main](https://github.com/AnkurSaxena135/Divide-Board-into-k-groups/blob/05bc87ee006c212b5fec92810e1e0df7f76a6dc0/src/DivideBoard.java#L11) function
```
public static void main(String[] args) {
		Cell[][] myBoard = divideBoard(9,9);
		printBoard(myBoard);
	}
```
This should divide a 9x9 board into 9 equal and contiguous groups as demonstrated below
```
2|2|2|2|3|3|3|3|3|
2|2|2|4|4|4|4|3|3|
1|2|2|4|4|4|4|4|3|
1|1|5|5|5|5|5|5|3|
1|1|5|5|9|9|8|8|8|
1|1|5|9|9|9|9|8|8|
1|1|6|9|9|9|8|8|8|
6|6|6|6|7|7|7|7|8|
6|6|6|6|7|7|7|7|7|
```

+ Similarly, passing the following arguments
```
public static void main(String[] args) {
		Cell[][] myBoard = divideBoard(4,4);
		printBoard(myBoard);
	}
```
should divide a 4x4 board into 4 equal and contiguous groups as demonstrated below
```
2|2|2|1|
4|4|2|1|
4|4|3|1|
3|3|3|1|
```

