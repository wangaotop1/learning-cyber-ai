#include <stdio.h>

int main(void)
{
    int scores[5] = {88, 92, 75, 96, 80};
    int temp;

    for (int i = 0; i < 4; i++)
    {

        for (int j = 0; j < 4 - i; j++)
        {

            if (scores[j] > scores[j + 1])
            {
                temp = scores[j];
                scores[j] = scores[j + 1];
                scores[j + 1] = temp;
            }
        }
    }

    printf("从小到大的顺序是：");
    for (int i = 0; i < 5; i++)
    {
        printf("%d ", scores[i]);
    }
    printf("\n");

    return 0;
}