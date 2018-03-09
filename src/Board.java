
import javax.swing.JButton;
import javax.swing.JFrame;
import java.awt.GridLayout;
import java.awt.Color;
import java.awt.Dimension;

public class Board {

	private JFrame frame;
	private Color[] colors= new Color[]{Color.RED,Color.GREEN,Color.MAGENTA,Color.YELLOW,Color.BLACK,
										Color.PINK,Color.BLUE,Color.CYAN,Color.DARK_GRAY,Color.ORANGE};
	/**
	 * Create the application.
	 * @param myBoard 
	 */
	public Board(int groups,int size, Cell[][] myBoard) {
		initialize(groups,size,myBoard);
	}

	/**
	 * Initialize the contents of the frame.
	 * @param myBoard 
	 */
	private void initialize(int groups,int size, Cell[][] myBoard) {
		setFrame(new JFrame());
		getFrame().setBounds(100, 100, 780, 479);
		getFrame().setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		getFrame().getContentPane().setLayout(new GridLayout(size, size, 1, 1));
	
		for(int i=0;i<size;i++) {
			for(int j=0;j<size;j++) {
				
				JButton btn = new JButton("");
				btn.setPreferredSize(new Dimension(50, 50));
				btn.setBackground(colors[myBoard[i][j].group-1]);
				btn.setOpaque(true);
				frame.getContentPane().add(btn);
			}
		}	
		getFrame().pack();
	
	}

	public JFrame getFrame() {
		return frame;
	}

	public void setFrame(JFrame frame) {
		this.frame = frame;
	}

}
