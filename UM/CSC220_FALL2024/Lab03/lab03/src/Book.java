// package lab03;

/**
 * Class representation of a book. The ISBN, author, and title can never change
 * once the book is created.
 * 
 * Note that ISBNs are unique.
 *
 */
public class Book {

  private long isbn;
  private String author;
  private String title;

  public Book(long isbn, String author, String title) {
    this.isbn = isbn;
    this.author = author;
    this.title = title;
  }

  // return the author
  public String getAuthor() {
    return this.author;
  }

  // return the ISBN
  public long getIsbn() {
    return this.isbn;
  }

  // return the title
  public String getTitle() {
    return this.title;
  }

  /**
   * Two books are considered equal if they have the same ISBN, author, and
   * title.
   * 
   * @param other --
   *              the object begin compared with "this"
   * @return true if "other" is a Book and is equal to "this", false otherwise
   */
  public boolean equals(Object other) {
    // Lab Part 1
    if (!(other instanceof Book)) // make sure the Object we're comparing to is a Book
      return false;

    Book o = (Book) other; // if the above was not true, we know it's safe to treat 'other' as a Book

    // compare the ISBN, author, and title of 'this' and 'other' to make sure
    // they're equal
    if (this.isbn == o.isbn && this.author.equals(o.author) && this.title.equals(o.title)) {
      return true;
    }
    // if any of the above checks fail, the Books are not equal
    return false;
  }

  /**
   * Returns a string representation of the book.
   */
  public String toString() {
    return isbn + ", " + author + ", \"" + title + "\"";
  }
}
