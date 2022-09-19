#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *restart;
	listint_t *start;

	if (list == NULL)
		return (0);
	start = list;
	restart = list->next;
	while (start && restart && restart->next)
	{
		if (start == restart)
			return (1);
		start = start->next;
		restart = restart->next->next;
	}
	return (0);
}
