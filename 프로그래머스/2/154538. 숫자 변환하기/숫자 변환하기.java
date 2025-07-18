import java.util.*;
class Solution {
    public int solution(int x, int y, int n) {
        if (x == y) {
            return 0;
        }
        int answer = 0;
        int[] arr = new int[y+1];
        int cursor = x;
        Arrays.fill(arr, Integer.MAX_VALUE);
        arr[cursor] = 0;
        while (cursor <= y) {
            if (arr[cursor] >= y) {
                cursor++;
                continue;
            }
            if (cursor * 2 <= y) {
                arr[cursor * 2] = Math.min(arr[cursor] + 1, arr[cursor * 2]);
            }
            if (cursor * 3 <= y) {
                arr[cursor * 3] = Math.min(arr[cursor] + 1, arr[cursor * 3]);
            }
            if (cursor + n <= y) {
                arr[cursor + n] = Math.min(arr[cursor] + 1, arr[cursor + n]);
            }
            if (cursor == y) {
                return arr[cursor];
            }
            cursor += 1;
        }
        
        return -1;
    }
}