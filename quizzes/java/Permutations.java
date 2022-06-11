public class Permutations {
    public static void main(String[] args) {
        printPermutations("abcd", 0);
    }

    private static void swap(String str, int i, int j) {
        StringBuilder sb = new StringBuilder(str);
        sb.setCharAt(i, str.charAt(j));
        sb.setCharAt(j, str.charAt(i));
        str = sb.toString();
    }

    public static void printPermutations(String str, int idx) {
        int len = str.length();

        if (idx == len) {
            System.out.println(str);
            return;
        }

        for (int i = idx; i < len; i++) {

            swap(str, i, idx);
            printPermutations(str, idx + 1);
            swap(str, i, idx);
        }
    }

}
