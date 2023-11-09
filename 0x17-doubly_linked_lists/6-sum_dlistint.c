#include "lists.h"

/**
 * sum_dlistint - Sums all the data of a dlistint_t list.
 * @head: A pointer to the head of the list.
 *
 * Return: Sum of all the data of the list.
 */

int sum_dlistint(dlistint_t *head)
{
int sum = 0;
dlistint_t *temp = head;
while (temp != NULL)
{
sum += temp->n;
temp = temp->next;
}
return (sum);
}
