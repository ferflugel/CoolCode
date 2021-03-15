#include <stdio.h>
#include <stdlib.h>
#include "praxis_helper.h"

void create_weardrobe(struct weardrobe** wear, int size)
{
    *wear = (struct weardrobe*) malloc(sizeof(struct weardrobe));
    (*wear) -> size = size;
    (*wear) -> hangers = (struct piece *) malloc(sizeof(struct piece) * size);
}

void add_item(struct weardrobe* wear, int position, char* name, int category)
{
    wear -> hangers[0].name = name;
    wear -> hangers[0].category = category;
}