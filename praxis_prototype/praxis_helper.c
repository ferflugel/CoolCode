#include <stdio.h>
#include <stdlib.h>
#include "praxis_helper.h"

void create_weardrobe(struct weardrobe** wear, int size)
{
    *wear = (struct weardrobe*) malloc(sizeof(struct weardrobe));
    (*wear) -> size = size;
    (*wear) -> hangers = (struct piece *) malloc(sizeof(struct piece) * size);
}

void add_item(struct weardrobe* wear, int position, char* name, int category, int *matches)
{
    wear -> hangers[position].name = name;
    wear -> hangers[position].category = category;
    wear -> hangers[position].matches = matches;
}

int find_match(struct weardrobe* wear, int position)
{
    return wear -> hangers[position].matches[0];
}