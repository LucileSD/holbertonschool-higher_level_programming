#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *newnode, *prev;
	tmp = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
         return (NULL);
	}
	newnode->n = number;

	if (*head != NULL)
	{
		while (tmp->n < number)
		{
			prev = tmp;
			tmp = tmp->next;
		}
	}
	else
		*head = newnode;

	
	prev->next = newnode;
	newnode->next = tmp;

	return (newnode);
}
