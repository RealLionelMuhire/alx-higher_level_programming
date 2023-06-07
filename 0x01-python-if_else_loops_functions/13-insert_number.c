#include "lists.h"

/**
 * insert_nodeint_at_index - inserts a new node at a given position
 * @n: data for inserted node
 * @head: head node of linked list
 * @idx: index place
 * Return: added node otherwise NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	/*declare n_node, tmp and conter*/
	listint_t *n_node, *tmp;
	int count = 0;
	/*initialize n_node*/
	n_node = (listint_t *)malloc(sizeof(listint_t));
	if (!n_node)
	{
		return (NULL);
	}

	/*if index is 0*/
	if (number == 0 && *head)
	{
		n_node->next = *head;
		*head = n_node;
		return (n_node);
	}
	/*assign head to tmp*/
	tmp = *head;
	/*iterate to find the index*/
	while (tmp)
	{
		if (count == number - 1)
		{
			n_node->next = tmp->next;
			tmp->next = n_node;
			return (n_node);
		}
		count++;
		tmp = tmp->next;
	}
	free(n_node);
	return (NULL);
}
