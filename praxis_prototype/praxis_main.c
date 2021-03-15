#include <stdio.h>
#include <stdlib.h>
#include "praxis_helper.h"

int main(void)
{
    struct weardrobe *my_weardrobe;
    create_weardrobe(&my_weardrobe, 5);
    // my_weardrobe -> hangers[0].name = "White cool shirt";
    // my_weardrobe -> hangers[0].category = 1;
    add_item(my_weardrobe, 0, "Madrid Jersey", 2);
    printf("%s is in category %i\n", my_weardrobe -> hangers[0].name, my_weardrobe -> hangers[0].category);
}