#ifndef HELPER
#define HELPER

struct weardrobe 
{
    struct piece *hangers;
    int size; 
};

struct piece 
{
    int category;
    char *color;
    char *texture;
    int *matches;
};

void create_weardrobe(struct weardrobe** wear, int size);

#endif 