fun main(args: Array<String>) {
    val a = readLine()?.toInt()
    if((a!! % 2) == 0) {
        print(a)
        println(" is even")
    } else {
        print(a)
        println(" is odd")
    }
}