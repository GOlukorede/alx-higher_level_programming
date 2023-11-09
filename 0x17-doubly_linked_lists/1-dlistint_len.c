#include "lists.h"

/**
 * dlistint_len - Count number of elements in a list
 * @h: node
 *
 * Return: Number of nodes
 */

size_t dlistint_len(const dlistint_t *h)
{
size_t sum = 0;
while (h != NULL)
{
sum += 1;
h = h->next;
}
printf("%lu elements\n", sum);
return (sum);
}
