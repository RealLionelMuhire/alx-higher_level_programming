#include "lists.h"

/**
 * check_cycle - finds the loop in the linked list
 * @head: of linked list
 * Return: 1 at first looping node otherwise 0
 */

int check_cycle(listint_t *head)
{
	/*declare a fast pointer and a slow pointer*/
	listint_t *slow, *fast;

	if (!head)
		return (0);

	slow = head;
	fast = head;

	/*iterate through each loop*/
	while (fast && fast->next)
	{
		/*the slow ptr move next to next */
		slow = slow->next;
		/*the fast pointer moves faster X2 than slower*/
		fast = fast->next->next;

		/*if there is a loop, then slow and fast are equal*/
		if (slow == fast)
		{
			/*reset the slow to head*/
			slow = head;

			/*
			 * when they meet again it means that it is
			 * begining of a loop
			 */
			while (fast != slow)
			{
				fast = fast->next;
				slow = slow->next;
			}
			/*returning the first catch up*/
			return (1);
		}
	}
	/*no loop found*/
	return (0);

}
