#include <stdio.h>
#include <string.h>

struct User 
{
    char username[50];
    int level;
};

int main(void)
{
    struct User hacker1;
    strcpy(hacker1.username, "Alice");
    hacker1.level = 5;

    printf("Username: %s\n", hacker1.username);
    printf("Level: %d\n", hacker1.level);

    struct User hacker2 = {"Bob", 10};
    printf("Username:%s, Level: %d\n", hacker2.username, hacker2.level);

    return 0;
}
