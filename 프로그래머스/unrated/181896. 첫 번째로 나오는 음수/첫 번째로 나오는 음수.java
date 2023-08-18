class Solution {
    public int solution(int[] num_list) {
        int i = 0;
        while (i < num_list.length){
            if (num_list[i] < 0) return i;
            i++;
        }
        return -1;
    }
}