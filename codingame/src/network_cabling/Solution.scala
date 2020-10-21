package network_cabling

import math._
import scala.util._
import scala.io.StdIn._

object Solution extends App {
  def fetchInput(): (List[Long], Long, Long) = {
    val N = readLine.toInt
    var minX = Long.MaxValue
    var maxX = Long.MinValue

    val housesY = Range(0, N).foldLeft(List[Long]()) { (arr, _) =>
      val Array(x, y) = (readLine split " ").map (_.toLong)
      minX = min(x, minX)
      maxX = max(x, maxX)

      arr :+ y
    }
    (housesY, minX, maxX)
  }

  def requiredCableLength(houses: List[Long], minX: Long, maxX: Long): Long = {
    Console.err.println("Houses: %s".format(houses.mkString(", ")))

    val xRequired = maxX - minX
    val median = houses.sorted.apply(houses.size / 2)
    val yFromMedian = houses.foldLeft(0L) {(required, x) => required + abs(x - median)}
    Console.err.println("Max Y: %d".format(xRequired))
    Console.err.println("Median: %d".format(median))

    xRequired + yFromMedian
  }

  val (houses, minX, maxX) = fetchInput()
  println(requiredCableLength(houses, minX, maxX))
}