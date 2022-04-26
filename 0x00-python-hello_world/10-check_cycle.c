#include "lists.h"

/**
* check_cycle - checks if a linked lists has a cycle in it
* @list: singly linked list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{
	listint_t *next1 = list;
	listint_t *next2 = list;

	if (list == NULL)
		return (0);

	while (1)
	{
		if(next2->next != NULL && next2->next->next != NULL)
		{
			next2 = next2->next->next;
			next1 = next1->next;
		
			if (next2 == next1)
				return (1);
		}
		else
			return (0);
	}
}
