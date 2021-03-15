#include <stdio.h>
#include <stdlib.h>
#include "praxis_helper.h"

int main(void)
{
    struct weardrobe *my_weardrobe;
    create_weardrobe(&my_weardrobe, 5);
    printf("Okay\n");
}