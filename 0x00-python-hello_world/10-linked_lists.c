#include "lists.h"

/**
 * print_listint - print the list of integers in linked list
 * @h: head of linked list
 * Return: the size of linked list otherwise 0;
 */

size_t print_listint(const listint_t *h)
{
	size_t count = 0;

	if (!h)
	{
		return (0);
	}

	while (h)
	{
		printf("%d\n", h->n);
		h = h->next;
		count++;
	}
	return (count);
}

/**
 * add_nodeint - adds a new node at beggining
 *
 * @head: head of linked list
 * @n: integer elelment of lnked list
 *
 * Return: the new node created otherwise NULL;
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *n_node;


	n_node = (listint_t *)malloc(sizeof(listint_t));
	if (!n_node)
	{
		free(n_node);
		return (NULL);
	}
	n_node->n = n;
	n_node->next = *head;

	*head = n_node;

	return (n_node);
}

/**
 * free_listint - free the memory allocated
 * @head: head node
 */

void free_listint(listint_t *head)
{
	listint_t *tmp;

	while (head)
	{
		tmp = head->next;
		free(head);
		head = tmp;
	}
}
