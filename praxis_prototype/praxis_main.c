#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "praxis_helper.h"

int main(void)
{
    // Creating the weardobe 
    srand(time(NULL));
    struct weardrobe *my_weardrobe;
    create_weardrobe(&my_weardrobe, 10); // <- max number of clothes

    // Adding the pieces of clothes to the weardrobe 
    int a[] = {1, 0};
    int b[] = {2, 1, 2}; // {length, idx1, idx2, ..., idxn}
    add_item(my_weardrobe, 0, "Madrid Jersey", 1, "White", "Nylon" ,b);
    add_item(my_weardrobe, 1, "Nike pants", 2, "Black", "Cotton", a);
    add_item(my_weardrobe, 2, "Adidas pants", 2, "Black", "Cotton", a);

    // Basic testing
    printf("%s is in category %i\n", my_weardrobe -> hangers[0].name, my_weardrobe -> hangers[0].category);
    printf("%s is in category %i\n", my_weardrobe -> hangers[1].name, my_weardrobe -> hangers[1].category);

    // This block of code will change with time because the function includes rand()
    int match_for_madrid = find_match(my_weardrobe, 0);
    printf("%s matches with %s\n", my_weardrobe -> hangers[0].name, my_weardrobe -> hangers[match_for_madrid].name);

    // This block tests the information file of a clothe
    view_item(my_weardrobe, 1);
}