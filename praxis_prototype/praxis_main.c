#include <stdio.h>
#include <stdlib.h>
#include "praxis_helper.h"

int main(void)
{
    struct weardrobe *my_weardrobe;
    create_weardrobe(&my_weardrobe, 5);
    // my_weardrobe -> hangers[0].name = "White cool shirt";
    // my_weardrobe -> hangers[0].category = 1;
    int a[] = {0};
    int b[] = {1};
    add_item(my_weardrobe, 0, "Madrid Jersey", 1, b);
    add_item(my_weardrobe, 1, "Nike pants", 2, a);
    printf("%s is in category %i\n", my_weardrobe -> hangers[0].name, my_weardrobe -> hangers[0].category);
    printf("%s is in category %i\n", my_weardrobe -> hangers[1].name, my_weardrobe -> hangers[1].category);

    int match_for_madrid = find_match(my_weardrobe, 0);
    printf("%s matches with %s\n", my_weardrobe -> hangers[0].name, my_weardrobe -> hangers[match_for_madrid].name);
}