#include <stdio.h>

int main() {
    // 外层循环控制行数 (i 从 1 到 9)
    for (int i = 1; i <= 9; i++) {
        // 内层循环控制每一行的列数 (j 从 1 到 i)
        for (int j = 1; j <= i; j++) {
            printf("%d*%d=%-2d  ", j, i, i * j); 
            // %-2d 表示输出整数，占2个字符宽度，左对齐，这样排版更整齐
        }
        printf("\n"); // 每一行打印完后换行
    }
    return 0;
}