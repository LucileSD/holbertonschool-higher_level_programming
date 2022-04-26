#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *newnode, *prev = NULL;
	tmp = *head;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
         return (NULL);
	}
	newnode->n = number;

	if (*head != NULL)
	{
		while (tmp && tmp->n < number)
		{
			prev = tmp;
			tmp = tmp->next;
		}
		if (!prev)
		{
			*head = newnode;
			newnode->next = tmp;
		}
		else
		{
			prev->next = newnode;
			newnode->next = tmp;
		}
	}
	else
	{
		*head = newnode;
		newnode->next = 0;
	}
	return (newnode);
}
