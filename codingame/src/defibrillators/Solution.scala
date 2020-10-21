package defibrillators
import math._
import scala.util._
import scala.io.StdIn._

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
object Solution extends App {
  def toCoord = (x: String) => x.replace(',', '.').toFloat

  val EARTH_RADIUS: Int = 6371
  val LON: Float = toCoord(readLine)
  val LAT: Float = toCoord(readLine)
  val N = readLine.toInt

  var nearestDistance: Double = Double.PositiveInfinity
  var defDistance: Double = Double.PositiveInfinity
  var nearestName: Option[String] = None
  for(i <- 0 until N) {
    val DEFIB = readLine
    val Array(_, name, _, _, lonDef, latDef) = DEFIB.split(";")

    defDistance = computeDistance(LON, LAT, toCoord(lonDef), toCoord(latDef))
    if (defDistance < nearestDistance) {
      nearestDistance = defDistance
      nearestName = Some(name)
    }
  }

  println(nearestName.get)

  // Tools
  def computeDistance(lonA: Float, latA: Float, lonB: Float, latB: Float): Double = {
    val x = (lonB - lonA) * cos((latA + latB) / 2)
    val y = (latB - latA)
    sqrt(pow(x, 2) + pow(y, 2)) * 6371
  }
}