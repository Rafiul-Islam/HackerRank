import java.util.Scanner;

public class Plus_Minus {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int length = scanner.nextInt();
        int array[] = new int[length];
        int positiveCount = 0;
        int negetiveCount = 0;
        int zerocount = 0;

        for (int i = 0; i < array.length; i++) {
            array[i] = scanner.nextInt();
        } // end foor loop

        for (int i = 0; i < array.length; i++) {

            if (array[i] > 0) {
                positiveCount++;
            } else if (array[i] < 0) {
                negetiveCount++;
            } else {
                zerocount++;
            }
        } // end for loop

        double positiveRatio = (double)positiveCount / (double)length;
        double negetiveRatio = (double)negetiveCount / (double)length;
        double zeroRatio = (double)zerocount / (double)length;
        
        System.out.println(String.format("%5f", positiveRatio));
        System.out.println(String.format("%5f", negetiveRatio));
        System.out.println(String.format("%5f", zeroRatio));

    }

}
