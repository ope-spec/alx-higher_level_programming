#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @linked_list: pointer to the head of the list
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *linked_list)
{
listint_t *slow, *fast;

if (linked_list == NULL)
return (0);

slow = linked_list;
fast = linked_list->next;

while (fast != NULL && fast->next != NULL)
{
if (slow == fast)
return (1);

slow = slow->next;
fast = fast->next->next;
}

return (0);
}
