import java.io.*;
import java.util.*;

public class day7{

    //Constants
    public static String fileName = "input.txt";

    //Run Program
    public static void main(String[] args){
        
        System.out.println("Part 1 Answer: " + calculateAnswer(1));
        System.out.println("Part 2 Answer: " + calculateAnswer(2));
        
    }

    //Calculate Answer
    public static int calculateAnswer(int chosenPart){
        
        //Generate Lists
        ArrayList<ArrayList<String[]>> handTypes = populateList(chosenPart);

        //Sort Lists
        HandComparator hc = new HandComparator(chosenPart);
        for(int i = 0; i < handTypes.size(); i++){
            Collections.sort(handTypes.get(i), hc);
        }

        //Find Answer
        int total = 0;
        int counter = 1;
        for(ArrayList<String[]> handType: handTypes){
            for(String[] s: handType){
                total += Integer.valueOf(s[1]) * counter;
                counter++;
            }
        }
        return total;
        
    }

    //Populate Hand Types
    public static ArrayList<ArrayList<String[]>> populateList(int part){

        //Generate 3D List
        ArrayList<ArrayList<String[]>> handTypes = 
            new ArrayList<ArrayList<String[]>>();
        for(int i = 0; i < 7; i++){
            handTypes.add(new ArrayList<String[]>());
        }

        //Read in File
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))){
            String line;
            while ((line = br.readLine()) != null){
                String[] hand = (line.split(" "));

                //Count Characters
                HashMap<Character, Integer> chars = new HashMap<Character, Integer>();
                for(char c: hand[0].toCharArray()){
                    Character ch = c;
                    if (chars.containsKey(ch)){
                        chars.replace(ch, chars.get(ch)+1);
                    }else{
                        chars.put(ch, 1);
                    }
                }

                //Morph Jacks
                Integer jacks = -1;
                boolean containsJack = false;
                if(chars.containsKey('J') && part == 2){
                    jacks = chars.get('J');
                    chars.remove('J');
                    containsJack = true;
                }

                //Order Card Type Amounts
                ArrayList<Integer> amounts = new ArrayList<Integer>();
                for (Character c: chars.keySet()){
                    amounts.add(chars.get(c));
                }
                Collections.sort(amounts, Collections.reverseOrder());
                if(containsJack && part == 2){
                    if (amounts.size() > 0){
                        amounts.set(0, amounts.get(0) + jacks); 
                    }else {
                        amounts.add(5);
                    }
                }

                //Seperate Types
                if (amounts.get(0) == 5){
                    handTypes.get(6).add(hand); //Five of a Kind
                }else if (amounts.get(0) == 4){
                    handTypes.get(5).add(hand); //Four of a Kind
                }else if (amounts.get(0) == 3){
                    if (amounts.get(1) == 2){
                        handTypes.get(4).add(hand); //Full House
                    }else{
                        handTypes.get(3).add(hand); //Three of a Kind
                    }
                }else if (amounts.get(0) == 2){
                    if(amounts.get(1) == 2){
                        handTypes.get(2).add(hand); //Two Pair
                    }else {
                        handTypes.get(1).add(hand); //One Pair
                    }
                }else {
                    handTypes.get(0).add(hand); //High Card
                }    
            }

        //File Read Fails...
        }catch (IOException e){
            System.out.println("Failed to read file.");
            e.printStackTrace();
        }

        return handTypes;
        
    }
    
    //Hand Comparator
    static class HandComparator implements Comparator<String[]> {

        static HashMap<Character, Integer> values = new HashMap<Character, Integer>();

        public HandComparator(int part){
            values.put('2', 1);
            values.put('3', 2);
            values.put('4', 3);
            values.put('5', 4);
            values.put('6', 5);
            values.put('7', 6);
            values.put('8', 7);
            values.put('9', 8);
            values.put('T', 9);
            values.put('Q', 11);
            values.put('K', 12);
            values.put('A', 13);
            if (part == 2){
                values.put('J', 0);
            }else {
                values.put('J', 10);
            }
        }
        
        public int compare(String[] h1, String[] h2) {
            char[] a1 = h1[0].toCharArray();
            char[] a2 = h2[0].toCharArray();
            for(int i = 0; i < h1[0].length(); i++){
                Integer c1 = values.get(a1[i]);
                Integer c2 = values.get(a2[i]);
                if (c1 < c2){
                    return -1;
                }else if (c1 > c2){
                    return 1;
                }
            }
            return 0;
        }
        
    }

}