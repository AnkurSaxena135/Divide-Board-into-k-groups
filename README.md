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
This should divide a 9x9 board into 9 equal and contiguous groups as demonstrated below ![](https://github.com/AnkurSaxena135/Divide-Board-into-k-groups/blob/master/sample/9x9.gif)


+ Similarly, passing the following arguments
```
public static void main(String[] args) {
		Cell[][] myBoard = divideBoard(9,6);
		printBoard(myBoard);
	}
```
should divide a 6x6 board into 9 equal and contiguous groups as demonstrated below
![](https://github.com/AnkurSaxena135/Divide-Board-into-k-groups/blob/master/sample/6x6.gif)
