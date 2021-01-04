# include <nRF24L01.h>

# include <printf.h>

# include <RF24.h>

# include <RF24_config.h>


# include <SPI.h>

# include "RF24.h"

int
sw = 6; // 스위치
D6에
연결하고
변수
선언

int
read_sw = 0; // 스위치
읽은
값
변수
선언

int
love;

int
led = 3;

int
count = 0;

int
cnt = 0;

// 0
번과
1
번으로
송수신을
결정

// 수신
아두이노는
0
으로, 송신
아두이노는
1
로
설정하고
컴파일

bool
radioNumber = 0;

RF24
radio(7, 8); // 7
번핀
CE, 8
번핀
CSN으로
SPI통신
설정

// pipe
adresses를
설정하기
위한
값

// 하나의
Rx가
6
개까지의
Tx와
통신가능

// 5
byte의
문자열로
주소값
설정가능

byte
addresses[6] = "ABCDE";

void
setup()

{

    Serial.begin(9600); // 통신속도
9600
bps로
시리얼
통신
시작

pinMode(sw, INPUT_PULLUP);

pinMode(3, OUTPUT); // 스위치
내부풀업
입력모드로
설정

radio.begin(); // nRF24L01모듈
초기화

// 전원
공급
관련
문제가
발생하지
않도록
PA레벨을
LOW로
설정, RF24_PA_MAX가
기본값

// RF24_PA_MIN, RF24_PA_LOW, RF24_PA_HIGH and RF24_PA_MAX

// NRF24L01: -18
dBm, -12
dBm, -6
dBM, and 0
dBm

radio.setPALevel(RF24_PA_LOW);

// 송신기
설정

if (radioNumber)

{

    radio.openWritingPipe(addresses); // 데이터를
보낼
주소
설정

radio.stopListening(); // Listening을
멈춤

}

// 수신기
설정

else

{

    radio.openReadingPipe(1, addresses); // 데이터를
받을
주소
설정

radio.startListening(); // 읽는
pipe
주소의
data
Listening
시작

}

}



void
loop()

{

if (radioNumber) // 송신기

{

    read_sw = digitalRead(6);

if (read_sw == 1)

{

    char
message[] = "전자부품 No.1 쇼핑몰";

radio.write( & message, sizeof(message)); // 해당
텍스트를
송신

char
message2[] = "Device mart";

radio.write( & message2, sizeof(message2)); // 해당
텍스트를
송신

delay(300);

}

}

else // 수신기

{

if (radio.available())

{

    int
message = 0; // 최대
32
byte까지
받아들일수
있음

radio.read( & message, sizeof(message));

love = message; // 읽은
텍스트
출력

if (love == 10)
{

    count = count + 1;

Serial.println("수신");

cnt = count % 2;

Serial.println(cnt);

if (cnt == 0)
{

    digitalWrite(3, HIGH);

}

else {
    digitalWrite(3, LOW);
}}}}}