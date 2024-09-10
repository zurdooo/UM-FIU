// package lab03;
import java.util.ArrayList;

/**
 * Testing class for Library.
 * 
 * 
 */
public class LibraryTest {

  public static void main(String[] args) {

    // lab03 - part 2 samples
    // book1
    // isbn: 9780374292799L
    // author: Thomas L. Friedman
    // title: The World is Flat

    // book2
    // isbn: 9780330351690L
    // author: Jon Krakauer
    // title: Into the Wild

    // You wrote 5 Methods and 1 Constuctor
    // I suggest testing that all of these work before moving to part 3

    // **WRITE YOUR TESTS HERE**
    Book book1 = new Book(9780374292799L, "Thomas L. Friedman", "The World is Flat");
    Book book2 = new Book(9780330351690L, "Jon Krakauer", "Into the Wild");
    Book book3 = new Book(9780330351690L, "Jon Krakauer", "Into the Wild");

    System.out.println("Expected: False");
    System.out.println("Actual: " + book1.equals(book3) + "\n");

    // lab03 - part 3 tests
    Library lib = new Library();

    if (lib.lookup(978037429279L) != null)
      System.err.println("TEST FAILED -- empty library: lookup(isbn)");

    // test a small library - with four books in it
    lib.add(9780374292799L, "Thomas L. Friedman", "The World is Flat");
    lib.add(9780330351690L, "Jon Krakauer", "Into the Wild");
    lib.add(9780446580342L, "David Baldacci", "Simple Genius");

    if (lib.lookup(9780330351690L) != null)
      System.err.println("TEST FAILED -- small library: lookup(isbn)");

    lib.checkout(978037429279L, "Jane Doe", 1, 1, 2008);

    if (lib.lookup(9780330351690L) != null)
      System.err.println("TEST FAILED -- small library: lookup(isbn)");

    System.out.println("Testing done.");
  
  // Additional tests for Library class

  // Test adding a book with the same ISBN
  lib.add(9780374292799L, "Duplicate Author", "Duplicate Title");
  if (lib.lookup(9780374292799L) == null)
    System.err.println("TEST FAILED -- adding duplicate ISBN");

  // Test checking out a book that doesn't exist
  boolean checkoutResult = lib.checkout(1234567890123L, "John Doe", 1, 1, 2023);
  if (checkoutResult)
    System.err.println("TEST FAILED -- checkout non-existent book");

  // Test checking out a book that is already checked out
  lib.checkout(9780374292799L, "Jane Doe", 1, 1, 2023);
  boolean secondCheckoutResult = lib.checkout(9780374292799L, "John Doe", 1, 1, 2023);
  if (secondCheckoutResult)
    System.err.println("TEST FAILED -- checkout already checked out book");

  // Test checking in a book that doesn't exist
  boolean checkinResult = lib.checkin(1234567890123L);
  if (checkinResult)
    System.err.println("TEST FAILED -- checkin non-existent book");

  // Test checking in a book that is already checked in
  lib.checkin(9780374292799L);
  boolean secondCheckinResult = lib.checkin(9780374292799L);
  if (secondCheckinResult)
    System.err.println("TEST FAILED -- checkin already checked in book");

  // Test lookup by holder when no books are checked out
  ArrayList<LibraryBook> booksCheckedOut = lib.lookup("Jane Doe");
  if (!booksCheckedOut.isEmpty())
    System.err.println("TEST FAILED -- lookup(holder) with no books checked out");

  // Test lookup by holder when books are checked out
  lib.checkout(9780330351690L, "Jane Doe", 1, 1, 2023);
  booksCheckedOut = lib.lookup("Jane Doe");
  if (booksCheckedOut.size() != 1 || booksCheckedOut.get(0).getIsbn() != 9780330351690L)
    System.err.println("TEST FAILED -- lookup(holder) with books checked out");

  // Test checkin by holder
  boolean checkinByHolderResult = lib.checkin("Jane Doe");
  if (!checkinByHolderResult)
    System.err.println("TEST FAILED -- checkin(holder)");

  // Test checkin by holder when no books are checked out
  checkinByHolderResult = lib.checkin("Jane Doe");
  if (checkinByHolderResult)
    System.err.println("TEST FAILED -- checkin(holder) with no books checked out");

  System.out.println("Additional testing done.");

}
}