import java.util.*;
import java.math.*;

public class Tuple<E1, E2> {
	private E1 x;
	private E2 y;
	
	
	
	public Tuple() {
	}
	
	public Tuple(E1 x, E2 y) {
		this.x = x;
		this.y = y;
	}
	
	
	
	public E1 x() {
		return this.x;
	}
	
	public void x(E1 x) {
		this.x = x;
	}
	
	public E2 y() {
		return this.y;
	}
	
	public void y(E2 y) {
		this.y = y;
	}
	
	
	
	public boolean equals(Tuple<E1, E2> other) {
		return this.x.equals(other.x()) && this.y.equals(other.y());
	}
	
	public String toString() {
		return "( " + this.x + ", " + this.y + ")";
	}
}
