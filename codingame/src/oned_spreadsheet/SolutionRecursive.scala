package oned_spreadsheet

import math._
import scala.util._
import scala.io.StdIn._

object Operation extends Enumeration {
  val MULT, ADD, SUB, VALUE = Value

  def bound(x: Operation.Value): (Int, Int) => Int = {
    x match {
      case Operation.MULT => ((a1, a2) => a1 * a2)
      case Operation.ADD => ((a1, a2) => a1 + a2)
      case Operation.SUB => ((a1, a2) => a1 - a2)
      case Operation.VALUE => ((a1, _) => a1)
    }
  }
}
/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
object SolutionRecursive extends App {
  val N = readLine.toInt

  def computeValue(index: Int, operations: Array[(Operation.Value, String, String)], results: Array[Option[Int]]): Int = {
    val (operation, arg1, arg2) = operations(index)
    val Array(resolvedArg1, resolvedArg2): Array[Int] = Array(arg1, arg2) map {arg: String =>
      if (arg.startsWith("$")) {
        val argReference = arg.substring(1).toInt
        results(argReference) match {
          case Some(value) => value
          case None => computeValue(argReference, operations, results)
        }
      } else {
        if (arg.equals("_")) 0 else arg.toInt
      }
    }

    val result = Operation.bound(operation)(resolvedArg1, resolvedArg2)
    Console.err.println("Operation is: %s(%d, %d): = %d".format(operation, resolvedArg1, resolvedArg2, result))

    results(index) = Some(result)
    result
  }

  val operations = Array.ofDim[(Operation.Value, String, String)](N)
  var blocking = collection.mutable.Map[Int, Set[Int]]()
  for(i <- 0 until N) {
    val Array(operation, arg1, arg2) = readLine split " "
    operations(i) = (Operation.withName(operation), arg1, arg2)
  }

  val results: Array[Option[Int]] = Array.fill[Option[Int]](N)(None)
  for(i <- 0 until N) {
    println(computeValue(i, operations, results))
  }
}