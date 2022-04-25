#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: the header of the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortue, *lievre;
	tortue = lievre = list;

	while(tortue && lievre && lievre->next)
	{
		tortue = tortue->next;
		lievre = lievre->next->next;

		if (tortue == lievre)
			return (1);
	}
	return (0);
}
