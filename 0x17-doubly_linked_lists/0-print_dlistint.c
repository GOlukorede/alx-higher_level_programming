#include "lists.h"

/**
 * print_dlistint - print values of doubly linked list
 * @h: node
 *
 * Return: Number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
int data;
size_t sum = 0;
while (h != NULL)
{
sum += 1;
data = h->n;
printf("%d\n", data);
h = h->next;
}
printf("%lu elements\n", sum);
return (sum);
}
