import java.util.*;

class Solution {
    public int[][] solution(int[][] data, String ext, int val_ext, String sort_by) {
        int[][] answer = {};
        Map<String, Integer> sortMap = Map.of(
            "code", 0,
            "date", 1,
            "maximum", 2,
            "remain", 3
        );
        
        int extIdx = sortMap.get(ext);
        int sortIdx = sortMap.get(sort_by);
        
        return Arrays.stream(data)
            .filter(d -> d[extIdx] < val_ext)
            .sorted(Comparator.comparing(d -> d[sortIdx]))
            .toArray(int[][]::new);
    }
}