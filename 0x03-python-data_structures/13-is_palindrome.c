#include "lists.h"

/**
 * is_palindrome - checks wether a linked list is palindome
 * @head: head node
 * Return: 1 if is pallindome otherwise 0
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *past = NULL, *prev = NULL;

	slow = *head;
	fast = *head;

	if (*head == NULL)
		return (1);

	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}

	while (slow)
	{
		past = slow->next;
		slow->next = prev;
		prev = slow;
		slow = past;
	}
	
	slow = prev;
	fast = *head;

	while (slow != NULL)
	{
		if (slow->n != fast->n)
			return (0);
		slow = slow->next;
		fast = fast->next;
	}
	return (1);
}
