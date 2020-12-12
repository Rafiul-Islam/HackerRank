import java.util.ArrayList;
import java.util.Scanner;

public class Grading_Students {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int length = scanner.nextInt();
        int ary[] = new int[length];
        ArrayList<Integer> list = new ArrayList<>();

        for (int i = 0; i < length; i++) {
            ary[i] = scanner.nextInt();
        }

        for (int i = 0; i < length; i++) {

            if (ary[i] < 38) {
                list.add(ary[i]);
            } else {
                int result = ary[i] / 5 + 1;
                int tempValue = result * 5;

                if ((tempValue - ary[i]) < 3) {
                    list.add(tempValue);
                } else {
                    list.add(ary[i]);
                }
            }

        }
        for (int i = 0; i < ary.length; i++) {
            System.out.println(list.get(i));
        }

    }
}
