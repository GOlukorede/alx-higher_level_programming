#include "lists.h"

/**
 * *get_dnodeint_at_index - Returns nth node of a listint_t linked list.
 * @head: head node
 * @index: index of the nth node
 * Return: nth node
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
dlistint_t *temp = head;
while (temp != NULL && index > 0)
{
temp = temp->next;
index--;
}
return (temp);
}
