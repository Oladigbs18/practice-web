// The program includes five multiple-choice questions with four options each. 
//It prompts the user for their answers,
// compares them to the correct answers, and calculates the final score as a percentage.

import java.util.Scanner;

public class Assignment {
    /**
     * @param args
     */
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int score = 0;
        System.out.println("Welcome to the quiz!");
        System.out.println("Question 1: What is the capital of Canada?");
        System.out.println("A. Toronto");
        System.out.println("B. Ottawa");
        System.out.println("C. Vancouver");
        System.out.println("D. Montreal");
        System.out.print("Your answer: ");
        String answer1 = input.nextLine();
        if (answer1.equals("B")) {
            score++;
        }
        System.out.println("Question 2: What is the capital of the United States?");
        System.out.println("A. New York");
        System.out.println("B. Washington D.C.");
        System.out.println("C. Los Angeles");
        System.out.println("D. Chicago");
        System.out.print("Your answer: ");
        String answer2 = input.nextLine();
        if (answer2.equals("B")) {
            score++;
        }
        System.out.println("Question 3: What is the capital of China?");
        System.out.println("A. Beijing");
        System.out.println("B. Shanghai");
        System.out.println("C. Hong Kong");
        System.out.println("D. Macau");
        System.out.print("Your answer: ");
        String answer3 = input.nextLine();
        if (answer3.equals("A")) {
            score++;
        }
        System.out.println("Question 4: What is the capital of Japan?");
        System.out.println("A. Tokyo");
        System.out.println("B. Osaka");
        System.out.println("C. Kyoto");
        System.out.println("D. Yokohama");
        System.out.print("Your answer: ");
        String answer4 = input.nextLine();
        if (answer4.equals("A")) {
            score++;
        }
            System.out.println("Question 5: What is the capital of South Korea?");
            System.out.println("A. Seoul");
            System.out.println("B. Busan");
            System.out.println("C. Incheon");
            System.out.println("D. Daegu");
            System.out.print("Your answer: ");
            String answer5 = input.nextLine();
            if (answer5.equals("A")) {
                score++;
            }
            System.out.println("Your score is " + score + "/5.");

            double percentage = (double) score / 5 * 100;
            System.out.println("Your percentage is: " + percentage + "%");
        }
