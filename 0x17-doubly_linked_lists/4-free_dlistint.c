#include "lists.h"

/**
 * free_dlistint - Function that frees a dlistint_t list.
 * @head: head node
 * Return: void
 */

void free_dlistint(dlistint_t *head)
{
dlistint_t *current;

while (head != NULL)
{
current = head;
head = head->next;
free(current);
}
}
