

import java.awt.EventQueue;
import java.util.PriorityQueue;
import java.util.concurrent.ThreadLocalRandom;

public class DivideBoard {

	private static Cell[][] board;
	private static int boardSize;
	private static PriorityQueue<Cell> queue = new PriorityQueue<Cell>(5,(cell1,cell2)-> {return Integer.compare(cell1.degree,cell2.degree);});

	public static void main(String[] args) {
		int groups=10;
		int size=10;
		Cell[][] myBoard = divideBoard(groups,size);
		
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Board boardUI = new Board(groups,size,myBoard);
					boardUI.getFrame().setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
		//printBoard(myBoard);
	}
	private static Cell[][] divideBoard(int groups,int size) {

		board = new Cell[size][size];
		boardSize = size;

		initBoard();

		int initRow= ThreadLocalRandom.current().nextInt(0, size);
		int initCol= ThreadLocalRandom.current().nextInt(0, size);
		
		queue.add(board[initRow][initCol]);

		for(int grpno = 1; grpno <= groups; grpno++){

			int count = (size*size)/groups;
			while( count != 0 ) {

				Cell nextCell=queue.poll();
				selectCell(nextCell.row,nextCell.col,grpno);
				count--;
			}
			if(grpno != groups) {
				Cell firstCell = queue.poll();
				queue.clear();
				queue.add(firstCell);
			}
		}
		return board;
	}
	private static void initBoard() {
		for(int i=0;i<boardSize;i++) {
			for(int j=0;j<boardSize;j++) {
				board[i][j]=new Cell(i,j,-1,0);
			}
		}
		assignDegree();
	}
	private static void assignDegree() {
		//assign all cells
		assignValue(board,-1,-1,4);
		//assign edges
		assignValue(board,0,-1,3);
		assignValue(board,boardSize-1,-1,3);
		assignValue(board,-1,0,3);
		assignValue(board,-1,boardSize-1,3);
		//assign corners
		assignValue(board,0,0,2);
		assignValue(board,0,boardSize-1,2);
		assignValue(board,boardSize-1,0,2);
		assignValue(board,boardSize-1,boardSize-1,2);
	}
	private static void assignValue(Cell[][] board, int row, int col, int deg) {
		if(row==-1 && col==-1) {
			for(int i=0;i<boardSize;i++) {
				for(int j=0;j<boardSize;j++) {
					board[i][j].degree=deg;
				}
			}
		}
		else if(row!=-1 && col!=-1) board[row][col].degree=deg;
		else {
			if(row==-1) {
				for(int i=0;i<boardSize;i++) {board[i][col].degree=deg;}
			}
			if(col==-1) {
				for(int j=0;j<boardSize;j++) {board[row][j].degree=deg;}
			}
		}
	}
	private static void selectCell( int row, int col, int group) {
		
		board[row][col].group=group;
		board[row][col].degree=-1;
		if(row<boardSize-1 && board[row+1][col].degree>0) {
		
			board[row+1][col].degree--;
			queue.remove(board[row+1][col]);
			queue.add(board[row+1][col]);
		}
		if(row>0 && board[row-1][col].degree>0) {
		
			board[row-1][col].degree--;
			queue.remove(board[row-1][col]);
			queue.add(board[row-1][col]);
		}
		if(col>0 && board[row][col-1].degree>0) {
		
			board[row][col-1].degree--;
			queue.remove(board[row][col-1]);
			queue.add(board[row][col-1]);
		}
		if(col<boardSize-1 && board[row][col+1].degree>0) {
		
			board[row][col+1].degree--;
			queue.remove(board[row][col+1]);
			queue.add(board[row][col+1]);
		}
	}	
	@SuppressWarnings("unused")
	private static void printBoard(Cell[][] board) {

		for(int i=0;i<boardSize;i++) {
			for(int j=0;j<boardSize;j++) {
				System.out.print(board[i][j].group+"|");
			}
			System.out.println();
		}
	}
}
