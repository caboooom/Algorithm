class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = new int[4];
        
        int lux = (int)1e9;
        int luy = (int)1e9;
        int rdx = 0;
        int rdy = 0;
        
        for(int i=0; i<wallpaper.length; i++){
            if(wallpaper[i].indexOf('#') != -1){
                if (i < lux) lux = i;
                if (wallpaper[i].indexOf('#') < luy) luy = wallpaper[i].indexOf('#');
                if (i+1 > rdx) rdx = i+1;
                if (wallpaper[i].lastIndexOf('#')+1 > rdy) rdy = wallpaper[i].lastIndexOf('#')+1;
            }
        }
        return new int[]{lux, luy, rdx, rdy};
    }
}