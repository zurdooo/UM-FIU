// package lab03;

import java.io.File;
import java.io.FileNotFoundException;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.GregorianCalendar;
import java.util.Scanner;

/**
 * Class representation of a library (a collection of library books).
 * 
 */
public class Library {

  private ArrayList<LibraryBook> library;

  public Library() {
    library = new ArrayList<LibraryBook>();
  }

  /**
   * Add the specified book to the library, assume no duplicates.
   * 
   * @param isbn   --
   *               ISBN of the book to be added
   * @param author --
   *               author of the book to be added
   * @param title  --
   *               title of the book to be added
   */
  public void add(long isbn, String author, String title) {
    library.add(new LibraryBook(isbn, author, title));
  }

  /**
   * Add the list of library books to the library, assume no duplicates.
   * 
   * @param list --
   *             list of library books to be added
   */
  public void addAll(ArrayList<LibraryBook> list) {
    library.addAll(list);
  }

  /**
   * Add books specified by the input file. One book per line with ISBN, author,
   * and title separated by tabs.
   * 
   * If file does not exist or format is violated, do nothing.
   * 
   * @param filename
   */
  public void addAll(String filename) {
    ArrayList<LibraryBook> toBeAdded = new ArrayList<LibraryBook>();

    try {
      Scanner fileIn = new Scanner(new File(filename));
      int lineNum = 1;

      while (fileIn.hasNextLine()) {
        String line = fileIn.nextLine();

        Scanner lineIn = new Scanner(line);
        lineIn.useDelimiter("\\t");

        if (!lineIn.hasNextLong())
          throw new ParseException("ISBN", lineNum);
        long isbn = lineIn.nextLong();

        if (!lineIn.hasNext())
          throw new ParseException("Author", lineNum);
        String author = lineIn.next();

        if (!lineIn.hasNext())
          throw new ParseException("Title", lineNum);
        String title = lineIn.next();

        toBeAdded.add(new LibraryBook(isbn, author, title));

        lineNum++;
      }
    } catch (FileNotFoundException e) {
      System.err.println(e.getMessage() + " Nothing added to the library.");
      return;
    } catch (ParseException e) {
      System.err.println(e.getLocalizedMessage()
          + " formatted incorrectly at line " + e.getErrorOffset()
          + ". Nothing added to the library.");
      return;
    }

    library.addAll(toBeAdded);
  }

  /**
   * Returns the holder of the library book with the specified ISBN.
   * If no book with the specified ISBN is in the library, returns null.
   * 
   * @param isbn --
   *             ISBN of the book to be looked up
   */
  public String lookup(long isbn) {
    // Lab Part 3
    // iterate through the library
    for (LibraryBook book : library) {
      // if the book is found return the holder
      if (book.getIsbn() == isbn) {
        return book.getHolder();
      }
    }
    // if the book is not found return null
    return null;
  }

  /**
   * Sets the holder and due date of the library book with the specified ISBN.
   * If no book with the specified ISBN is in the library, returns false.
   * If the book with the specified ISBN is already checked out, returns false.
   * Otherwise, returns true.
   * 
   * @param isbn   --
   *               ISBN of the library book to be checked out
   * @param holder --
   *               new holder of the library book
   * @param month  --
   *               month of the new due date of the library book
   * @param day    --
   *               day of the new due date of the library book
   * @param year   --
   *               year of the new due date of the library book
   */
  public boolean checkout(long isbn, String holder, int month, int day, int year) {
    // Lab Part 3
    // iterate through the library
    for (LibraryBook book : library) {
      // look for the book
      if (book.getIsbn() == isbn) {
        // check if book is checked out
        if (book.getHolder() == null) {
          // set the holder and due date
          book.checkout(holder, new GregorianCalendar(year, month, day));
          // checkout successful
          return true;
        } else {
          return false;
        }

      }
    }

    // no book is found
    return false;
  }

  // *********************************************************************
  // * you will implement the rest of the methods for your assignment *
  // * don't touch them before finishing the lab portion *
  // *********************************************************************

  /**
   * Returns the list of library books checked out to the specified holder.
   * 
   * If the specified holder has no books checked out, returns an empty list.
   * 
   * @param holder --
   *               holder whose checked out books are returned
   */
  public ArrayList<LibraryBook> lookup(String holder) {
    // Assignment Part 1

    // Create arraylist to return books that the holder checked out
    ArrayList<LibraryBook> checkedOutBooks = new ArrayList<LibraryBook>();
    /// loop through the library
    for (LibraryBook book : library) {
      // if the book is checked out by the holder
      if (book.getHolder() != null && book.getHolder().equals(holder)) {
        // add the book to the list
        checkedOutBooks.add(book);
      }
    }
    // return the list
    return checkedOutBooks;
  }

  /**
   * Unsets the holder and due date of the library book.
   * If no book with the specified ISBN is in the library, returns false.
   * If the book with the specified ISBN is already checked in, returns false.
   * Otherwise, returns true.
   * 
   * @param isbn --
   *             ISBN of the library book to be checked in
   */
  public boolean checkin(long isbn) {
    // Assignment Part 2.1
    // iterate through the library
    for (LibraryBook book : library) {
      // look for the book to cheeckin
      if (book.getIsbn() == isbn) {
        // check if book is checked out
        if (book.getHolder() != null) {
          // use the libray book method to checkin and set holder and duedate to null
          book.checkin();
          // succesful checkin so return true
          return true;
        }
        // if the book holder is not null then the book is already checked in
        else {
          return false;
        }

      }
    }
    // if we reach here then the book is not in the library
    return false;
  }
  public boolean checkin(String holder){
    // Assignment Part 2.1
    Boolean any_book_checked = false;
    // iterate through the library
    for (LibraryBook book : library) {
      // look for book checked in by holder
      if (book.getHolder() != null && book.getHolder().equals(holder)){
        // checkin book to unset holder and dude date
        book.checkin();
        any_book_checked = true;
      }
    }
    // return true if any book was checked in
    return any_book_checked;
  }
}