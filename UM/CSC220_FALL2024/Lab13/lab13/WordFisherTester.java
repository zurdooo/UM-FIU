package lab13;

public class WordFisherTester {
	
	public static void main(String[] args) {
		
		WordFisher alice = new WordFisher("texts/carroll-alice.txt", "stopwords.txt");
		
		WordFisher moby = new WordFisher("texts/moby-dick.txt", "stopwords.txt");

		// Test getWordCount()
		System.out.println("\n***** getWordCount() Tests *****");
		System.out.println("Moby Dick total words: " + moby.getWordCount());
		System.out.println("Alice total words: " + alice.getWordCount());
		
		// Test getNumUniqueWords()
		System.out.println("\n***** getNumUniqueWords() Tests *****");
		System.out.println("Moby Dick unique words: " + moby.getNumUniqueWords());
		System.out.println("Alice unique words: " + alice.getNumUniqueWords());
		
		// Test getFrequency()
		System.out.println("\n***** getFrequency() Tests *****");
		System.out.println("Frequency of 'whale' in Moby Dick: " + moby.getFrequency("whale"));
		System.out.println("Frequency of 'handkerchief' in Moby Dick: " + moby.getFrequency("handkerchief"));
		System.out.println("Frequency of 'handkerchief' in Alice: " + alice.getFrequency("handkerchief"));
		
		// Test pruneVocabulary()
		System.out.println("\n***** pruneVocabulary() Tests *****");
		moby.pruneVocabulary();
		alice.pruneVocabulary();
		System.out.println("Moby Dick words after pruning: " + moby.getWordCount());
		System.out.println("Alice words after pruning: " + alice.getWordCount());
		
		// Test getTopWords()
		System.out.println("\n***** getTopWords() Tests *****");
		System.out.println("Top 10 words in Moby Dick: " + moby.getTopWords(10));
		
		// Test commonPopularWords()
		System.out.println("\n***** commonPopularWords() Tests *****");
		System.out.println("Common popular words (n=20): " + moby.commonPopularWords(20, alice));
	}
}
