/* 
* Author: Vincent Truong
* Embedded C
* Here are some best practices for embedded C Programming
*/

#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

/*
* Standard libraries: stdint for unsigned and signed n-bit integers,
* stdbool for bool values
*/

/* Read from sensor for example */
typedef struct
{
    uint8_t slaveAddr;
    bool bIsActive;
    uint16_t msTimeout;
}Ic2Handle_t;


void printSpeed(int verticalSpeed)
{
    printf("Vertical Speed = %d\n", verticalSpeed);
}

/////////////////////////////
//Gloabal Variable
/////////////////////////////
static uint16_t gtotalGreenApples      = 15;
bool gIsLightOn                        = false;
volatile static uint32_t gCounterTicks = 0;
static char gWifiHome[64]              = "VincentSweetHome";
static char gWifiOffice[64]            = "VincentOffice";
static char *gActiveWifi = gWifiHome;

void printWifiName(const char *const pWifi)
{
    /*
    * Explanation of const char *const pWifi
    * 1. const char means don't change the name of the wifi
    * pWifi[0] = 1 without the const char * would result in 1incentSweetHome
    * 2. *const pWifi means that you don't want to shift the pointer of the array
    * *pWifi without the const would result in incentSweetHome because there's no const
    * 
    * */
   printf("WiFi name here: %s\n", pWifi);
}


int main(void)
{
    /*
    * Rules for Embedded C
    * 1. Follow camelCase for variables
    * 2. Always use clear and descriptive names
    * 3. Always create new variables in a new line
    * 4. Should align variable values with each other
    * 5. Varaible names should be prefixed:
    *   pointer:        prefix p
    *   double pointer: prefix pp
    *   boolean:        prefix b
    *   handles:        prefix h
    *   global:         prefix g
    * 6. What if there are variables with multiple types?
    *   Level of Priority:
    *       a. Global - g
    *       b. Pointer - p
    *       c. Normal - b, h
    * 7. Variable Keywords:
    *   Const, Static, and Volatile
    *   Const - short for consistent.
    *   Static - limits the usability of using the variable out of the program's scope or method.
    *   Volatile - prevents from making assumptions or optimization to the variable, unpredictable.
    */

   uint16_t totalApples = 16;
   float verticalSpeed = 16.32f;

   const char *pHouseName = "Vincent's House";
   const float mathPi = 3.14f;

    Ic2Handle_t *pTempSensor;
    pTempSensor->bIsActive = true;
    pTempSensor->slaveAddr = 0x1F;
    pTempSensor->msTimeout = 0x2342;

    int verticalSpeed = 12;
    printSpeed(verticalSpeed);

    uint32_t startTicks = gCounterTicks;
    printWifiName(gActiveWifi);
}