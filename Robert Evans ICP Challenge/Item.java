/**
 *  This class serves a management system for essentials allowing the user to record the stock price and name of an item
 * @author Robert-William Evans
 * @version 1.0.0
 */

import java.util.*;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.Serializable;
import java.util.InputMismatchException;



public class Item {
    private String iName;
    private double iPrice;
    private int stock;

    public Item(String iName, double iPrice, int stock) {
        this.iName = iName;
        this.iPrice = iPrice;
        this.stock = stock;
    }

    /**
     *This is a setter method the name variable
     * @param iName This is passed through method
     *
     */
    public void setiName(String iName){
        this.iName = iName;

    }

    /**
     *This is a setter method for the price variable
     * @param iPrice
     *
     */
    public void setiPrice(float iPrice){
        this.iPrice = iPrice;
    }

    /**
     *This is a setter method for the stock variable
     * @param stock
     *
     */
    public void setStock(int stock){
        this.stock = stock;
    }

    /**
     *This is a getter method for the price variable
     * @return
     */
    public double getPrice(){
        return iPrice;

    }

    /**
     *This is a getter method for the stock  variable
     * @return
     */
    public int getStock(){
        return stock;

    }

    /**
     *This is a getter method for the name variable
     * @return
     */
    public String getName(){
        return iName;
    }


    /**
     * This prints out the details of the item
     */
    public void itemDetails(){
        System.out.println("Item: " + iName + ", Quantity: " + stock + ", Price: " + iPrice);
    }

    /**
     *This is a test method to help us manage our records.
     * @param args
     */
    public static void main(String args[]){
        try {
            Scanner numItems = new Scanner(System.in);//Takes the amount of items one wants to stock and allows the user to create an item
            System.out.println("Enter the amount of items you want to add: ");
            int nItems = numItems.nextInt();
            for (int i = 0; i < nItems; i++) {

                Scanner input = new Scanner(System.in);
                System.out.println("Enter the name of the item:   ");
                String inputN = input.nextLine();

                Scanner input2 = new Scanner(System.in);
                System.out.println("Enter the price of the item: ");
                double inputP = input2.nextDouble();

                Scanner input3 = new Scanner(System.in);
                System.out.println("Enter the stock of the item:  ");
                int inputS = input3.nextInt();

                Item item1 = new Item(inputN, inputP, inputS);
                item1.itemDetails();

                item1.writingTextToFile();// writes this information to a file
            }

        } catch (InputMismatchException e){// in case user enters wrong data type for a question
            System.out.println("Please you have entered a wrong input");
        }


        }

    /**
     * This enables the user to write to a file
     */

    private void writingTextToFile() {
        PrintWriter printWriter = null;

        try {

            printWriter = new PrintWriter(new FileOutputStream("essentials_stock.txt", true));
        } catch (FileNotFoundException exception) {
            exception.getMessage();
        }

        printWriter.print(iName + " "+ stock + " " + "GHc" + iPrice);
        printWriter.println();

        printWriter.close();

        try {

            printWriter = new PrintWriter(new FileOutputStream("backup_essentials_stock.txt", true));
        } catch (FileNotFoundException exception) {
            exception.getMessage();
        }

        printWriter.print(iName + " "+ stock + " " + "GHc" + iPrice);
        printWriter.println();

        printWriter.close();
    }
}



















