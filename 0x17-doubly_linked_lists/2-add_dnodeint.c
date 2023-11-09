#include "lists.h"

/**
 * *add_dnodeint - adds node to list beginning
 * @head: head node
 * @n: data
 * adlistint_t - doubly list node data type
 * Return: New head node
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
dlistint_t *temp = (dlistint_t *)malloc(sizeof(dlistint_t));

if (!temp)
return (NULL);
temp->n = n;
temp->prev = NULL;
temp->next = *head;
*head = temp;

return (temp);
}
