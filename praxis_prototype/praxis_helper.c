#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "praxis_helper.h"

void create_weardrobe(struct weardrobe** wear, int size)
{
    *wear = (struct weardrobe*) malloc(sizeof(struct weardrobe));
    (*wear) -> size = size;
    (*wear) -> hangers = (struct piece *) malloc(sizeof(struct piece) * size);
}

void add_item(struct weardrobe* wear, int position, char* name, int category, char *color, char *texture, int *matches)
{
    wear -> hangers[position].name = name;
    wear -> hangers[position].category = category;
    wear -> hangers[position].matches = matches;
    wear -> hangers[position].texture = texture;
    wear -> hangers[position].color = color;
}

void view_item(struct weardrobe* wear, int position)
{
    printf("Name: %s\n", wear -> hangers[position].name);
    printf("Color: %s\n", wear -> hangers[position].color);
    printf("Texture: %s\n", wear -> hangers[position].texture);
    printf("Group: %i\n", wear -> hangers[position].category);
}

int find_match(struct weardrobe* wear, int position)
{
    int n = wear -> hangers[position].matches[0];
    int idx_selected = 1 + (rand() % n);
    printf("n = %i\n", idx_selected);
    return wear -> hangers[position].matches[idx_selected];
}