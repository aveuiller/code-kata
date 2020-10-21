package  chuck_norris

import math._
import scala.util._
import scala.io.StdIn._

final case class NotEnoughCardsException() extends Exception("Could not draw") {}

case class Card(name:String) extends Ordered[Card] {
  def compare(that: Card) =  this.toComparable(this.value()) - that.toComparable(that.value())

  protected def toComparable(value: String): Int = {
    value
      .replace("J", "11")
      .replace("Q", "12")
      .replace("K", "13")
      .replace("A", "14")
      .toInt
  }

  // Drop the color
  def value(): String = name.substring(0, name.size - 1)

  // Drop the value
  def color(): String = name.last.toString

}

case class Deck(var cards: collection.mutable.Queue[Card]) {
  @throws(classOf[NotEnoughCardsException])
  def drawOne(): Card = {
    this.draw(1)(0)
  }

  @throws(classOf[NotEnoughCardsException])
  def draw(n: Int = 1): Seq[Card] = {
    if (this.count() < n) {
      throw new NotEnoughCardsException()
    }
    for (i <- 0 until n) yield cards.dequeue()
  }

  def addAll(newCards: Seq[Card]) = {
    cards = cards :++ newCards
  }

  def add(newCard: Card) = {
    cards = cards :+ newCard
  }

  def count() = cards.size

}

object Game {
  val DISCARD_PER_BATTLE = 3
  val EX_AEQUO = "PAT"
}

case class Game(player1: Deck, player2: Deck) {
  var rounds: Int = 0

  def playRound(): Option[String] = {
    Console.err.println("Player1 cards (%d): %s".format(player1.count(), player1.cards.mkString(", ")))
    Console.err.println("Player2 cards (%d): %s".format(player2.count(), player2.cards.mkString(", ")))

    rounds += 1
    var cards1: Seq[Card] = Nil
    var cards2: Seq[Card] = Nil
    try {
      cards1 = player1.draw()
    } catch {
      case e : NotEnoughCardsException => return Some("2")
    }
    try {
      cards2 = player2.draw()
    } catch {
      case e : NotEnoughCardsException => return Some("1")
    }

    Console.err.println("Significant cards: %s vs %s".format(cards1.last, cards2.last))
    while (cards1.last.compareTo(cards2.last) == 0) {
      try {
        val (newCards1, newCards2) = playBattle()
        cards1 = cards1 :++ newCards1
        cards2 = cards2 :++ newCards2
      } catch {
        case e : NotEnoughCardsException => return Some(Game.EX_AEQUO)
      }
      Console.err.println("Significant cards: %s vs %s".format(cards1.last, cards2.last))
    }

    if (cards1.last > cards2.last) {
      player1.addAll(cards1)
      player1.addAll(cards2)
    } else {
      player2.addAll(cards1)
      player2.addAll(cards2)
    }

    (player1.count(), player2.count()) match {
      case (0, 0) => Some(Game.EX_AEQUO)
      case (_, 0) => Some("1")
      case (0, _) => Some("2")
      case _ => None
    }
  }

  def playBattle(): (Seq[Card], Seq[Card]) = {
    Console.err.println("Playing Battle!")
    (player1.draw(Game.DISCARD_PER_BATTLE + 1), player2.draw(Game.DISCARD_PER_BATTLE + 1))
  }
}

object Solution extends App {
  def initPlayer(): Deck = {
    val n = readLine.toInt
    val player = Deck(new collection.mutable.Queue(initialSize=n))
    for(i <- 0 until n) player.add(Card(readLine))
    player
  }

  def play(): String = {
    val player1 = initPlayer()
    val player2 = initPlayer()

    val game = Game(player1, player2)
    var result: Option[String] = None

    while(result.isEmpty) {
      result = game.playRound()
    }

    // PAT does not return the amount of turns
    result.get match {
      case Game.EX_AEQUO => Game.EX_AEQUO
      case _ => "%s %d".format(result.get, game.rounds)
    }
  }

  println(play())
}