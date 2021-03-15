#ifndef HELPER
#define HELPER

struct weardrobe 
{
    struct piece *hangers;
    int size; 
};

struct piece 
{
    char *name; // Any name
    int category; // Number (predefined)
    char *color;
    char *texture;
    int *matches; // Indexes of matches
};

void create_weardrobe(struct weardrobe** wear, int size);

void add_item(struct weardrobe* wear, int position, char* name, int category, char *color, char *texture, int *matches);

void view_item(struct weardrobe* wear, int position);

int find_match(struct weardrobe* wear, int position);

#endif 