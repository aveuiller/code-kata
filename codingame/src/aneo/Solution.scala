package aneo

import math._
import scala.util._
import scala.io.StdIn._

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 *
 * Score 80% ! :(
 **/
object Solution extends App {

    def fetchInput(): (Int, Array[(Int, Int)]) = {
        val speed = readLine.toInt
        val lightCount = readLine.toInt
        var lights = Array[(Int, Int)]()
        for(i <- 0 until lightCount) {
            val Array(distance, duration) = (readLine split " ").map (_.toInt)
            lights = lights :+ (distance, duration)
        }

        (speed, lights)
    }

    def is_green(distance: Int, duration: Int, speed: Int): Boolean = {
        /* Light is at distance meters.
           Stays green for duration seconds, then red for duration seconds.
           Starts green.
           The vehicule goes at speed km/h
        */
        val speedMetersSeconds = speed / 3.6
        val secondsToLight = round(distance / speedMetersSeconds)
        val numberOfTransitions = secondsToLight / duration
        // Nymber of iteration, should be pair to be a green value
        Console.err.println("- Checking light - Duration: " + duration + "; distance: " + distance + "; speed: " + speedMetersSeconds)
        Console.err.println("-- Second to light: " + secondsToLight + "; Nb transitions: " + numberOfTransitions)

        return numberOfTransitions.toInt % 2 == 0
    }

    def compatible_speed(speed: Int, lights: Array[(Int, Int)]): Boolean = {
        for ((distance, duration) <- lights) {
            if (! is_green(distance, duration, speed)) {
                Console.err.println("- Found an incompatible light, reducing speed")
                return false
            }
        }
        return true
    }

    def solve(speed: Int, lights: Array[(Int, Int)]): Int = {
        Console.err.println("We have " + lights.size + " lights to go through")
        for (result: Int <- Range(speed, 0, -1)) {
            Console.err.println("Trying out speed: " + result)
            if (compatible_speed(result, lights)) {
                return result
            }
        }
        return 0
    }

    val (speed, lights) = fetchInput()
    println(solve(speed, lights))
}