import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String[] line = reader.readLine().split(" ");
        int w = Integer.parseInt(line[0]);
        int h = Integer.parseInt(line[1]);

        int n = Integer.parseInt(reader.readLine());
        int[][] distFromOrigin = new int[n][3]; 

        for (int i=0; i<n; i++){
            line = reader.readLine().split(" ");
            int direction = Integer.parseInt(line[0]);
            int distance = Integer.parseInt(line[1]);

            int left = 0;
            int right = 0;
            switch(direction){
                case 1:
                    left = h + distance;
                    right = w + h + (w-distance);
                    break;
                case 2:
                    left = h + w + h + (w-distance);
                    right = distance;
                    break;
                case 3:
                    left = h-distance;
                    right = w  + h + w + distance;
                    break;
                case 4:
                    left = h + w + distance;
                    right = w + (h-distance);
                    break;
            }

            distFromOrigin[i][0] = left;    // 원점으로부터 반시계방향 거리
            distFromOrigin[i][1] = right;   // 원점으로부터 시계방향거리
            distFromOrigin[i][2] = direction;   // 상점이 위치한 방향
            
        }

        // 동근이의 위치
        line = reader.readLine().split(" ");
        int direction = Integer.parseInt(line[0]);
        int distance = Integer.parseInt(line[1]);

        int left = 0; // 원점으로부터 반시계방향 거리 
        int right = 0; // 원점으로부터 시계방향 거리
        int answer = 0;
        switch(direction){
            case 1:
                left = h + distance;
                right = w + h + (w-distance);
                for (int i=0; i<n; i++){
                    int dir = distFromOrigin[i][2];
                    switch (dir){
                        case 1:
                            answer += Math.abs(left - distFromOrigin[i][0]);
                            break;
                        case 2:
                            answer += Math.min(right - distFromOrigin[i][1], left + distFromOrigin[i][1]);
                            break;
                        case 3:
                            answer += left - distFromOrigin[i][0];
                            break;
                        case 4:
                            answer += distFromOrigin[i][1] - right;
                            break;
                    }
                }
                break;
            case 2:
                left = h + w + h + (w-distance);
                right = distance;
                for (int i=0; i<n; i++){
                    int dir = distFromOrigin[i][2];
                    switch (dir){
                        case 1:
                            answer += Math.min(right + distFromOrigin[i][0], distFromOrigin[i][1] - right);
                            break;
                        case 2:
                            answer += Math.abs(right - distFromOrigin[i][1]);
                            break;
                        case 3:
                            answer += right + distFromOrigin[i][0];
                            break;
                        case 4:
                            answer += distFromOrigin[i][1] - right;
                            break;
                    }
                }
                break;
            case 3:
                left = h - distance;
                right = w + h + w + distance;
                for (int i=0; i<n; i++){
                    int dir = distFromOrigin[i][2];
                    switch (dir){
                        case 1:
                            answer += distFromOrigin[i][0] - left;
                            break;
                        case 2:
                            answer += left + distFromOrigin[i][1];
                            break;
                        case 3:
                            answer += Math.abs(left - distFromOrigin[i][0]);
                            break;
                        case 4:
                            answer += Math.min(distFromOrigin[i][0] - left, left + distFromOrigin[i][1]);
                            break;
                    }
                }
                break;
            case 4:
                left = h + w + distance;
                right = w + (h-distance);
                for (int i=0; i<n; i++){
                    int dir = distFromOrigin[i][2];
                    switch (dir){
                        case 1:
                            answer += left - distFromOrigin[i][0];
                            break;
                        case 2:
                            answer += right - distFromOrigin[i][1];
                            break;
                        case 3:
                            answer += Math.min(left - distFromOrigin[i][0],right + distFromOrigin[i][0]);
                            break;
                        case 4:
                            answer += Math.abs(right - distFromOrigin[i][1]);
                            break;
                    }
                }
                break;
        }


        System.out.println(answer);
    }
}
