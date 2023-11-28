#include <stdio.h>
#include <stdlib.h>

#define CREATE_TREE_IMPL
#include "create_tree.h"

typedef struct {
    int hight;
    int x;
    int width;
} move;

typedef struct {
    int len;
    move *item;
} moves;

int max(int *arr) {
    int m = 0;
    for (int i = 0; i < 4; i++) {
        if (arr[i] > m)
            m = arr[i];
    }
    return m;
}

int tetris_ric(node *root, int x, int height, int width, int parent_hight) {
    if (root == NULL) {
        return 0;
    }

    int len_tetris_piece = x + width - 1;
    int sx, dx = 0;

    if (root->data >= x && root->data <= len_tetris_piece) {

        root->hight += height;

        if (parent_hight < root->hight)
            parent_hight = root->hight;

        sx = tetris_ric(root->sx, x, height, width, root->hight);
        dx = tetris_ric(root->dx, x, height, width, root->hight);
        int hs[] = {sx, dx, root->hight, parent_hight};
        root->hight = max(hs);
        return root->hight;
    } else if (root->data > len_tetris_piece) {
        sx = tetris_ric(root->sx, x, height, width, parent_hight);
        return sx;
    } else {
        dx = tetris_ric(root->dx, x, height, width, parent_hight);
        return dx;
    }
}

int tetris_call(moves mosse, int n, int m) {
    tree *t = alloc_tree();
    create_tree(t, n);
    visualizeBinaryTree(t, "binary_tree");
    for (int i = 0; i < mosse.len; i++) {
        move mossa = mosse.item[i];
        int game_over =
            tetris_ric(t->root, mossa.x, mossa.hight, mossa.width, 0);
        if (game_over > m) {
            return i + 1;
        }
    }
    return -1;
}

int main() {
    moves *mosse = malloc(sizeof(moves));
    mosse->len = 7;
    mosse->item = malloc(sizeof(move) * mosse->len);

    mosse->item[0].x = 1;
    mosse->item[0].width = 3;
    mosse->item[0].hight = 12;

    mosse->item[1].x = 6;
    mosse->item[1].width = 3;
    mosse->item[1].hight = 3;

    mosse->item[2].x = 2;
    mosse->item[2].width = 5;
    mosse->item[2].hight = 2;

    mosse->item[3].x = 8;
    mosse->item[3].width = 1;
    mosse->item[3].hight = 5;

    mosse->item[4].x = 4; // 4
    mosse->item[4].width = 2;
    mosse->item[4].hight = 3;

    mosse->item[5].x = 2;
    mosse->item[5].width = 2;
    mosse->item[5].hight = 2;

    mosse->item[6].x = 4;
    mosse->item[6].width = 3;
    mosse->item[6].hight = 7;

    int game_over = tetris_call(*mosse, 8, 16);

    printf("Numero di mosse %d", game_over);
}
