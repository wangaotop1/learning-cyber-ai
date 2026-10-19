#include <stdio.h>
#include <string.h>

int main(void)
{
    char correct_pwd[] = "cyber2026";
    char input_pwd[20];
    printf("请输入密码: ");
    scanf("%19s", input_pwd);

    if (strcmp(correct_pwd, input_pwd) == 0)
    {
        printf("密码正确，访问成功！\n");
    } else 
    {
        printf("密码错误，访问失败！\n");
    }

    return 0;
}