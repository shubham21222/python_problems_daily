class Solution {
    public int minSteps(String s, String t) {
        int x[]= new int[26];
        int y[]= new int[26];
        int count =0;
        for(int i=0;i<s.length();i++)
        {
            x[s.charAt(i)-'a']++;
        }
        for(int i=0;i<t.length();i++)
        {
            y[t.charAt(i)-'a']++;
        }
        for(int i=0;i<26;i++)
        {
            if(x[i]!=y[i] && x[i]>y[i])
            count+=x[i]-y[i];

           // System.out.println("x==>"+x[i]+" y==>"+y[i]);
        }
        return count;
    }
}