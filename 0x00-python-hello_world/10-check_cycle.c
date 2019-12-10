#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checks if there is a loop in the linked list
 * @list: pointer to head of list
 * Return: 0 if there isn't a loop, 1 if there is a loop
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle;
	listint_t *rabbit;

	turtle = list;
	rabbit = list->next;

	while (rabbit && rabbit->next)
	{
		if (turtle == rabbit)
			return (1);
		turtle = turtle->next;
		rabbit = rabbit->next->next;
	}
	return (0);
}
