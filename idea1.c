#include <stdio.h>

int main(void)
{
    int scores[5] = {88, 92, 75, 96, 80};

    for (int i = 0; i < 5; i++)
    {
        printf("第%d个成绩: %d\n", i + 1, scores[i]);
    }

    return 0;
}
