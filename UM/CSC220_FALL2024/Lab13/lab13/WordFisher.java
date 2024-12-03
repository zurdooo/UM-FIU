package lab13;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * The WordFisher class analyzes word frequency in a text file, allowing for 
 * operations such as pruning stopwords and finding common popular words.
 */
public class WordFisher {

    /**
     * A map containing words as keys and their occurrence frequencies as values.
     */
    public HashMap<String, Integer> vocabulary;

    /**
     * A list of stopwords to exclude from word frequency analysis.
     */
    public List<String> stopwords;

    /**
     * The file path of the input text file.
     */
    private String inputTextFile;

    /**
     * The file path of the stopwords file.
     */
    private String stopwordsFile;

    /**
     * Constructs a WordFisher object and initializes its state.
     *
     * @param inputTextFile  the path to the text file for analysis
     * @param stopwordsFile  the path to the file containing stopwords
     */
    WordFisher(String inputTextFile, String stopwordsFile) {
        this.inputTextFile = inputTextFile;
        this.stopwordsFile = stopwordsFile;

        buildVocabulary();
        getStopwords();
    }

	/**
     * Reads stopwords from the specified stopwords file and stores them in the 
     * stopwords list.
     */
    public void getStopwords() {
        stopwords = new ArrayList<String>();
        String word;

        try {
            BufferedReader input = new BufferedReader(new FileReader(stopwordsFile));
            while ((word = input.readLine()) != null) {
                stopwords.add(word);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Builds the vocabulary by reading words from the input text file and 
     * counting their frequencies.
     */
    public void buildVocabulary() {
        vocabulary = new HashMap<String, Integer>();
        try {
            BufferedReader input = new BufferedReader(new FileReader(inputTextFile));
            String line;
            while ((line = input.readLine()) != null) {
                String[] words = line.toLowerCase().split("\\s+");
                for (String word : words) {
                    word = word.replaceAll("[^a-zA-Z]", ""); // Remove non-letter characters
                    if (!word.isEmpty()) {
                        vocabulary.put(word, vocabulary.getOrDefault(word, 0) + 1);
                    }
                }
            }
            input.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * Returns the total number of words in the input text file based on the 
     * vocabulary.
     *
     * @return the total word count
     */
    public int getWordCount() {
        return vocabulary.values().stream().mapToInt(Integer::intValue).sum();
    }

    /**
     * Returns the number of unique words in the vocabulary.
     *
     * @return the number of unique words
     */
    public int getNumUniqueWords() {
        return vocabulary.size();
    }

    /**
     * Returns the frequency of a specific word in the vocabulary.
     *
     * @param word  the word whose frequency is to be returned
     * @return the frequency of the word, or -1 if the word is not in the vocabulary
     */
    public int getFrequency(String word) {
        if (vocabulary.containsKey(word)) {
            return vocabulary.get(word);
        }
        return -1;
    }

    /**
     * Removes all stopwords from the vocabulary.
     */
    public void pruneVocabulary() {
        stopwords.forEach(word -> vocabulary.remove(word));
    }

    /**
     * Retrieves the top n words from the vocabulary based on their frequency.
     *
     * @param n  the number of top words to retrieve
     * @return a list of the top n words
     */
    public ArrayList<String> getTopWords(int n) {
        ArrayList<String> topWords = new ArrayList<String>();
        vocabulary.entrySet().stream()
            .sorted((e1, e2) -> e2.getValue().compareTo(e1.getValue()))
            .limit(n)
            .forEach(entry -> topWords.add(entry.getKey()));
        return topWords;
    }

    /**
     * Finds the common popular words between this WordFisher instance and another.
     *
     * @param n     the number of top words to consider
     * @param other another WordFisher instance to compare with
     * @return a list of common popular words
     */
    public ArrayList<String> commonPopularWords(int n, WordFisher other) {
        ArrayList<String> commonPopWords = new ArrayList<String>();
        ArrayList<String> thisTop = this.getTopWords(n);
        ArrayList<String> otherTop = other.getTopWords(n);
        
        for (String word : thisTop) {
            if (otherTop.contains(word)) {
                commonPopWords.add(word);
            }
        }
        return commonPopWords;
    }

}
