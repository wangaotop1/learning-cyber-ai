#include <stdio.h>

int main() {
    float c, f; // 定义两个浮点型变量，代表摄氏度和华氏度

    printf("请输入摄氏度温度: ");
    scanf("%f", &c); // 注意：float 类型用 %f，前面必须加 & 取地址符

    f = c * 9.0 / 5.0 + 32.0; // 转换公式

    printf("转换后的华氏度是: %.2f\n", f); // %.2f 表示保留两位小数

    return 0;
}