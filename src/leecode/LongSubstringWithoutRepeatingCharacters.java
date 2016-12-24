package leecode;

import java.awt.print.Printable;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class LongSubstringWithoutRepeatingCharacters {
   /*
    * Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Subscribe to see which companies asked this question
    */
	
	public static  int lengthOfLongestSubstring(String s){
		if (s.length()==0) {
			return 0;
		}
		HashMap<Character, Integer> map = new HashMap<Character, Integer>();
		int max = 0;
		int j=0;
		for (int i = 0;i < s.length(); ++i) {
			if (map.containsKey(s.charAt(i))){
				j = Math.max(j, map.get(s.charAt(i))+1);
			}
			map.put(s.charAt(i), i);
			max = Math.max(max, i-j+1);
		}
		
		return max;
	}
	
	public static int lengthOfLongestSubstringTwo(String s){
		int n = s.length();
		Set<Character> set = new HashSet<>();
		int ans = 0, i=0, j=0;
		while(j<n){
			if (!set.contains(s.charAt(j))) {
				set.add(s.charAt(j));
				j++;
				ans = Math.max(ans, j-i);
			}else{
				set.remove(s.charAt(i));
				i++;
			}
			
		}
		return ans;
	}
	
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int s=lengthOfLongestSubstringTwo("abcabcbb");
		System.out.println(s);		

	}

}
