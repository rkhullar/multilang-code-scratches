package deletion_distance;

import java.util.stream.IntStream;

public class main {

  /*
   * minimal number of characters to delete for two string to match
   * d(a,b) = 0 if a matches b
   * d(a,b) = |a| + |b| if a and b have no common characters
   */
  public static int deletion_distance(String a, String b) {
    return a.length() + b.length() - 2*max_common_length(a, b);
  }

  public static int max_common_length(String a, String b) {
    int max_streak = 0;
    // traverse string a
    for (int i=0; i<a.length(); i++) {
      // find all matches in string b for current character
      for (int j: find_char(b, a.charAt(i))) {
        // determine streak
        int streak = 0;
        while ((streak < a.length()-i) && (streak < b.length()-j) && (a.charAt(i+streak) == b.charAt(j+streak)))
          streak++;
        // update result
        if (streak > max_streak)
          max_streak = streak;
      }
    }
    return max_streak;
  }

  public static int[] find_char(String target, char key) {
     return IntStream.range(0, target.length()).filter(i -> key == target.charAt(i)).toArray();
  }

  public static void main(String[] args) {
//    String a = "hello world";
//    String b = "mellow swirl";
    String a = "abc";
    String b = "bcd";
    System.out.println(deletion_distance(a, b));
  }
}
