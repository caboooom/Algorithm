class Solution {
    public int[] solution(String[] park, String[] routes) {
        int[] answer = new int[2];
        
        // 시작점 찾기
        int x=0, y=0;
        for(int i=0; i<park.length; i++){
            for(int j=0; j<park[0].length(); j++){
                if (park[i].charAt(j)=='S'){
                    x = i;
                    y = j;
                    break;
                }
            }
        }
        
        int nx=0, ny=0;
        int dx=0, dy=0;
        for (String route : routes){
            String[] arr = route.split(" ");
            int dist = Integer.parseInt(arr[1]);
            switch(arr[0]){
                case "N":
                    dx = -1;
                    dy = 0;
                    break;
                case "S":
                    dx = 1;
                    dy = 0;
                    break;
                case "W":
                    dx = 0;
                    dy = -1;
                    break;
                case "E":
                    dx = 0;
                    dy = 1;
            }
            
            // 이동 가능 여부 판단
            boolean movable = true;
            int curX = x, curY = y;
            for(int i=0; i<dist; i++){
                
                nx = curX + dx;
                ny = curY + dy;
                if(nx < 0 || nx >= park.length || ny < 0 || ny >= park[0].length() || park[nx].charAt(ny) == 'X'){
                    movable = false;
                    break;
                }else{
                    curX = nx;
                    curY = ny;
                }
            }
            
            // 이동
            if (movable){
                x = curX;
                y = curY;
            }
            
        }
        
        answer[0] = x; answer[1] = y;
        return answer;
    }
}