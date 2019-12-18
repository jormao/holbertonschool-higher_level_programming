#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head to sigle linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int count = 0, rev = 0, adv = 0;
	char str_new[100];

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	while (current)
	{
		count++;
		str_new[count - 1] = current->n;
		current = current->next;
	}
	rev = (count / 2) - 1;
	if (count % 2 == 0)
		adv = (count / 2);
	else
		adv = (count / 2) + 1;
	while (rev >= 0)
	{
		if (str_new[rev] != str_new[adv])
			return (0);
		rev--;
		adv++;
	}
	free(current);
	return (1);
}
