# Variables
Variables in Lascal are dynamically typed. They can be inizialized outside of the start loop. Any whitespace characters should be labeled with `\s+`. For example:

    x =5;
    x = "hi\s+john";
    start
    println x;
    end.