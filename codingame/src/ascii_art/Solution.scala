package ascii_art

import math._
import scala.util._
import scala.io.StdIn._

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
object Solution extends App {

  val MISSING_LETTER_KEY: Char = '?'

  def fetchInput(): (Int, Map[Char, Array[String]], String) = {
    val L = readLine.toInt
    val H = readLine.toInt
    val T = readLine

    val RENDER = collection.mutable.Map[Char, Array[String]]()
    for(i <- 0 until H) {
      val ROW = readLine
      var lowerBound: Option[Int] = None
      var upperBound: Option[Int] = None
      var charValue: Option[Char] = None
      var renderData: Option[Array[String]] = None
      var completeData = Array[String]()

      for (i <- Range(0, ROW.size / L)) {
        lowerBound = Some(i * L)
        upperBound = Some(((i + 1) * L))
        // We have the char suite [a-z]\?
        charValue = Some(if (i < 26) (97 + i).toChar else MISSING_LETTER_KEY)

        renderData = RENDER.get(charValue.get)
        completeData = renderData.getOrElse(Array[String]()) :+ ROW.slice(lowerBound.get, upperBound.get)
        RENDER.put(charValue.get, completeData)
      }
    }
    (H, RENDER.toMap, T)
  }

  def render(height: Int, renderBinding: Map[Char, Array[String]], text: String): Unit = {
    for (i <- 0 until height) {
      for (char <- toRender.toLowerCase()) {
        print(renderBinding.getOrElse(char, renderBinding(MISSING_LETTER_KEY))(i))
      }
      println()
    }
  }

  val (height, renderBinding, toRender) = fetchInput()
  render(height, renderBinding, toRender)
}