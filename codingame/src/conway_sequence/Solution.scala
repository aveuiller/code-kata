import math._
import scala.util._
import scala.io.StdIn._

object Solution extends App {

  def nextConway(previous: Array[Int]): Array[Int] = {
    var result: Array[Int] = Array()

    var item: Int = previous.head
    var count: Int = 0
    for (i <- previous) {
      if (i != item) {
        result = result ++ Array(count, item)
        item = i
        count = 1
      } else {
        count += 1
      }
    }

    result ++ Array(count, item)
  }

  def conway(init: Int, length: Int) {
    var result = Array(init)
    for(i <- 0 until length) {
      result = nextConway(result)
      println(result.mkString(" "))
    }
  }

  conway(readLine.toInt, readLine.toInt)
}