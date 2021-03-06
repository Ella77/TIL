# C 기초 문법 정리

확실하게 외우지 못하고 있던 것들만 정리한다.

## 0. 기본

- `,` 콤마 연산자
    + 둘 이상의 변수 동시 선언할 때. `int a=1, b=2;`
    + 한 줄에 여러 문장을 쓸 때. `a++, b++;`
- 연산 순서: [위키피디아](https://ko.wikipedia.org/wiki/C%EC%99%80_C%2B%2B%EC%97%90%EC%84%9C%EC%9D%98_%EC%97%B0%EC%82%B0%EC%9E%90) 문서 아래쪽에 잘 정리되어있다. 비트 연산자가 논리 연산자보다 앞서고 `&`이 `|`보다 앞선다.
- `scanf` 함수는 데이터의 경계를 공백(빈칸, 탭, 엔터)로 구분한다.
- 비트 연산: 두 숫자에서 같은 위치의 비트끼리 연산한다.
    + `&`, `|` : 두 숫자 사이에서 AND, OR 연산
    + `^` : 두 숫자 사이에서 XOR 연산. 두 개의 비트가 서로 다를 때만 1을 반환한다.
    + `~` : `~a` 형태로 쓰여서 NOT 연산을 한다. 보수 연산이라고도 하며 모든 비트를 반전시킨다. 부호 비트까지 반전된다.
    + `<<`, `>>` : 모든 비트의 위치를 왼쪽, 오른쪽으로 한 칸씩 옮긴다. `a << 2` 형태는 a를 왼쪽으로 2칸 bit shift 연산한다는 의미다. 왼쪽으로 이동하면 우측에 생기는 빈자리는 0으로 채워진다. 우측으로 이동시키면 역시 왼쪽 빈자리에 0이 채워지는데 음수일 경우엔 시스템에 따라 1을 채울지 0을 채울지가 달라진다. 지금 내 맥북은 1이 채워진다.
- NULL 포인터: 가끔 gcc에서 `NULL`을 인식하지 못할 때가 있다. undeclared variable이라고. 그래서 다른 방법으로 선언하고 값을 넣어줘야한다.
    + `float *ptr = (float *)0;`
    + `char *ptr = (char *)0;`
    + `double *ptr = (double *)0;`
    + `char *ptr = '\0';`
    + `int *ptr = NULL;`
- 포인터의 `+` 연산은 단순히 1이 더해지는게 아니라 포인터의 이동을 뜻한다. int 형이라면 4바이트가 이동하고, char 타입이라면 1바이트가 이동하는 식.

## 1. 자료형

### 1.1 숫자 관련

#### 1.1.1 정수형

- `int`
    + 4바이트 공간을 차지한다. 0과 1을 표현하는 비트로 바꾸면 총 32비트다.
    + 가장 왼쪽의 비트는 MSB(Most Significant Bit)라 해서 부호를 나타낸다. 0이면 양수, -1이면 음수다.
    + 31비트만 사용해서 수를 표현하므로 범위가 `-2^32 < int < 2^32` 이다.
    + 음수 계산은 쉽다. 양수를 2진법으로 바꾼 후 -> 보수를 만들고(1과 0을 뒤바꿈) -> 1을 더하면 원래 양수에 -를 붙인 값이 된다. 즉 두 수를 합쳤을 때 1111111 형태가 될텐데 거기서 1을 더하면 한 자리가 초과되면서 넘어간 자리수는 표현이 안되고 나머지 모두가 0이 되버린다. 두 수를 합했을 때 0이 되므로 음수라고 할 수 있는 것이다.
- long
- unsigned int

#### 1.1.2 실수형

- float
- double

### 1.2 문자

- char

### 1.3 문자열

- 문자열 상수와 문자 배열로 나뉜다. 각각 타입은 `char *str`, `char str[]`이다. 이 때 str은 첫 글자를 가리키는 포인터다. 문자열을 출력하거나 인식할 때 `'\0'` 널 문자까지 인식한다.
- 문자열 상수는 각 문자들을 변경할 수 없고, 문자 배열은 가능하다.
- 문자열을 가리키는 포인터에 1씩 더해주면 다음 문자를 가리키게 된다.
- `strlen(str)` 함수는 널문자를 제외한 순수 문자열의 길이를 리턴하고, `sizeof(str)`은 문자열 상수일 경우엔 포인터 변수의 크기를, 문자 배열일 경우엔 전체 문자 배열의 크기를 리턴한다. `str[30]`에 문자열이 `"abcde"`만 들어있더라도 30을 리턴한다.

### 1.4 배열

#### 1.4.1 선언

- 정수형 1차원 배열 선언
    + `int arr[] = {1, 2, 3};` : 이렇게 원소 수를 지정 안해도 알아서 할당된다.
    + `int arr[3] = {0, };` or `int arr[3] = {0};` : 모든 원소를 0으로 초기화
    + `int arr[10] = {1, 2};` : 크기 10의 배열을 선언하는데 첫 번째, 두 번째 원소를 1, 2로 넣고 나머지는 0으로 대입된다.
- 정수형 2차원 배열 선언
    + `int values[2][3] = {{3, 5, 7}, {4, 6, 8}};`
    + `int values[2][3] = {3, 5, 7, 4, 6, 8};`
- 문자열이 들어있는 배열의 타입은 `char **` 더블 포인터다. 

#### 1.4.2 배열 포인터

- 퀵 정렬 코드를 보면서 지금까지 틀리게 알고 있었던 것을 깨달았다.
- 아래 `func1`, `func2`는 동작 원리가 같다.
- 주소값을 넘겨주는 것이기 때문에 func의 바깥에 있는 main 함수의 arr 배열은 func 호출 이후에 값이 바뀌게 된다.
- `int arr[]` 처럼 선언하는 방식은 함수의 매개변수에서만 가능하다.
- 원래는 이게 바뀌면 안되는 줄 알았다. 무조건 더블 포인터를 써야하는 건 줄 알았다.

```c
#include <stdio.h>

void func1(int *arr1)
{
    arr1[0] = 100;
}

void func2(int arr1[])
{
    arr1[0] = 100;
}

int main(void)
{
    int arr[2] = {1, 2};
    printf("prev: %d\n", arr[0]);
    func1(arr);
    // func2(arr);
    printf("post: %d\n", arr[0]);
    return (0);
}
```

- 문자열의 경우도 마찬가지다.

```c
#include <unistd.h>

void    func(char *str);
void    func1(char str[])
void    ft_putchar(char c);
void    ft_putstr(char *str);

int     main(void)
{
    char str[] = "abcde";

    ft_putstr(str);
    ft_putchar('\n');
    func(str);
    // func1(str);
    ft_putstr(str);
    return (0);
}

void    func(char *str)
{
    str[0] = 'A';
}

void    func1(char str[])
{
    str[0] = 'A';
}

void    ft_putchar(char c)
{
    write(1, &c, 1);
}

void    ft_putstr(char *str)
{
    while (*str)
        ft_putchar(*str++);
}
```

## 2. 제어문

### 2.1 for, while 반복문

- for 반복문의 증감식에서 전위, 후위에 따라 내부 동작 원리가 다르다. 컴파일러가 알아서 최적화하는 경우도 있지만 그렇지 않은 경우 전위 증감 연산자를 활용하는 것이 성능상 이득이 있다. 무엇을 활용하든 결과는 변하지 않는다.
    + 전위 증감 연산자(`++i`, `--i`)

    ```c
    i = i + 1;
    return i;
    ```

    + 후위 증감 연산자(`i++`, `i--`)

    ```c
    const int temp = i;
    i = i + 1;
    return temp;
    ```

### 2.2 if, switch

## 3. 라이브러리 만들기

- `gcc -c ft_putchar.c` : `*.c` 파일을 `*.o` 파일로 만든다. `-c` 옵션은 main function 없이 컴파일할 수 있도록 한다.
- `ar rc libstr.a ft_putchar.o ft_putstr.o`
    + `*.o` 파일을 가지고 하나의 라이브러리 파일을 만든다.
    + `ar` : 우리가 사용할 커맨드
    + `rc` : 옵션
    + `libstr.a` : 만들 라이브러리 파일 이름이다. 무조건 맨 앞에 `lib`가 prefix로 붙어야 한다. `str`이 라이브러리 이름, `.a` 확장자는 정적 라이브러리를 의미한다. 동적 라이브러리도 존재함.
- `gcc main.c -L. -lstr`
    + main.c 파일을 컴파일한다.
    + `-L.` : 현재 디렉토리에 있는 라이브러리 파일을 사용한다.
    + `-lstr` : -l은 라이브러리를 의미하고, 우리가 만든 라이브러리의 이름을(str) 명시해준다.
- `ranlib libstr.a` : 라이브러리 파일에 함수가 몇 천개고 매우 크면 컴파일할 때나 불러 쓸 때나 느려진다. 명령어는 라이브러리에 인덱스를 생성해준다.

## 4. 매개변수 불러 쓰기

```c
int main(int argc, char **argv);
```

- `argc`
    + 추가로 입력한 것들의 개수를 의미한다.
    + white-space로 구분해서 하나하나 받아들인다. 만약 공백을 포함하고 싶다면 쌍따옴표로 감싸준다.
    + 파일 명이 언제나 들어가기 때문에 argc는 항상 최소 1이다. 즉 argv[0]은 언제나 존재함.
- `argv` : 문자열을 가리키는 포인터가 들어있는 포인터 배열이다.

## 5. 동적 할당

배열의 길이가 정해지지 않았을 때 코드의 변수를 통해 동적으로 할당하는 방법이다.

### 5.1 malloc

```c
#include <stdlib.h>
#define LEN 42

int     main(void)
{
    int     i;
    char    *str;

    str = (char *)malloc(sizeof(*str) * (LEN + 1));
    if (!str)
    {
        memset(str, 0, sizeof(*str) * LEN + 1);
        i = 0;
        while (i < LEN)
        {
            str[i] = '0' + (i % 10);
            i++;
        }
        str[i] = '\0';
        ft_putstr(str);
        ft_putchar('\n');
        free(str);
    }
    else
    {
        ft_putstr("malloc error!\n");
    }
    return (0);
}
```

- `#include <stdlib.h>` 라이브러리 사용한다.
- `(char *)` : malloc의 리턴 타입이 void pointer다. 어떤 타입의 배열일지 알 수 없으니까. 그래서 원하는 형태로 캐스팅해줘야 한다.
- `sizeof(*str) * (LEN + 1)` : 어떤 타입이 배열 안에 들어갈지에 따라 메모리 할당 크기가 달라진다. sizeof 함수를 사용하면 쉽게 원소의 크기를 알 수 있고, 이 경우엔 문자열이므로 널 문자까지 계산해서 길이에 1을 더한 값을 곱해줬다.
- 동적 할당이 안 된 경우를 대비해서 꼭 체크해준다.

### 5.2 calloc

- `void* calloc(size_t elt_count, size_t elt_size);` : 함수 원형이다. 두 번째 매개변수만큼의 크기를 첫 번째 매개변수 개수만큼 할당한다.
    + `arr = (int *)calloc(5, sizeof(int));`
-  malloc과 다른 점은 자동으로 0으로 초기화된다는 점이다.

### 5.3 realloc

- `void* realloc(void* memblock, size_t size);` : 함수의 원형. 첫 번째 매개변수로 이미 할당된 포인터 변수를 넣고, 바꾸고싶은 공간 크기를 두 번째 매개변수로 넣어준다.
    + `realloc(arr, sizeof(int)*10);`
- 이미 동적할당된 변수의 크기를 바꿀 때 사용한다.

### 5.4 memset, free

- `memset`: 원형은 `void *memset(void *ptr_strart, int value, size_t count);`이다. count 크기만큼 value로 값을 대입한다.
- `free(str)`
    + 전체 프로그램이 종료되면 결국 사용한 메모리 모두가 해제되지만 직접 해제해주는 것이 좋다.
    + 동적할당한 함수가 종료되더라도 여전히 메모리는 사용 중이다.
    + 할당 받은 메모리가 함수 내부에서만 사용되었다면 함수안에서 free 해야 하고, 함수가 끝나도 유지되어야 한다면 함수를 호출한 쪽에서 free 해야 한다.
    + 안쪽에서부터 순서대로 해야한다. 만약 문자열이 여러개 들어가있는 더블 포인터라면 문자열 하나 하나에 할당된 메모리를 먼저 해제해준 다음, 각 문자열의 주소를 갖고 있는 바깥 배열을 해제해줘야 한다.
- 정수형 배열 `arr`을 포인터 형태로 함수의 매개변수로 전달할 때
    + `int arr[4];`로 정의했다면 무조건 배열 포인터 `int (*ptr)[4]` 형태로 전달해야 한다. 더블 포인터를 쓸 수 없다.
    + `(int *)malloc(sizeof(*arr) * len)` 형태로 동적할당했다면 `int **ptr` 형태로 매개변수전달이 가능하다.

## 6. 입출력

### 6.1 입력

- `#include <stdio.h>` -> `scanf("%d %s %c", &int, str, &c);` : 입력 포맷을 정해주고 입력된 값이 들어갈 변수의 주소값을 넣어준다.
    + 문자열 입력 조건을 `[]`로 설정해줄 수도 있다. 기본은 white space 기준으로 하나씩 하나씩 읽어들인다.

    ```c
    char str[80];
    scanf("%[12345]s", str); // 12345 숫자만 입력받겠다는 의미
    scanf("%[^12345]s", str); // ^는 not과 같은 의미다. 12345 빼고 입력받음.
    scanf("%[0-9]s", str); // 정규표현식처럼 활용
    scanf("%[^\n]s", str); // 개행문자 만나면 종료. 개행문자 제외하고 입력받음
    scanf("%79[^\n]s", str); // 개행문자까지 입력 받되 79자만 입력받는다.
    scanf("%[a-zA-Z]s", str); // 영문자만 입력
    ```

- `#include <stdio.h>` -> `getchar();` 딱 한 글자 char 타입을 불러온다.
- `#include <unistd.h>` -> `read(1, &buf, 1)` : 왼쪽 예는 char 타입의 buf에서 1바이트를 가져와서 스탠다드 아웃에 출력하는 형태다.
    + 첫 번째 매개변수는 file descriptor. 0, 1, 2의 값이 들어갈 수 있고 스탠다드인, 스탠다드 아웃, 스탠다드 에러를 의미. 어디서 읽어올것인가를 나타낸다.
    + 두 번째 매개변수는 버퍼. 읽어온 값을 어디에 저장할 것인가를 나타낸다.
    + 세 번째 매개변수는 바이트 사이즈. 몇 바이트 읽어올 것인지 정한다.

### 6.2 출력

- `#include <stdio.h>` -> `printf("%d %s %c", int, str, c);` : 가장 쉽고 편한 출력 함수.
- `#include <stdio.h>` -> `putchar(c);` 한 글자 출력
- `#include <unistd.h>` -> `write(1, &c, 1);` : 왼쪽의 예는 캐릭터 하나의 주소값을 받아서 출력하는 형태
    + 첫 번째 매개변수는 file descriptor다. 0, 1, 2로 값을 지정해줄 수 있는데 순서대로 `STDIN`, `STDOUT`, `STDERROR`다. 일반적으론 1을 써서 출력하지만 만약 에러 발생시 출력할 곳을 정한다면 2로 하면 된다.
    + 두 번째 매개변수는 출력할 원료(?) 버퍼다. 버퍼에서 어떤 값을 읽어오게 된다.
    + 세 번째 매개변수는 얼마나 읽어올건지 정하는 바이트 단위 값이다.
    + 썼을 때 성공하면 쓴 바이트 크기를 리턴한다. 실패하면 -1 리턴

### 6.3 커서 이동

- `#include <unistd.h>` -> `lseek(int fd, off_t offset, int whence)`
    + fd는 file descriptor다. offset은 커서를 몇 바이트 이동할건지 정수로 적어준다. off_t 타입은 typedef로 지정해놓은 타입일거다. whence는 offset을 적용할 방식을 나타내는데 아래 세 가지 종류가 있다.
    + `SEEK_SET` : 딱 그 바이트 위치로 커서를 보낸다. 처음으로 보낼 때 offset을 0으로 하고 이 명령어를 적용하면 쉽다.
    + `SEEK_CUR` : 현재 커서 위치에서 offset이 적용된다.
    + `SEEK_END` : 파일의 끝에서부터 offset이 적용된다. 즉 파일의 사이즈 오프셋에서 적용된다고 생각하면 된다.
- 사용 상황
    + 파일에 같은 길이의 문장들이 `'\n'`으로 구분되어 여러개 있다고 가정하자. 각 문장들을 읽어와서 변수에 할당해야한다.
    + 엄청 큰 값을 써서 문자열 배열을 만들고 문자열들을 할당할 수도 있지만 낭비다.
    + 그래서 malloc을 해야 하는데 문장의 길이를 모른다. 그래서 뉴라인 문자 전까지 먼저 파일을 읽어들여서 길이가 얼마인지 알아내야 한다. 근데 파일을 읽을 때는 커서가 이동하기 때문에 커서를 다시 원위치 시켜서 사이즈를 측정한 문장을 다시 읽을 수 있게 해야한다.
    + 그 때 lseek을 사용하면 된다.

```c
#include <unistd.h>

int     get_str_len(void)
{
    char    buf;
    int     len;

    len = 0;
    read(0, &buf, 1);
    while (buf != '\n')
    {
        len++;
        read(0, &buf, 1);
    }
    lseek(0, 0, SEEK_SET);
    return (len);
}
```

### 6.4 파일

- 기본 틀
    + 파일과의 스트림을 열고 -> 제대로 열었는지 체크
    + 닫고 -> 제대로 닫았는지 체크
    + open 매개변수의 의미는 쓰기와 만들기 모드로 열고, 권한 역시 같은 걸로 준다는 의미다.

    ```c
    #include <sys/types.h>
    #include <sys/stat.h>
    #include <fcntl.h>

    int main(void)
    {
        int fd;

        fd = open("file_name", O_WRONLY | O_CREAT, S_IRUSR | S_IWUSR);
        if (fd == -1)
        {
            ft_putstr("open() failed\n");
            return (1);
        }
        ft_putnbr(fd);
        if (close(fd) == -1)
        {
            ft_putstr("close() failed\n");
            return (1);
        }
        return (0);
    }
    ```

- 문자 하나 출력, 문자열 출력 함수. 둘 다 원하는 원하는 파일에다 출력하는 형태로 기존에 써오던 것과는 약간 다르다.

    ```c
    void    ft_putchar(int fd, char c)
    {
        write(fd, &c, 1);
    }

    void    ft_putstr_fd(int fd, char *str)
    {
        write(fd, str, ft_strlen(str));
    }
    ```

- 추가 예제
    + 버프 사이즈를 정해놓고 한방에 크게 읽어온다. 읽어온 바이트를 ret 변수가 저장하기 때문에 그 수치를 이용해서 문자열 끝에 NULL 문자를 넣어줘서 문자열을 마무리한다.

```c
int main(void)
{
    int fd;
    int ret;
    char buf[BUF_SIZE + 1];


    fd = open("42", O_WRONLY | O_CREAT | O_APPEND, S_IRUSR | S_IWUSR);
    if (fd == -1)
    {
        ft_putstr("open() failed\n");
        return (1);
    }
    while (ret = read(fd, buf, BUF_SIZE))
    {
        buf[ret] = '\0';
        ft_putnbr(ret);
        ft_putstr(buf);
    }
    ft_putnbr(fd);
    ft_putchar(fd, 'Z');
    ft_putstr_fd(fd, "Hello World!\n")
    if (close(fd) == -1)
    {
        ft_putstr("close() failed\n");
        return (1);
    }
    return (0);
}
```

## 7. 전처리문

컴파일러가 컴파일하기 전에 처리되는 작업이라서 전처리다. 코드를 하나하나 수정하지 않고 스위치 온/오프하듯 적용할 수 있어서 특정 상황을 조절할 때 사용한다. 종류는 `#define`, `#if`, `#ifdef`, `#ifndef`, `#defined`, `#undef` 등이 있고 항상 첫 문자로 #이 사용된다.

- 파일 처리 : `#include`
- 형태 정의 : `#define`, `#undef`
- 조건 처리 : `#if`, `#ifdef`, `#ifndef`, `#else`, `#elif`, `#endif`
    + `#if` : …이 참이라면
    + `#ifdef` : …이 정의되어 있다면
    + `#ifndef` : …이 정의되어있지 않다면
    + `#else` : #if나 #ifdef에 대응
    + `#elif` : “else + if”의 의미
    + `#endif` : #if, #ifdef, #infdef 의 끝
- 에러 처리 : `#error`
- 디버깅 : `#line`
- 컴파일 옵션 처리 : `#pragma`

### 7.0 헤더 파일

- 헤더 파일을 쓰는 이유는 할 일을 줄이기 위해서다. ft_putchar 함수를 여기저기 수많은 .c 파일에서 불러 쓴다고 했을 때 만약 프로토타입의 수정이 있다면 모든 파일을 열어서 하나하나 선언부를 수정해줘야한다. 헤더파일을 쓴다면 해당 함수와, 헤더파일의 선언부 딱 2가지만 수정하면 되기 때문에 편리하다.
- 예시
    + `main.c` 파일과 `print.c` 파일이 있다고 하자. 그리고 print.c 파일에는 `ft_putchar`, `ft_putstr` 함수가 있다.
    + print.c 파일에서도 ft_putchar, ft_putstr 함수의 순서는 지켜줘야 한다. ft_putstr 함수에서 ft_putchar 함수를 쓰기 때문에 ft_putchar를 위쪽에서 구현해야 한다. 혹은 맨 위에 프로토타입을 선언하든지.
    + 그리고 ft_putchar 함수가 unistd.h의 write 함수를 사용하기 때문에 print.c 파일에서 해당 헤더 파일을 include 해야 한다. main에서는 include할 필요 없고 그냥 쓰는 함수만 맨 위에 선언해주면 된다.

### 7.1 include

- `#include` : 컴파일 전에 특정 파일을 불러온다. 만약 특정 파일을 include 해놓고 `cpp main.c` 명령어를 쳐 보면 어떤 파일을 불러왔는지 볼 수 있다. 정말 단순하게 헤더 파일에 있는 내용들을 위에 붙여넣는 역할을 한다.
- 단순히 붙여넣기만 하기 때문에 만약 `stdio.h`를 사용하는 파일이 여러개라면 수많은 텍스트들이 붙여넣어진다. 그래서 이미 include 되었으면 추가로 include하지 않겠다는 표시를 해야 한다. 그게 ifndef 같은 전처리다.
- 제공되는 라이브러리(stdio.h 또는 stdlib.h 같은)는 `#include <stdio.h>` 형태로 쓸 수 있다. `< >` 표시는 표준 디렉토리에 있다는 말. 사용자가 직접 만든 라이브러리는 `#include "../my_header.h"` 처럼 적어줘야 한다. 헤더가 현재 파일과 다른 경로에 있다면 표시해줘야 함.

### 7.2 define, undef

- `#define TARGET change` : 딱 그 단어만 바꾼다. abc를 xyz로 바꾼다면 앞 뒤 공백으로 구분된 abc만 잡아서 xyz로 바꾼다. zabc, abcz, zabcz는 바꾸지 않는다. 그리고 문자열 내에 있는 단어 역시 바꾸지 않는다.
- define을 쓸 땐 TARGET을 꼭 모두 대문자로 적어줘야 한다. 상수처럼.
- 만약 동적으로 활용하고 싶다면 소괄호를 사용하면 된다. 아래 예제처럼 사용해서 함수처럼 이용할 수도 있다.

    ```c
    #define SUM(x) ((x) = (x) + (x))
    ```

- `#`을 이용하면 소괄호 없이 바로 x 값을 활용할 수 있는데 자동으로 문자열 배열로 치환된다. 근데 `?`는 에러난다. 그냥 이런게 가능하단 정도만 알아두고 쓰지 않겠다.

    ```c
    #define SGB(x) #x
    printf("%d\n", SGB(What the hell is this\n));
    ```

- 지정한 것을 해제도 가능

    ```c
    #define ADD(a, b) (a + b)
    #undef ADD(a, b)
    ```

### 7.3 조건 전처리기

#### 7.3.1 if, endif

```c
#define A 1
#if A
    source code.....
#endif
```

위 코드는 전처리된다. 참 거짓 구분할 수 있고, A 말고 숫자 1을 그대로 써도 된다. 파일의 모든 코드를 다 감쌀 수 있다. 범위 제한 없음.

#### 7.3.2 ifdef

```c
#define MYDEF /* MYDEF는 값은 가지지 않았지만 어쨋든 정의는 되었다 */
#ifdef YOURDEF /* 만약 YOURDEF가 정의되어 있다면... */
# define BASE 10 /* BASE == 10 */
#elif MYDEF /* 그외에 MYDEF가 정의되었다면... */
# define BASE 2 /* BASE == 2 */
#endif
```

- 값을 지정하지 않고 단순히 정의만 하더라도 ifdef에서 참이 된다. 위 코드 결과는 아래 MYDEF 조건 부분에서 통과돼서 BASE가 2로 치환된다.
- 값을 지정하지 않고 선언하면 아무것과도 치환되지 않는다는 의미다. 
- 만약 전처리문 if 내에 다른 전처리문이 들어간다면 위 코드 예제처럼 #은 띄우지 않고 바로 적지만, 다음 내용은 한 칸 띄워주는게 좋다. 한 꺼풀씩 더 깊게 들어갈 수록 스페이스로 빈 칸 한 개씩 추가해주면 된다.

#### 7.3.3 #ifndef 헤더명_H__ ~ #endif

```c
#ifndef STDIO_H__
# define STDIO_H__
#endif

#ifndef __FT_TEST1_H__
# define __FT_TEST1_H__
#endif
```

- .c 파일에서는 그냥 include만 하면 된다. ifndef는 헤더파일에서 하면 된다.
- 헤더 파일이 중복 선언되는 것을 피하기 위해서 주로 사용되는 패턴이다.
- 중복으로 선언되면 신택스 에러가 나기 떄문에 #ifndef를 사용해서 선언되어있으면 선언을 하지 않게 만든다.
- stdio.h 에는 위와 같은 코드가 애초에 삽입되어있다.
- 42에서는 만약 파일명이 `test1.h` 이라면 `__FT_TEST1_H__` 하기로 했다.

### 7.4 선언

- 다른 .c 파일에 있는 함수를 현재 파일에서 쓰려면 맨 위에 선언해줘야 한다.
- 다만 재밌는 것은 다른 파일의 함수의 이름만 똑같이 해주면 리턴 타입과 매개변수는 달라져도 컴파일은 된다. 이렇게 하진 않겠지만 괴상하다.

## 8. typedef

```c
typedef int hello;
```

- 타입을 내가 원하는 것으로 만들 수 있다. 다르게 이름을 지정하는 것.
- 전처리와는 달리 실제로 executable하다.
- 만약 특정 함수 내에서 typedef를 한다면 그 함수의 scope 내에서만 적용된다.
- 기본 자료형에 다른 이름을 붙여준다면 모두 대문자로 하는게 좋다.
- unistd.h의 write 함수를 보면 마지막 매개변수의 타입은 size_t이고, 리턴 타입은 ssize_t다. 함수를 만들고 관리하는 사람이 함수를 정의할 때 typedef를 사용한 것이다. 마치 헤더파일을 사용할 때처럼 쉽게 타입을 한 곳에서 변경할 수 있게 해주는 역할도 한다.
- 주로 구조체 struct를 만들고 그것을 쉽게 가리키기 위해 사용한다.

```c
#define INTP int*
typedef int* int_p;

int main(void)
{
    int *a, b, c;
    INTP d, e, f;
    int_p g, h, i;
    return (0);
}
```

- a, b, c: a만 포인터고 b, c는 그냥 정수형 타입이다.
- d, e, f: 역시 d만 포인터고, e, f는 정수다. 단순히 글자가 바뀐 것일 뿐이기 때문에 a, b, c와 같은 효과다.
- g, h, i: 이 경우는 typedef를 썼기 때문에 모든 변수가 정수 타입의 포인터가 된다.

## 9. Struct - 구조체

### 9.1 기본

- 여러 가지의 데이터가 모여야 하나의 의미를 가지는 종류. 예를 들어 평면 좌표에서 x, y 좌표가 모두 있어야 위치를 나타낼 수 있는 그런 것이다.
- 사용자 정의 자료형이라고도 하며, 내부 변수들은 '멤버'라고 지칭한다.
- 구조체 형태 정의할 때 마지막에 꼭 `;` 붙여줘야한다.
- 선언은 이름에 struct까지 붙여 써서 타입을 지정해줘야 하고, 멤버로의 접근은 `.` 연산자를 이용한다.

### 9.2 선언

```c
struct point
{
    int x;
    int y;
};

struct person
{
    char name[20];
    char phone[20];
};

int main(void)
{
    struct point p1;
    struct person me = {"Gyubin Son", "+82 1053590948"};

    p1.x = 10;
    p1.y = 20;
    return (0);
}
```

- 구조체를 선언함과 동시에 바로 초기화할 때는 배열 초기화처럼 `{ }`를 써서 한 번에 모든 값을 지정해줄 수 있다.
- 하지만 그냥 선언만 하고, 다음 줄에서 대입을 하는 것은 불가능하다. 단순 정수형 타입이라도 안된다. 하나하나 `.`으로 접근해서 값을 넣어야 한다.
- 동시에 초기화할 때 `struct person p = {.age = 20, .name = "Free Lec", .phone = "3142-6702"};` 이렇게 멤버를 지정해서 할 수도 있다.

```c
struct point
{
    int x;
    int y;
};

struct circle
{
    struct point p;
    double radius;
};

int main()
{
    struct circle c1 = {10, 10, 1.5};
    struct circle c2 = {{30, 30}, 2.4};
    struct circle c3 = {{30}, 2.4};
}
```

- 중첩 구조체일 경우 원소 개수를 정확하게 입력하는 경우엔 첫 번째 예제처럼 풀어서 대입하는 것이 가능한데
- 원소 개수를 똑같이 입력할 수 없다면 중괄호로 묶어줘야 한다. 세 번째 예제에서 y 값은 자동으로 0이 된다.

### 9.3 구조체 배열과 포인터

- 일반 배열과 비슷하다. `struct person p_arr[10];` 형태로 가능.
- 포인터를 사용할 때는 `*` 연산자가 `.` 연산자보다 우선순위가 느리기 때문에 첫 번째 원소의 이름 값을 가져오고 싶다면 `(*p_arr).name` 처럼 사용해야 한다. 혹은 `p_arr -> name` 가능.
- 구조체 변수의 주소값과, 구조체 변수의 첫 번째 멤버의 주소값은 일치.
- 구조체 배열에서 원소 간의 주소값 차이는 그 원소의 크기만큼이고 연결돼있다.
    + 만약 구조체가 정수형 하나, 문자열 배열 20짜리 크기 하나라면
    + 배열의 첫 번째 원소인 구조체의 주소값과 정수형 변수의 주소값은 같으며
    + 정수형 크기인 4만큼 이동한 주소값에 문자 배열이 위치하고 시작하며 20만큼 차지한다.
    + 이후 바로 구조체 배열의 다음 원소인 구조체가 위치한다.
- 구조체 간의 사칙연산은 불가능하고 대입 연산 `=` 만 허용된다. 같은 타입일 때만 가능하고 값이 복사된다.

## 10. ENUM - 열거형

```c
enum color {RED = 1, GREEN = 3, BLUE = 5};

int main(void)
{
    enum color c1 = RED;
    enum color c2 = GREEN;
    enum color c3 = BLUE;

    return (0);
}
```

- 글로벌 스코프에서 선언하고, 함수 내에서 값을 받아와서 사용한다.
- 값을 지정해주지 않으면 0부터 1씩 증가한 값이 들어간다.
- 중간에 값을 지정해주면 첫 상수는 무조건 0이고, 지정해준 값 다음 값은 + 1이 되어서 들어간다.
- 만약 열거형이 2개 이상이라면 하나로 합치는 것이 좋다.

```c
enum days {MON, TUE, WED, THU, FRI, SAT, SUN};

int main(void)
{
    enum days day;

    scanf("%d", &day);
    switch (day)
    {
        case MON:
            printf("Hello");
            break;
        case TUE:
            printf("Dude~");
            break;
    }
    return (0);
}
```

## 11. UNION - 공용체

```c
union u_data
{
    int d1;
    double d2;
    char d3;
}

int main(void)
{
    union u_data data;

    data.d1 = 1;
    printf("%d, %f, %c\n", data.d1, data.d2, data.d3);
    data.d2 = 3.3;
    printf("%d, %f, %c\n", data.d1, data.d2, data.d3);
    data.d3 = 'a';
    printf("%d, %f, %c\n", data.d1, data.d2, data.d3);
    return (0);
}
```

- 구조체와 같은 형태지만 다른 용도로 쓰인다.
- 특정 값을 받아야할 때 이것이 정수인지, 실수인지, 캐릭터인지 모를 경우가 있다. 그 때 각각을 모두 선언하기엔 메모리 낭비이기 때문에 결국 하나만 사용하면 되도록 메모리 효율을 좋게 한 형태가 유니언이다.
- 그래서 구조체가 모든 멤버들에게 메모리를 각각 할당해주는 것과 달리 유니언은 가장 큰 멤버의 메모리 크기를 사용하고 그것을 공유한다. 멤버 중 하나에 값이 할당되면 나머지 멤버는 사용할 수 없다.
- 위 예제를 보면 대입된 값 외의 변수의 값은 사용할 수 없다는 것을 알 수 있다.

## 12. 함수 포인터

```c
return_type (*function)(arg1, arg2, ...);
int (*func_name)(char *);
```

- 함수를 매개변수로 넘길 수 있다.
- `void ft_putchar(char c);` 함수를 넘긴다면 `void (*f)(char)` 형태로 나온다. 즉 리턴타입, 매개변수만 잘 맞춰주고 함수 명 앞에 스타를 붙여주면 된다.

```c
int *ft_map(int *arr, int arr_len, int (*db_num)(int));
int double_num(int num);

int main(void)
{
    int *temp;
    int arr[5] = "{1, 2, 3, 4, 5}"

    temp = ft_map(arr, 5, &double_num);
    return (0);
}
```

- 위 예제는 map 함수와 숫자를 2배로 하는 함수를 사용해본 것이다.
- 함수를 넘겨줄 때 `&`를 활용해서 이름만 적어주면 된다.
- 재밌는 것은 함수를 map 안에서 활용할 때는 `(*f)` 형태로 적어주지 않아도 된다. 컴파일러가 알아서 해주기 때문에 그냥 f 형태로 사용하면 된다. `*f`, `************f`도 주소값을 찍어주면 다 똑같다.

## 13. Data Structure - 자료구조

- Data type = data + operation
    + 자료형은 데이터와 연산 명령들이 합해진 개념이다.
    + 예를 들어 정수 자료형이라면 정수 형태의 데이터와 사칙연산 + 나머지 연산이 포함된 개념이다.
- 알고리즘 성능 측정 기준
    + 공간 복잡도(Space Complexity): 얼마나 적은 메모리를 쓰느냐
    + 시간 복잡도(Time Complexity): 얼마나 적은 시간이 걸리느냐
    + 보통 시간에 대한 비용이 공간 비용보다 더 높기 때문에 시간만 주로 쓴다. 하지만 임베디드 쪽에서는 반대가 되기도 한다.
