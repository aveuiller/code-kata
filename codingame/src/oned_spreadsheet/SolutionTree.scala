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
object SolutionTree extends App {
  val N = readLine.toInt

  def computeValue(leaf: Int, operations: Array[(Operation.Value, String, String)], results: Array[Int]) = {
    def resolveArg(x: String) = if (x startsWith "$") results(x.substring(1).toInt) else (if (x == "_") 0 else x.toInt)
    val (operation, arg1, arg2) = operations(leaf)
    results(leaf) = Operation.bound(operation)(resolveArg(arg1), resolveArg(arg2))
    Console.err.println("Operation is: %s(%s, %s): = %d".format(operation, arg1, arg2, results(leaf)))
  }


  val operations = Array.ofDim[(Operation.Value, String, String)](N)
  var blocking = collection.mutable.Map[Int, Set[Int]]()
  for(i <- 0 until N) {
    val Array(operation, arg1, arg2) = readLine split " "
    operations(i) = (Operation.withName(operation), arg1, arg2)
    // Force presence of elements in the tree, even if not blocking
    blocking.put(i, blocking.getOrElse(i, Set[Int]()))

    // Add args in elements they are blocking
    for (arg: String <- Array(arg1, arg2)) {
      if (arg startsWith "$") {
        val dependency: String = arg.substring(1)
        blocking.put(dependency.toInt, blocking.getOrElse(dependency.toInt, Set[Int]()) + i)
      }
    }

  }

  // Console.err.println("Operations\n\t %s".format(operations.mkString("\n\t")))
  Console.err.println("Operations count %d (should be %d)".format(operations.size, N))
  val results = Array.ofDim[Int](N)

  while(! blocking.isEmpty) {
    val (leaf, blocked) = blocking.maxBy(_._2.size)
    Console.err.println("Solving operation on index %d (blocking %s)".format(leaf, blocked.mkString(", ")))
    computeValue(leaf, operations, results)

    blocking.remove(leaf)
  }

  for (element <- results) {
    println(element)
  }
}