# Functions in Lascal
Functions are procedures but with a return value. They can be declared with `func` keyword. For example:

    func hi() {
        return "hi";
    }
Functions can't be used in println statements.

    println hi();
    // prints hi()
    // Alternative
    x = hi();
    println x;