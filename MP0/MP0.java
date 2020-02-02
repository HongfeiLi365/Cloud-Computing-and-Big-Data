
import java.io.*;
import java.lang.reflect.Array;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.*;


class ValueThenKeyComparator<K extends Comparable<? super K>,
                                        V extends Comparable<? super V>>
        implements Comparator<Map.Entry<K, V>> {
    
        public int compare(Map.Entry<K, V> a, Map.Entry<K, V> b) {
            int cmp1 = a.getValue().compareTo(b.getValue());
            if (cmp1 != 0) {
                return cmp1;
            } else {
                return b.getKey().compareTo(a.getKey()); // reverse comparison
            }
        }
    
    }
    

public class MP0 {
    Random generator;
    String userName;
    String delimiters = "\\s+|\\t|\\,|\\;|\\.|\\?|\\!|\\-|\\:|\\@|\\[|\\]|\\(|\\)|\\{|\\}|\\_|\\*|\\/"; // " \t,;.?!-:@[](){}_*/"
    String[] stopWordsArray = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"};

    public MP0(String userName) {
        this.userName = userName;
    }




    public Integer[] getIndexes() throws NoSuchAlgorithmException {
        Integer n = 10000;
        Integer number_of_lines = 50000;
        Integer[] ret = new Integer[n];
        long longSeed = Long.parseLong(this.userName);
        this.generator = new Random(longSeed);
        for (int i = 0; i < n; i++) {
            ret[i] = generator.nextInt(number_of_lines);
        }
        return ret;
    }

    public String[] process() throws Exception{
    	String[] topItems = new String[20];
        Integer[] indexes = getIndexes();

    	//TO DO
    	String cur_line;
    	String[] cur_line_array;
    	Integer n = 50000;
    	Map<String, Integer> frequencies = new HashMap<String, Integer>();
        Scanner scanner = new Scanner(System.in);
        String[] inputString = new String[n];
        for (int i = 0; i < n; i++) {
            inputString[i] = scanner.nextLine();
        }

        for (int i: indexes){
            cur_line = inputString[i];
            cur_line = cur_line.toLowerCase();
            cur_line_array = cur_line.split(this.delimiters, 0);
            for (String word: cur_line_array){
                word = word.trim();
                if (word.length()>0) {
                    if (!Arrays.asList(stopWordsArray).contains(word)){
                        if (frequencies.containsKey(word)){
                            frequencies.put(word, frequencies.get(word)+1);
                        }
                        else{
                            frequencies.put(word, 1);
                        }
                    }
                }
                
            }
            
        }

        List<Map.Entry<String, Integer>> list = new ArrayList<Map.Entry<String, Integer>>(frequencies.entrySet());
        Collections.sort(list, new ValueThenKeyComparator<String, Integer>());
        
        for (int i=0; i<20; i++){
            topItems[i] = list.get(list.size()-i-1).getKey();
        }
        
		return topItems;
    }

    public static void main(String args[]) throws Exception {
    	if (args.length < 1){
    		System.out.println("missing the argument");
    	}
    	else{
    		String userName = args[0];
	    	MP0 mp = new MP0(userName);
	    	String[] topItems = mp.process();

	        for (String item: topItems){
	            System.out.println(item);
	        }
	    }
	}

}
