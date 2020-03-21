#include <LiquidCrystal.h> //LCD Library
#include <SoftwareSerial.h>  //Software serial port library

SoftwareSerial IoT = SoftwareSerial(0xFF,2);  
SoftwareSerial barcode = SoftwareSerial(3,0xFF); 
LiquidCrystal lcd(19, 18, 17, 16, 15, 14);  
char ch; 
int total_bill = 0;

int SA = 0;
int SO = 0;
int MO = 0;
int WB = 0;
int KS = 0;
int MA = 0;
int BO = 0;

void setup()
{
  pinMode(13, OUTPUT); 
  lcd.begin(16, 2);  
  lcd.clear();
  lcd.setCursor(0, 0); 
  lcd.print(" Smart Trolley");  
  delay(1000);
  
  digitalWrite(13, HIGH); 
  delay(500);             
  digitalWrite(13, LOW);  
  delay(500);
  digitalWrite(13, HIGH);
  delay(500);
  digitalWrite(13, LOW);
  
  IoT.begin(9600);    
  barcode.begin(9600); 
  
  IoT.print("http://ksp.comoj.com/shoppingtrolley");
  IoT.print("T=%d&SA=%d&SO=%d&MO=%d&WB=%d&KS=%d&MA=%d&BO=%d",total_bill,SA,SO,MO,WB,KS,MA,BO); //send data to webpage
}

void loop()
{
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("PLS SCAN BARCODE");  
      lcd.setCursor(0, 1);    
      lcd.print("BILL: Rs.");
      lcd.print(total_bill); 
      delay(1000);
      
      ch = barcode.read(); 
      
      digitalWrite(13, HIGH);  
      delay(500);
      digitalWrite(13, LOW);   
      
      switch(ch)
      {
        case '1': //if barcode data is 1 then 
                  SA++;   //Increment item count
                  total_bill = total_bill + 55;                    
                  lcd.clear();
                  lcd.setCursor(0, 0);
                  lcd.print("Sanitiser Rs.55");
                  lcd.setCursor(0, 1);
                  lcd.print("BILL: Rs.");
                  lcd.print(total_bill);
                  delay(2000);
                  break;

        case '2': //if barcode data is 2 then
                  SO++;  //Increment item count
                  total_bill = total_bill + 45;   
                  
                  lcd.clear();
                  lcd.setCursor(0, 0);
                  lcd.print("   Soap Rs.45");
                  lcd.setCursor(0, 1);
                  lcd.print("BILL: Rs.");
                  lcd.print(total_bill);
                  delay(2000);
                  break;
                  
        case '3': //if barcode data is 3 then
                  BO++;  
                  total_bill = total_bill + 100;
                  
                  lcd.clear();
                  lcd.setCursor(0, 0);
                  lcd.print("  Box Rs.100");
                  lcd.setCursor(0, 1);
                  lcd.print("BILL: Rs.");
                  lcd.print(total_bill);
                  delay(2000);
                  break;

        case '4':
                  MO++;
                  total_bill = total_bill + 15;
                  lcd.clear();
                  lcd.setCursor(0, 0);
                  lcd.print("Masala Oats: 15");
                  lcd.setCursor(0, 1);
                  lcd.print("BILL: Rs.");
                  lcd.print(total_bill);
                  delay(2000);
                  break;

        case '5':
                  WB++;
                  total_bill = total_bill + 50;
                  lcd.clear();
                  lcd.setCursor(0, 0);
                  lcd.print("WaterBottle: 50");
                  lcd.setCursor(0, 1);
                  lcd.print("BILL: Rs.");
                  lcd.print(total_bill);
                  delay(2000);
                  break;

         case '6':
                  KS++;
                  total_bill = total_bill + 55;
                  lcd.clear();
                  lcd.setCursor(0, 0);
                  lcd.print(" Knorr Soup: 55");
                  lcd.setCursor(0, 1);
                  lcd.print("BILL: Rs.");
                  lcd.print(total_bill);
                  delay(2000);
                  break;

          case '7':
                  MA++;
                  total_bill = total_bill + 12;
                  
                  lcd.clear();
                  lcd.setCursor(0, 0);
                  lcd.print("   Maggie: 12");
                  lcd.setCursor(0, 1);
                  lcd.print("BILL: Rs.");
                  lcd.print(total_bill);
                  delay(2000);
                  break;
      }
    
      IoT.print("http://ksp.comoj.com/shoppingtrolley"); 
      IoT.print(T=%d&SA=%d&SO=%d&MO=%d&WB=%d&KS=%d&MA=%d&BO=%d",total_bill,SA,SO,MO,WB,KS,MA,BO);
      delay(2000);
}




