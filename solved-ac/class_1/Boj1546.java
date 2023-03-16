package class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj1546 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        int numberOfScore= Integer.parseInt(bufferedReader.readLine());
        String[] scoreStringArray = split(bufferedReader.readLine());
        double[] scoreDoubleArray = toDoubles(scoreStringArray,numberOfScore);
        System.out.println(getScore(modifyScore(scoreDoubleArray, getMax(scoreDoubleArray))));
    }

    private static double getMax(double[] scores) {
        double max=0;
        for(double score:scores){
            if(score>max){
                max=score;
            }
        }
        return max;
    }

    private static double[] toDoubles(String[] scoreStringArray, int numberOfScore) {
        double[] scoreDoubleArray= new double[numberOfScore];
        for (int i = 0; i< numberOfScore; i++){
           scoreDoubleArray[i]=Double.parseDouble(scoreStringArray[i]);
        }
        return scoreDoubleArray;
    }

    private static String[] split(String text) throws IOException {
        return text.split(" ");
    }

    private static double getScore(double[] scoreArray) {
        double sum=0;
        for(double d: scoreArray){
            sum+=d;
        }
        return sum/scoreArray.length;
    }

    private static double[] modifyScore(double[] scoreArray, double max) {
        for(int i = 0; i< scoreArray.length; i++){
                scoreArray[i]=scoreArray[i]/max*100;
        }
        return scoreArray;
    }

}
