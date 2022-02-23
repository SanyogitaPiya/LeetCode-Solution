class Solution {
    public boolean isPalindrome(int x) {
        /*Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.*/
        int num=x;
        int rem=0;
        int rev=0;
        if(x<0)
            return false;
        while(num!=0)
        {
            rem=num%10;
            rev=(rev*10)+rem;
            num=num/10;
            
        }
        if(x==rev)
        {
            return true;
        }
        return false;
    }
}
