public class Foo {

    String S = "abc";

    public Foo() {
        System.out.println("constructor");
    }

    static {
        System.out.println("static");
    }
    {
        System.out.println("instance");
    }

    public static void main(String[] args) {
        new Foo();
        new Foo();
    }
}
