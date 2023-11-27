#ifdef CREATE_TREE_IMPL
#include <math.h>

typedef struct node {
    int data;
    int hight;
    struct node *sx;
    struct node *dx;
} node;

typedef struct tree {
    int n_nodes;
    node *root;
} tree;

node *alloc_node(int val) {
    node *nd = malloc(sizeof(node));
    nd->sx = NULL;
    nd->dx = NULL;
    nd->data = val;
    nd->hight = 0;
    return nd;
}

tree *alloc_tree() {
    tree *t = malloc(sizeof(tree));
    t->n_nodes = 0;
    t->root = NULL;
    return t;
}

void create_tree_p(node *root, int i, int n) {
    int m = (n - i) / 4;
    if (m * 2 < 1)
        return;
    node *sx = alloc_node(i + m);
    node *dx = alloc_node(n - m);
    root->sx = sx;
    create_tree_p(root->sx, i, root->data);
    root->dx = dx;
    create_tree_p(root->dx, root->data, n);
}

void create_tree(tree *t, int n) {
    int i = 0;
    while (pow(2, i) <= n) {
        i++;
    }
    n = pow(2, i);
    t->n_nodes = n;
    t->root = alloc_node(n / 2);
    create_tree_p(t->root, 0, n);
}

// Function to generate DOT code for the binary tree
void generateDotCode(node *root, FILE *dotFile) {
    if (root == NULL) {
        return;
    }

    fprintf(dotFile, "%d [label=\"%d\"];\n", root->data, root->data);

    if (root->sx != NULL) {
        fprintf(dotFile, "%d -- %d;\n", root->data, root->sx->data);
        generateDotCode(root->sx, dotFile);
    }

    if (root->dx != NULL) {
        fprintf(dotFile, "%d -- %d;\n", root->data, root->dx->data);
        generateDotCode(root->dx, dotFile);
    }
}

// Function to visualize the binary tree using Graphviz
void visualizeBinaryTree(tree *t, const char *filename) {
    FILE *dotFile = fopen(filename, "w");
    if (dotFile == NULL) {
        perror("Error opening DOT file");
        exit(EXIT_FAILURE);
    }

    fprintf(dotFile, "graph BinaryTree {\n");
    generateDotCode(t->root, dotFile);
    fprintf(dotFile, "}\n");

    fclose(dotFile);

    // Use Graphviz's dot command to generate the image
    char command[100];
    snprintf(command, sizeof(command), "dot -Tpng %s -o %s.png", filename,
             filename);
    system(command);
}
#endif
