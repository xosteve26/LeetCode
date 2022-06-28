class Solution {
    public int pivotIndex(int[] ip) {
        int total=0;
        for(int j=0; j<ip.length;j++){
            total+=ip[j];
        }
        
        int index=equi(ip,total);
        return index;
    }
    private static int equi(int[] ip,int total) {
        int rSum=total;
        int lSum=0;
        for(int j=0; j<ip.length;j++){
            rSum-=ip[j];
            System.out.println(lSum+" "+rSum);
            if(rSum == lSum){
                return j;
            }
            lSum+=ip[j];
        }
        return -1;
    }
}
