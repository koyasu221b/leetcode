public class Solution {
    public int minimumSize(int[] nums, int s) {
        // write your code here
        int sum = 0;
        int j = 0;
        int current_min_size = Integer.MAX_VALUE;
        for(int i = 0; i < nums.length; i++){

            while(j < nums.length){
                if(sum < s){
                    sum += nums[j];
                    j++;
                }else{
                    break;
                }
            }
            
            if(sum >= s){
                //since j++ ()
                 if((j-i + 1 -1) < current_min_size){
                    current_min_size = j - i + 1 -1;
                }
            }

            
            sum -= nums[i];
        }
        
        if(current_min_size < Integer.MAX_VALUE){
            return current_min_size;
        }
        
        return -1;
    }
}
