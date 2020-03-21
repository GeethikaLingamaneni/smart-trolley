#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

ESP8266WiFi WiFi;
char packetBuffer[255]; 

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT); 
    
    USE_SERIAL.begin(9600); 
    
    WiFi.addAP("project","12345678");     
    
    digitalWrite(LED_BUILTIN, HIGH);  
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);   
    delay(1000);
    digitalWrite(LED_BUILTIN, HIGH);
    delay(1000);
    digitalWrite(LED_BUILTIN, LOW);
}

void loop()
{
    digitalWrite(LED_BUILTIN, HIGH); 
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);  
    delay(500);
    
    
    if((WiFi.run() == WL_CONNECTED)) 
    {
        HTTPClient http; 
        packetBuffer = USE_SERIAL.readString();  
        http.begin(packetBuffer); 
        http.end();    }}





