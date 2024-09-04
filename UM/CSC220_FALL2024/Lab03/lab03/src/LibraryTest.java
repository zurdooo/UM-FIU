// package lab03;

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
  }

}
