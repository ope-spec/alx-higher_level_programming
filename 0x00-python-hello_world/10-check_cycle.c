#include "lists.h"

/**
* check_cycle - determines whether or not a singly
* linked list contains a cycle
* @linked_list: pointer to the head of the list
*
* Return: If there is no cycle, it is 0, otherwise it is 1.
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
