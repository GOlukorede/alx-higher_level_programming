#include "lists.h"

/**
 * *add_dnodeint_end - adds node to end of the list
 * @head: head node
 * @n: data
 * Return: New node
 */

dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
dlistint_t *temp = (dlistint_t *)malloc(sizeof(dlistint_t));

if (!temp)
	return (NULL);

temp->n = n;
temp->prev = NULL;
temp->next = NULL;

if (*head == NULL)
{
*head = temp;
}
else
{
dlistint_t *current = *head;

while (current->next != NULL)
{
current = current->next;
}
current->next = temp;
temp->prev = current;
}
return (temp);
}
