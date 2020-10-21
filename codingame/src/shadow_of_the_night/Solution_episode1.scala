package shadow_of_the_night

import math._
import scala.util._
import scala.io.StdIn._

object Player extends App {
  // W: width of the building.
  // H: height of the building.
  val Array(w, h) = (readLine split " ").map (_.toInt)
  Console.err.println("Size: (%d, %d)".format(w, h))
  val N = readLine.toInt // maximum number of turns before game over.
  val Array(x0, y0) = (readLine split " ").map (_.toInt)

  def center(lowerX: Int, lowerY: Int, upperX: Int, upperY: Int): (Int, Int) = {
    ((upperX + lowerX) / 2, (upperY + lowerY) / 2)
  }

  var (lowerX, lowerY, upperX, upperY) = (0, 0, w, h)
  Console.err.println("Initial bounds are (%d, %d), (%d, %d)".format(lowerX, lowerY, upperX, upperY))
  var x = x0
  var y = y0
  while(true) {
    val bombDir = readLine // the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    Console.err.println("Direction: %s".format(bombDir))
    bombDir.head match {
      case 'U' => upperY = y
      case 'D' => lowerY = y
      case _ =>
    }
    bombDir.last match {
      case 'R' => lowerX = x
      case 'L' => upperX = x
      case _ =>
    }
    Console.err.println("Bounds are now (%d, %d), (%d, %d)".format(lowerX, lowerY, upperX, upperY))

    val coord = center(lowerX, lowerY, upperX, upperY)
    x = coord._1
    y = coord._2
    println("%d %d".format(x, y))
  }
}