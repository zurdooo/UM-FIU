// #include <stdlib.h>
#include <stdio.h>
#include <math.h>

// ! Example 123, 132, 231, 213, 312, 321,

void print_permutations(int random_1, int random_2, int random_3)
{
    int perms[3] = {random_1,
                    random_2,
                    random_3};

    // for (int i = 0; i <= 2; i++)
    // {
    //     for (int j = 0; j <= 2; j++)
    //     {
    //         for (int k = 0; k <= 2; k++)
    //         {
    //             if (i != j && i != k && j != k)
    //             {
    //                 printf("%d%d%d\n", perms[i], perms[j], perms[k]);
    //             }
    //         }
    //     }
    // }

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            int a = i;
            int b = (i + j + 1) % 3;
            int c = (3 - a - b);

            printf("%d%d%d\n", perms[a], perms[b], perms[c]);
        }
    }
    return;
}

// int main()
// {
//     int digit;
//     printf("Enter Num: ");
//     scanf("%d", &digit);

//     if (digit < 3)
//     {
//         printf("%d -> Must be bigger than or equal to 3", digit);
//         return 0;
//     }

//     // Grab three positive integers less than or equal to 3
//     int random_1 = digit;
//     int random_2 = digit - 1;
//     int random_3 = digit - 2;

//     print_permutations(random_1, random_2, random_3);

//     return 0;
// }

int main()
{
    int c1;
    while ((c1 = getchar()) != EOF)
        if (c1 == '\t')
            printf(" \\t ");
        else if (c1 == '\n')
            printf("\\n\n");
        else if (c1 == '\\')
            printf("\\\\");
        else
            putchar(c1);
    return (0);
}
